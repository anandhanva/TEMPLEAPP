import json
from flask.globals import request
from b_core.platformlayers import constantslayer,constant_dropdownsui,qrmanage
from b_core.platformlayers import constantslayer,constant_dropdownsui
from b_core.responsemaster import responses
from b_core.maass.maasslogger import maasslogger
from b_core.statics import staticfunctions,blconstants
import traceback, sys


# USER LOGIN
def processLoginRequest(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.checkuserfrmdb(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")


# USER OTPVERIFICATION
def processOtpVerificationt(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants. processOtpVerificationtapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")


# USER HOME
def processhomeapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.processHomeapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")


# list pooja predhishta
def listpoojaprathishtaapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.listPoojaPrathishtaapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

# list pooja all
def listpoojaallapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.listPoojaAllapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

#view pooja cart
def viewpoojaapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.viewPoojaapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

#create pooja cart
def createpoojaformapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createPoojaFormapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")


#list offering prathishta
def listofferingprathsishtaapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.listOfferingPrathsishtaapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

#list offering
def listofferingapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.listOfferingaapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

#view offering cart
def viewofferingapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.viewOfferingapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")


#create offering form
def createofferingformapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createOfferinFormgapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

#VIEW CART
def viewcartapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.viewCartapiapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")


#LIST KANIKKA
def listkanikkaapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.listKanikkaapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")


#ADD KANIKKA
def addkanikkaapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.addKanikkaapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

#VIEW TEMPLE TIMIMG
def viewtempletimimgapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.viewTempleTimimgapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

#VIEW PRASADHAM
def viewprasadhamapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.viewPrasadhamapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("PRASADHAM","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("PRASADHAM","Hash Mismatch, Incorrect Request")

#ADD PRASADHAM
def addprasadhamapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.addPrasadhamapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("PRASADHAM","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("PRASADHAM","Hash Mismatch, Incorrect Request")

#VIEW HISTORY
def viewhistoryapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.viewHistoryapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("PRASADHAM","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("PRASADHAM","Hash Mismatch, Incorrect Request")


#VIEW ATTRACTION NEAR
def viewattractionapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.viewAttractionapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("PRASADHAM","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("PRASADHAM","Hash Mismatch, Incorrect Request")


#VIEW STAY NEAR BY
def viewneareststayapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.viewNearestStayapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("PRASADHAM","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("PRASADHAM","Hash Mismatch, Incorrect Request")


# LIST LORDS
def viewlordsapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.viewLordsapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("PRASADHAM","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("PRASADHAM","Hash Mismatch, Incorrect Request")

#VIEW AIR TRANSPORT
def viewairtransportapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.viewAirTransportapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
         maasslogger(request, "Wrong Credentials")
         return responses.standardErrorResponseToBE("PRASADHAM","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("PRASADHAM","Hash Mismatch, Incorrect Request")


#VIEW TRAIN TRANSPORT
def viewtraintransportapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.viewTrainTransportapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
         maasslogger(request, "Wrong Credentials")
         return responses.standardErrorResponseToBE("PRASADHAM","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("PRASADHAM","Hash Mismatch, Incorrect Request")


#VIEW ROAD TRANSPORT
def viewroadtransportapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.viewRoadTransportapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
         maasslogger(request, "Wrong Credentials")
         return responses.standardErrorResponseToBE("PRASADHAM","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("PRASADHAM","Hash Mismatch, Incorrect Request")

#VIEW CONTACT DETAILS
def viewcontactapi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.viewContactapi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
         maasslogger(request, "Wrong Credentials")
         return responses.standardErrorResponseToBE("PRASADHAM","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("PRASADHAM","Hash Mismatch, Incorrect Request")