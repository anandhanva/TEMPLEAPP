from b_core.statics import dbconstants
import traceback, sys
import json


# def getDietybyTempleid(req):
#     try:
#         req = json.loads(req)
#         dbQuery = {"diety_templeid":req['datafrm']['templeid']}
#         req['database'] = "templeapp"
#         req['collection'] = "diety"
#         datavalue = dbconstants.MongoAPI(req).read(dbQuery)
#         print("listed",datavalue)
#         return datavalue  
#     except ValueError as e:
#         print("EXCEPTION",str(e))
#         return str(e)
#     except Exception as e:
#         print("FAILED",str(e))


# def getPoojabyDietyid(req):
#     try:
#         dbQuery = {"pooja_templeid":req['datafrm']['diety_id']}
#         req['database'] = "templeapp"
#         req['collection'] = "pooja"
#         datavalue =dbconstants.MongoAPI(req).read(dbQuery)
#         print("listed",datavalue)
#     except ValueError as e:
#         print("EXCEPTION1")
#         return str(e)
#     except Exception as e:
#         print("FAILED",str(e))
#         return str(e)
#     return req

# def getKanikkabyDietyid(req):
#     try:
#         dbQuery = {"kanikka":req['datafrm']['diety_id']}
#         req['database'] = "templeapp"
#         req['collection'] = "kanikka"
#         datavalue = dbconstants.MongoAPI(req).read(dbQuery)
#         print("listed",datavalue)
#         return datavalue  
#     except ValueError as e:
#         print("EXCEPTION",str(e))
#         return str(e)
#     except Exception as e:
#         print("FAILED",str(e))
#     return req

# def getPrasadambyTempleid(req):
#     try:
#         dbQuery = {"prasadam_templeid":req['datafrm']['templeid']}
#         req['database'] = "templeapp"
#         req['collection'] = "prasadam"
#         datavalue =dbconstants.MongoAPI(req).read(dbQuery)
#         print("listed",datavalue)
#     except ValueError as e:
#         print("EXCEPTION1")
#         return str(e)
#     except Exception as e:
#         print("FAILED",str(e))
#         return str(e)
#     return req

# def getPackageSizebyPrasadam(req):
    
#     try:
#         dbQuery = {"package_size":req['datafrm']['prasadam_name']}
#         req['database'] = "templeapp"
#         req['collection'] = "prasadam"
#         datavalue = dbconstants.MongoAPI(req).read(dbQuery)
#         print("listed",datavalue)
#         return datavalue  
#     except ValueError as e:
#         print("EXCEPTION",str(e))
#         return str(e)
#     except Exception as e:
#         print("FAILED",str(e))
#     return req


# def getOfferingbyTempleid(req):
#     try:
#         dbQuery = {"offering_templeid":req['datafrm']['templeid']}
#         req['database'] = "templeapp"
#         req['collection'] = "offering"
#         datavalue =dbconstants.MongoAPI(req).read(dbQuery)
#         print("listed",datavalue)
#     except ValueError as e:
#         print("EXCEPTION1")
#         return str(e)
#     except Exception as e:
#         print("FAILED",str(e))
#         return str(e)
#     return req

# def getOfferingbyDietyid(req):
#     try:
#         dbQuery = {"offering_templeid":req['datafrm']['diety_id']}
#         req['database'] = "templeapp"
#         req['collection'] = "offering"
#         datavalue = dbconstants.MongoAPI(req).read(dbQuery)
#         print("listed",datavalue)
#         return datavalue  
#     except ValueError as e:
#         print("EXCEPTION")
#         return str(e)
#     except Exception as e:
#         print("FAILED",str(e))
#     return req
    
# def getDatabyAcnumid(req):
#     try:
#         dbQuery = {"acnum_templeid":req['datafrm']['ac_id']}
#         req['database'] = "templeapp"
#         req['collection'] = "account"
#         datavalue = dbconstants.MongoAPI(req).read(dbQuery)
#         print("listed",datavalue)
#         return datavalue  
#     except ValueError as e:
#         print("EXCEPTION")
#         return str(e)
#     except Exception as e:
#         print("FAILED",str(e))
#     return req

