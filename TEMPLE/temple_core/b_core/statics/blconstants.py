from collections import UserString
from flask.globals import request
from pymongo.message import query
from b_core.maass import maasslogger
import json
from b_core.statics import staticfunctions,staticconstants,dbconstants
from b_core.platformlayers import standardresponses
import re
import traceback, sys
# from temple.temple_core import b_core
from b_core.statics import dbmodules
from datetime import datetime



# LOGIN USER
def checkuserfrmdb(request):
    try:
    #     print("        REQUEST IVIDE ETHI    ",request)
    #     #Perform username and password validation with database if hashes and checksum are valid
    #     dbQuery = {"username":request['datafrm']['username'],"password":request['datafrm']['password']}
    #     print("           ividethi           ",dbQuery)
    #     request['database'] = "templeapp"
    #     request['collection'] = "login"
    #     usrSelect = dbconstants.MongoAPI(request).readOne(dbQuery)
    #     print("     ividethi 2   ",usrSelect)
    #     print("     ividethi 2   ",type(usrSelect))
    #     print("request********",request)
    #     if (request['datafrm']['username'] == usrSelect['username']) & (request['datafrm']['password'] == usrSelect['password']):
    #         print(">>>>>>>>>>>>>>>>.")
    #         request2 = {}
    #         dbQuery2 = {"role_id":int(usrSelect['userRole'])}
    #         request2['database'] = "templeapp"
    #         request2['collection'] = "roles"
    #         successurl = dbconstants.MongoAPI(request2).readOne(dbQuery2)
    #         # print("@!@!@!", successurl)
    #         # print(usrSelect['username'])
    #         # print(usrSelect['userpic'])
    #         # print(usrSelect['userRole'])
    #         # print(usrSelect['userstatus'])
    #         datadict = {"username":usrSelect['username'],
    #                     "user_prof_pic":usrSelect['userpic'],
    #                     "user_role":usrSelect['userRole'],
    #                     "success_url":successurl['success_url'],
    #                     "user_status":usrSelect['userstatus'],
    #                     "templeid":usrSelect['templeid']
    #                     }


    #         respdict = {}
    #         respdict['respfrmdb']=datadict
    #         respdict['result'] = "Success"
           
            
    #         print("DTA DICT",datadict)

    #         return respdict
    #     else:
    #         return staticconstants.INVALID_USER_PASS
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "login":"userlogin",
            "logintype":"user1"
        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        # for frame in traceback.extract_tb(sys.exc_info()[2]):
        #     fname,lineno,fn,text = frame
        #     print( "Error in %s on line %d", fname, lineno)
        return str(e)



# LOGIN OTPVERIFICATION
def processOtpVerificationtapi(request):
    try:
    #     print("        REQUEST IVIDE ETHI    ",request)
    #     #Perform username and password validation with database if hashes and checksum are valid
    #     dbQuery = {"username":request['datafrm']['username'],"password":request['datafrm']['password']}
    #     print("           ividethi           ",dbQuery)
    #     request['database'] = "templeapp"
    #     request['collection'] = "login"
    #     usrSelect = dbconstants.MongoAPI(request).readOne(dbQuery)
    #     print("     ividethi 2   ",usrSelect)
    #     print("     ividethi 2   ",type(usrSelect))
    #     print("request********",request)
    #     if (request['datafrm']['username'] == usrSelect['username']) & (request['datafrm']['password'] == usrSelect['password']):
    #         print(">>>>>>>>>>>>>>>>.")
    #         request2 = {}
    #         dbQuery2 = {"role_id":int(usrSelect['userRole'])}
    #         request2['database'] = "templeapp"
    #         request2['collection'] = "roles"
    #         successurl = dbconstants.MongoAPI(request2).readOne(dbQuery2)
    #         # print("@!@!@!", successurl)
    #         # print(usrSelect['username'])
    #         # print(usrSelect['userpic'])
    #         # print(usrSelect['userRole'])
    #         # print(usrSelect['userstatus'])
    #         datadict = {"username":usrSelect['username'],
    #                     "user_prof_pic":usrSelect['userpic'],
    #                     "user_role":usrSelect['userRole'],
    #                     "success_url":successurl['success_url'],
    #                     "user_status":usrSelect['userstatus'],
    #                     "templeid":usrSelect['templeid']
    #                     }


    #         respdict = {}
    #         respdict['respfrmdb']=datadict
    #         respdict['result'] = "Success"
           
            
    #         print("DTA DICT",datadict)

    #         return respdict
    #     else:
    #         return staticconstants.INVALID_USER_PASS
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "otp":"otpsend",
            "number":"1234"
        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        # for frame in traceback.extract_tb(sys.exc_info()[2]):
        #     fname,lineno,fn,text = frame
        #     print( "Error in %s on line %d", fname, lineno)
        return str(e)

        
#USER HOME
def processHomeapi(request):
    try:
    #     print("        REQUEST IVIDE ETHI    ",request)
    #     #Perform username and password validation with database if hashes and checksum are valid
    #     dbQuery = {"username":request['datafrm']['username'],"password":request['datafrm']['password']}
    #     print("           ividethi           ",dbQuery)
    #     request['database'] = "templeapp"
    #     request['collection'] = "home"
    #     usrSelect = dbconstants.MongoAPI(request).readOne(dbQuery)
    #     print("     ividethi 2   ",usrSelect)
    #     print("     ividethi 2   ",type(usrSelect))
    #     print("request********",request)
    #     if (request['datafrm']['username'] == usrSelect['username']) & (request['datafrm']['password'] == usrSelect['password']):
    #         print(">>>>>>>>>>>>>>>>.")
    #         request2 = {}
    #         dbQuery2 = {"role_id":int(usrSelect['userRole'])}
    #         request2['database'] = "templeapp"
    #         request2['collection'] = "roles"
    #         successurl = dbconstants.MongoAPI(request2).readOne(dbQuery2)
    #         # print("@!@!@!", successurl)
    #         # print(usrSelect['username'])
    #         # print(usrSelect['userpic'])
    #         # print(usrSelect['userRole'])
    #         # print(usrSelect['userstatus'])
    #         datadict = {"username":usrSelect['username'],
    #                     "user_prof_pic":usrSelect['userpic'],
    #                     "user_role":usrSelect['userRole'],
    #                     "success_url":successurl['success_url'],
    #                     "user_status":usrSelect['userstatus'],
    #                     "templeid":usrSelect['templeid']
    #                     }


    #         respdict = {}
    #         respdict['respfrmdb']=datadict
    #         respdict['result'] = "Success"
           
            
    #         print("DTA DICT",datadict)

    #         return respdict
    #     else:
    #         return staticconstants.INVALID_USER_PASS
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "OTP":"send",
            "number":"123456"
        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        # for frame in traceback.extract_tb(sys.exc_info()[2]):
        #     fname,lineno,fn,text = frame
        #     print( "Error in %s on line %d", fname, lineno)
        return str(e)

#LIST POOJA PRATHISHTA
def listPoojaPrathishtaapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='POOJAPRATHISHTA'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.pooja(dbQuery, "","l","pooja")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "pooja":"poojaname",
            "prathishta":"prathishtaname"
        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

#LIST POOJA ALL
def listPoojaAllapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='POOJAALL'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.pooja(dbQuery, "","l","pooja")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "pooja":"poojaname",
            "poojatype":"poojaall"
        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

#VIEW POOJA CART
def viewPoojaapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='POOJAALL'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.pooja(dbQuery, "","l","pooja")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "pooja":"poojaname",
            "poojatype":"poojaall"
        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)


# CREATE POOJA FORM
def createPoojaFormapi(request):
    try:

    # request['database'] = "templeapp"
    #     # request['collection'] = "pooja"
    #     modulename='CREATEPOOJAFORM'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.templeapp({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "createpooja":"poojaname",
            "poojatype":"pooja"
        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        # for frame in traceback.extract_tb(sys.exc_info()[2]):
        #     fname,lineno,fn,text = frame
        #     print( "Error in %s on line %d", fname, lineno)
        return str(e)

#LIST OFFERING PRATHISHTA
def listOfferingPrathsishtaapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='POOJAALL'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.prathishta(dbQuery, "","l","prathishta")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "prathishta":"name",
            "offering":"type"
        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

#LIST OFFERING
def listOfferingaapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='POOJAALL'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.offering(dbQuery, "","l","offering")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "offering":"name",
            "price":"50"
        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

#VIEW OFFERING CART
def viewOfferingapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='POOJAALL'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.offering(dbQuery, "","l","offering")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "offering":"offeringname",
            "offeringtype":"price"
        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

# CREATE POOJA FORM
def createOfferinFormgapi(request):
    try:

    # request['database'] = "templeapp"
    #     # request['collection'] = "offering"
    #     modulename='CREATEOFFERINGFORM'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.offering({},datadict,"c","offering")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.offering("",datadict,"i","offering")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "createoffering":"offeringname",
            "offeringtype":"offering1"
        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        # for frame in traceback.extract_tb(sys.exc_info()[2]):
        #     fname,lineno,fn,text = frame
        #     print( "Error in %s on line %d", fname, lineno)
        return str(e)


#VIEW CART
def viewCartapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='POOJAALL'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.cart(dbQuery, "","l","cart")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "cart":"cartname",
            "cartnumber":"5"
        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)


#LIST KANIKKA
def listKanikkaapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='POOJAALL'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.kanikka(dbQuery, "","l","kanikka")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "kanikka":"5",
            "total":"amount"        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)


# CREATE KANIKKA
def addKanikkaapi(request):
    try:

    # request['database'] = "templeapp"
    #     # request['collection'] = "kanikka"
    #     modulename='ADDKANIKKA'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.kanikka({},datadict,"c","kanikka")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.kanikka("",datadict,"i","kanikka")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "kanikka number":"8",
            "kanikka limit":"15000"
        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        # for frame in traceback.extract_tb(sys.exc_info()[2]):
        #     fname,lineno,fn,text = frame
        #     print( "Error in %s on line %d", fname, lineno)
        return str(e)

#VIEW TEMPLE TIMIMG
def viewTempleTimimgapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='VIEWTEMPLETIMIMG'
        # request['modulename'] = modulename
        # datavalue =dbmodules.timing(dbQuery, "","l","timing")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "TIMING":"time",
            "NAME":"annandhanam"        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

#VIEW PASADHAM
def viewPrasadhamapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='VIEWPRASADHAM'
        # request['modulename'] = modulename
        # datavalue =dbmodules.prasadham(dbQuery, "","l","prasadham")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "kanikka":"5",
            "total":"amount"        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)


#ADD PRASADHAM
def addPrasadhamapi(request):
    try:

    # request['database'] = "templeapp"
    #     # request['collection'] = "prasadham"
    #     modulename='ADDPRASADHAM'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.prasadham({},datadict,"c","prasadham")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.prasadham("",datadict,"i","prasadham")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "PRASADHAM TIME":"MORNING",
            "PRASADHAM RATE":"500"
        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        # for frame in traceback.extract_tb(sys.exc_info()[2]):
        #     fname,lineno,fn,text = frame
        #     print( "Error in %s on line %d", fname, lineno)


#VIEW HISTORY
def viewHistoryapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='VIEWHISTORY'
        # request['modulename'] = modulename
        # datavalue =dbmodules.history(dbQuery, "","l","history")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "pname":"annadanam",
            "time":"morning"
            }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)


#VIEW ATTRACTION NEAR
def viewAttractionapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='VIEWHISTORY'
        # request['modulename'] = modulename
        # datavalue =dbmodules.attraction(dbQuery, "","l","attraction")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "attraction name":"big shivalingam",
            "distance":"5km"
            }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)


#VIEW STAY NEARBY
def viewNearestStayapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='VIEWSTAY'
        # request['modulename'] = modulename
        # datavalue =dbmodules.stay(dbQuery, "","l","stay")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "attraction name":"big shivalingam",
            "distance":"5km"
            }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)


#LIST LORDS
def viewLordsapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='VIEWSTAY'
        # request['modulename'] = modulename
        # datavalue =dbmodules.lords(dbQuery, "","l","lords")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "Lord name":"lord name",
            "number of lords":"5k"
            }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

#VIEW AIR TRANSPORT
def viewAirTransportapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='VIEWSTAY'
        # request['modulename'] = modulename
        # datavalue =dbmodules.transports(dbQuery, "","l","transports")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
           "airport":"airport",
           "distance":"10km"
            }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)


#VIEW TRAIN TRANSPORT
def viewTrainTransportapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='VIEWSTAY'
        # request['modulename'] = modulename
        # datavalue =dbmodules.transports(dbQuery, "","l","transports")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
           "railwayt":"station name",
           "distance":"5km"
            }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)


#VIEW ROAD TRANSPORT
def viewRoadTransportapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='VIEWSTAY'
        # request['modulename'] = modulename
        # datavalue =dbmodules.transports(dbQuery, "","l","transports")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
           "road name":"nh 40",
           "distance":"10km"
            }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)


#VIEW CONTACT DETAILS
def viewContactapi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='VIEWSTAY'
        # request['modulename'] = modulename
        # datavalue =dbmodules.contact(dbQuery, "","l","contact")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
           "name":"temple",
           "contact":"9856324758"
            }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict       
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)