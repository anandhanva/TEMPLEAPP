# Prepare and pass the dictionary to db and generate QR Link by storing generated qr to cloud link
from pymongo import collation, collection, database
from b_core.statics import dbconstants
import random
from b_core.platformlayers import constantslayer
from datetime import datetime
from Crypto.Hash import RIPEMD160
import base64
import math


def createOrder(data):
    data['database'] = "templeapp"
    data['collection'] = "order"
    datadict = {}
    print("REQUEST DATAAAA",data)
    datadict['order_id'] = str(random.randint(999999,999999999)) + "TT" + str(random.randint(9999,9999999))
    countdocs = dbconstants.MongoAPI(data).count({})
    datadict['order_seqno'] = int(countdocs) + 1
    # datadict['order_date'] = data['req_timestamp']
    datadict['order_item'] = data['datafrm']
    usrdata = getUserId(data['datafrm']['reqdata']['customerMob'])
    print("*******************************", usrdata)
    datadict['orderby_userid'] = usrdata['user_id']
    datadict['order_status'] = 1
    datadict['payment_id'] = str(random.randint(999999,999999999)) + "PAY" + str(random.randint(9999,9999999))
    datadict['createdat'] = str(datetime.now())
    datadict['payment_status'] = 0
    cretordr = dbconstants.MongoAPI(data).write(datadict)
    if cretordr['Status']=="Successfully Inserted":
        return {"Status": datadict['order_id'], "createdat": datadict['createdat']}
    else:
        return {"Status":"Failed"}


def createQRfromDict(dict):
    retdata = constantslayer.createQRCode(dict)
    return retdata


def getUserId(id):
    print("GetUserData", id)
    requ = {}
    dbQuery2 = {"user_phone": id}
    requ['database'] = "temple"
    requ['collection'] = "users"
    userid = dbconstants.MongoAPI(requ).readOne(dbQuery2)
    return userid

# Code to read the qr data and prepare database lookup
def readQRdata(data):
    print("ReadQRData", data)
    data['database'] = "temple"
    data['collection'] = "order"
    datadict1 = {}
    datadict1['order_id']=getOrderId(data['datafrm']['qr_value'])
    dbquery3 = { 'order_id':datadict1['order_id'] }
    dataval = dbconstants.MongoAPI(data).readOne(dbquery3)
    return dataval

def getOrderId(id):
    request2 = {}
    dbQuery2 = {"qr_value":id}
    request2['database'] = "temple"
    request2['collection'] = "qr"
    oderid = dbconstants.MongoAPI(request2).readOne(dbQuery2)
    print("Orderid resp", oderid)
    return oderid['qr_orderid']

# Lookup the prepared query from above module to decode the data
def returnDataforQRfromdb(data):
    dbQuery = {"order_id":data['order_id']}
    data['database']="temple"
    data['collection']="order"
    return dbQuery

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

def returnValues(data):
    retData = returnDataforQRfromdb(data)
    dd={}
    dd['order_id'] = data['order_id']
    dd['amount'] = data['datafrm']['total']['amountpayable']
    dd['timestamp'] = data['createdat']
    hashval = dd['order_id'] + dd['amount'] + dd['timestamp']
    hashvalbin = ''.join(format(ord(x), 'b') for x in hashval)
    # hashvalbin = bytes(hashvalbin, 'utf-8')
    return str(hashvalbin)


def qrhandler(data):
    # Create the Order entry in the database orders table
    orderid = createOrder(data)
    print(orderid)
    data['order_id'] = orderid['Status']
    data['createdat'] = orderid['createdat']
    # If creation of order is successful, proceed
    if orderid['Status'] != "Failed":
        #Create values for QR hash in RIPEMD160
        qrdict = returnValues(data)
        # Generate QR and Return path of the Image
        qrimg = createQRfromDict(qrdict)
        #Prepare other values to be entered into the QR table
        qd={}
        qd['qr_orderid'] = data['order_id']
        qd['qr_createdat'] = data['createdat']
        qd['qr_imgurl'] = qrimg
        qd['qr_value'] = qrdict
        qd['qr_id'] = getrowid("qr")
        #Perform Insert into QR table
        data['database'] = "temple"
        data['collection'] = "qr"
        writetoQRtable = dbconstants.MongoAPI(data).write(qd)
        #Prepare and send response to backend
        qd.pop('_id')
        return sendResponse2BE(qd)
    # Return failed Status
    else:
        return {"Status":"Failed"}

def getrowid(tablename):
    cn = {}
    cn['database'] = "temple"
    cn['collection'] = tablename
    countdocs = dbconstants.MongoAPI(cn).count({})
    return int(countdocs) + 1

def sendResponse2BE(qd):
    imageurl = qd['qr_imgurl'];
    with open(imageurl, "rb") as img_file:
        my_image = base64.b64encode(img_file.read())
    qd['imagedata'] = my_image
    return qd