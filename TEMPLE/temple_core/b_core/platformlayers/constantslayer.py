from flask.globals import request
from b_core.maass import maasslogger
import json
from b_core.statics import staticfunctions,staticconstants,dbconstants
from b_core.platformlayers import standardresponses
import re
from b_core.statics import dbconstants
import json,jsonschema
from jsonschema import validate
import qrcode
from PIL import Image
import random
 
#Install pip3 install qrcode
#Install pip3 install pillow
# Needs a folder qrcodes/generated in the same location as this file
 


def parseRequestHCRD(request):
    try:
        #Convert Request to dictionary
        reqdata = convinptodict(request)
    except Exception as e:
        #Log exception
        maasslogger(request, str(e))
        return str(e)

    print(reqdata)
    #parse by pre defined request data
    hashfrmInput = reqdata['hashstr']
    checksumfrmInput = reqdata['checksum']
    datafrmInput = reqdata['requestdata']
    #prepare a return dictionary
    retaftrParsed = {}
    retaftrParsed['hashstr'] = hashfrmInput
    retaftrParsed['checksum'] = checksumfrmInput
    retaftrParsed['datafrm'] = datafrmInput
    return retaftrParsed

def convinptodict(input):
    #check input data type
    if(isinstance(input, dict)):
        #it is already dict
        return input
    elif(isinstance(input, str)):
        #convert string to dictionary
        return json.loads(input)
    elif(isinstance(input, int)):
        #convert int to dictionary
        return json.loads(input)
    else:
        return json.loads(json.dumpsinput)


def createHashfromData(request, modulename):
    #Extract Data
    hashabledata = convinptodict(request)
    print("HASHABLEDATA",hashabledata)
    rethashableonly = hashabledata
    print("RETHASHABLEONLY",rethashableonly)
    #Prepare Data
    hashinput = preparehash(rethashableonly)
    print("HASHINPUT",hashinput)
    hashinput = json.dumps(hashinput)
    #Convert to Hash
    print("HAAAASH",hashinput)
    print("MODULENAME",modulename)

    hashh = callmaass4hashing(hashinput, modulename)
    print("HASSHH***",hashh)
    #Return Hash
    return hashh

def preparehash(dataset):
    # print("request",request)
    hashstr = re.sub("{","||||",str(dataset)) # replace open brackets
    hashstr = re.sub("}","||||",hashstr) # replace close brackets
    hashstr = re.sub(":","|",hashstr) # replace semicolons
    hashstr = re.sub(" ","",hashstr) # replace spaces
    hashifyrequestdata = re.sub(",","||",hashstr) # replace commasz
    return hashifyrequestdata

def validateJSON(jsonData, schemaname):
    str1 = {}
    try:
        validated = validate(instance=jsonData, schema=schemaname)
    except jsonschema.exceptions.ValidationError as err:
        return {"resp_type": "failure"}
    return {"resp_type": "success"}


def callmaass4hashing(hashinput, modulename):
    # requestDataJson=json.dumps(hashinput)
    # print("REQUESTDATA",requestDataJson)
    configparams = staticfunctions.getUrlsbyModule(modulename)
    
    # configparams = json.dumps(configparams)
    print("CONFIG",configparams)
    logdata = {}
    logdata['parameters'] = configparams
    logdata['data'] = hashinput
    print("LOGDATA",logdata)
    print("LOGDATA",type(logdata))

    respfrmmasshash = staticfunctions.performRequest(logdata)
    # checkUserServers,standardresponses.checkUserHeaders,requestDataJson,standardresponses.checkUserReqType,standardresponses.checkUserMethodType,standardresponses.checkUserEndpoint)
    return respfrmmasshash
    # print("RESPFROMMAASS",respfrmmasshash)

# Function to create a qr code image 
def createQRCode(data):
    # Logo_link = imgurl
    # logo = Image.open(Logo_link)  
    # taking base width
    basewidth = 100  
    # adjust image size
    # wpercent = (basewidth/float(logo.size[0]))
    # hsize = int((float(logo.size[1])*float(wpercent)))
    # logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )  
    # taking url or text
    url = data
    # addingg URL or text to QRcode
    QRcode.add_data(url)
    # generating QR code
    QRcode.make()
    # Choosing color for QR
    QRcolor = 'Black'
    # adding color to QR code
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')
   
    # set size of QR code
    # pos = ((QRimg.size[0] - logo.size[0]) // 2,
    #     (QRimg.size[1] - logo.size[1]) // 2)
    # QRimg.paste(logo, pos)
    pathName = "qrcodes/generated/"
    fileName = str(random.randint(10000000,9999999999)) +'.png'
    # save the QR code generated
    pathofQRFile = pathName + fileName
    QRimg.save(pathofQRFile)
    # print('QR code generated!')
   
    return pathofQRFile
 
#  qrdata = createQRCode("DSFYGD9SFGBTDS9G6DFG7TDFB7GTDS7BTDSFGBT6SDFGDS7TVSADNF6GSADF")