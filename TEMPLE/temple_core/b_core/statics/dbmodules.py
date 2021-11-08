import json
from b_core.statics import dbconstants

#LOGIN TABLE
def login(query,datadict,op,login):
    d1 = {}
    d1['collection'] = login
    d1['database'] = "templeapp"
    if op=='i':
        datavalue = dbconstants.MongoAPI(d1).write(datadict)
        return datavalue
    elif op=='u':
        datavalue = dbconstants.MongoAPI(d1).update(query)
        return json.loads(datavalue)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(d1).read(query)
        return json.loads(datavalue)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(d1).readOne(query)
        return json.loads(datavalue)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(d1).count(query)
    elif op=='d':
        datavalue = dbconstants.MongoAPI(d1).delete(query)
        return datavalue

#home
def home(query,datadict,op,home):
    d1 = {}
    d1['collection'] = home
    d1['database'] = "templeapp"
    if op=='i':
        datavalue = dbconstants.MongoAPI(d1).write(datadict)
        return datavalue
    elif op=='u':
        datavalue = dbconstants.MongoAPI(d1).update(query)
        return json.loads(datavalue)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(d1).read(query)
        return json.loads(datavalue)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(d1).readOne(query)
        return json.loads(datavalue)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(d1).count(query)
    elif op=='d':
        datavalue = dbconstants.MongoAPI(d1).delete(query)
        return datavalue

#pooja
def  pooja(query,datadict,op,pooja):
    d1 = {}
    d1['collection'] = pooja
    d1['database'] = "templeapp"
    if op=='i':
        datavalue = dbconstants.MongoAPI(d1).write(datadict)
        return datavalue
    elif op=='u':
        datavalue = dbconstants.MongoAPI(d1).update(query)
        return json.loads(datavalue)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(d1).read(query)
        return json.loads(datavalue)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(d1).readOne(query)
        return json.loads(datavalue)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(d1).count(query)
    elif op=='d':
        datavalue = dbconstants.MongoAPI(d1).delete(query)
        return datavalue


#prathishta
def  prathishta(query,datadict,op,pradhishta):
    d1 = {}
    d1['collection'] = pradhishta
    d1['database'] = "templeapp"
    if op=='i':
        datavalue = dbconstants.MongoAPI(d1).write(datadict)
        return datavalue
    elif op=='u':
        datavalue = dbconstants.MongoAPI(d1).update(query)
        return json.loads(datavalue)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(d1).read(query)
        return json.loads(datavalue)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(d1).readOne(query)
        return json.loads(datavalue)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(d1).count(query)
    elif op=='d':
        datavalue = dbconstants.MongoAPI(d1).delete(query)
        return datavalue

#offering
def  offering(query,datadict,op,offering):
    d1 = {}
    d1['collection'] = offering
    d1['database'] = "templeapp"
    if op=='i':
        datavalue = dbconstants.MongoAPI(d1).write(datadict)
        return datavalue
    elif op=='u':
        datavalue = dbconstants.MongoAPI(d1).update(query)
        return json.loads(datavalue)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(d1).read(query)
        return json.loads(datavalue)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(d1).readOne(query)
        return json.loads(datavalue)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(d1).count(query)
    elif op=='d':
        datavalue = dbconstants.MongoAPI(d1).delete(query)
        return datavalue


#CART
def  cart(query,datadict,op,cart):
    d1 = {}
    d1['collection'] = cart
    d1['database'] = "templeapp"
    if op=='i':
        datavalue = dbconstants.MongoAPI(d1).write(datadict)
        return datavalue
    elif op=='u':
        datavalue = dbconstants.MongoAPI(d1).update(query)
        return json.loads(datavalue)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(d1).read(query)
        return json.loads(datavalue)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(d1).readOne(query)
        return json.loads(datavalue)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(d1).count(query)
    elif op=='d':
        datavalue = dbconstants.MongoAPI(d1).delete(query)
        return datavalue

#TIMING
def  timing(query,datadict,op,timing):
    d1 = {}
    d1['collection'] = timing
    d1['database'] = "templeapp"
    if op=='i':
        datavalue = dbconstants.MongoAPI(d1).write(datadict)
        return datavalue
    elif op=='u':
        datavalue = dbconstants.MongoAPI(d1).update(query)
        return json.loads(datavalue)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(d1).read(query)
        return json.loads(datavalue)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(d1).readOne(query)
        return json.loads(datavalue)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(d1).count(query)
    elif op=='d':
        datavalue = dbconstants.MongoAPI(d1).delete(query)
        return datavalue


#TIMING
def  prasadham(query,datadict,op,prasadham):
    d1 = {}
    d1['collection'] = prasadham
    d1['database'] = "templeapp"
    if op=='i':
        datavalue = dbconstants.MongoAPI(d1).write(datadict)
        return datavalue
    elif op=='u':
        datavalue = dbconstants.MongoAPI(d1).update(query)
        return json.loads(datavalue)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(d1).read(query)
        return json.loads(datavalue)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(d1).readOne(query)
        return json.loads(datavalue)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(d1).count(query)
    elif op=='d':
        datavalue = dbconstants.MongoAPI(d1).delete(query)
        return datavalue


#HISTORY OF PRASADAM BOOKING
def  history(query,datadict,op,history):
    d1 = {}
    d1['collection'] = history
    d1['database'] = "templeapp"
    if op=='i':
        datavalue = dbconstants.MongoAPI(d1).write(datadict)
        return datavalue
    elif op=='u':
        datavalue = dbconstants.MongoAPI(d1).update(query)
        return json.loads(datavalue)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(d1).read(query)
        return json.loads(datavalue)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(d1).readOne(query)
        return json.loads(datavalue)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(d1).count(query)
    elif op=='d':
        datavalue = dbconstants.MongoAPI(d1).delete(query)
        return datavalue


#ATTRACTION NEARBY
def  attraction(query,datadict,op,attraction):
    d1 = {}
    d1['collection'] = attraction
    d1['database'] = "templeapp"
    if op=='i':
        datavalue = dbconstants.MongoAPI(d1).write(datadict)
        return datavalue
    elif op=='u':
        datavalue = dbconstants.MongoAPI(d1).update(query)
        return json.loads(datavalue)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(d1).read(query)
        return json.loads(datavalue)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(d1).readOne(query)
        return json.loads(datavalue)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(d1).count(query)
    elif op=='d':
        datavalue = dbconstants.MongoAPI(d1).delete(query)
        return datavalue


#STAY NEARBY
def  stay(query,datadict,op,stay):
    d1 = {}
    d1['collection'] = stay
    d1['database'] = "templeapp"
    if op=='i':
        datavalue = dbconstants.MongoAPI(d1).write(datadict)
        return datavalue
    elif op=='u':
        datavalue = dbconstants.MongoAPI(d1).update(query)
        return json.loads(datavalue)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(d1).read(query)
        return json.loads(datavalue)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(d1).readOne(query)
        return json.loads(datavalue)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(d1).count(query)
    elif op=='d':
        datavalue = dbconstants.MongoAPI(d1).delete(query)
        return datavalue


#LIST LORDS
def  lords(query,datadict,op,lords):
    d1 = {}
    d1['collection'] = lords
    d1['database'] = "templeapp"
    if op=='i':
        datavalue = dbconstants.MongoAPI(d1).write(datadict)
        return datavalue
    elif op=='u':
        datavalue = dbconstants.MongoAPI(d1).update(query)
        return json.loads(datavalue)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(d1).read(query)
        return json.loads(datavalue)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(d1).readOne(query)
        return json.loads(datavalue)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(d1).count(query)
    elif op=='d':
        datavalue = dbconstants.MongoAPI(d1).delete(query)
        return datavalue

#VIEW TRANSPORT
def  transports(query,datadict,op,transports):
    d1 = {}
    d1['collection'] = transports
    d1['database'] = "templeapp"
    if op=='i':
        datavalue = dbconstants.MongoAPI(d1).write(datadict)
        return datavalue
    elif op=='u':
        datavalue = dbconstants.MongoAPI(d1).update(query)
        return json.loads(datavalue)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(d1).read(query)
        return json.loads(datavalue)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(d1).readOne(query)
        return json.loads(datavalue)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(d1).count(query)
    elif op=='d':
        datavalue = dbconstants.MongoAPI(d1).delete(query)
        return datavalue