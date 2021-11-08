import flask

import json
from maass import app
from flask import request,redirect
from flask import Response
import sys
import logging
from maass.constants.presets.schemas import users
from maass.constants.presets.schemas import merchants
from maass.constants.presets.schemas import loandetail
from maass.constants.constfns import CommonResponse
from maass.cruds.validations import validateJSON
from maass.cruds.checkuser import login
from maass.cruds.hashgen import hashifyrequest, hashifyresponse
from maass.cruds.checksumgen import createchecksumfrmdata
from maass.cruds.logger import loggersystem
from maass.cruds.panapi import pancheckApi

from maass.cruds.ruleEngine import rule_engine

from maass.cruds.equifax_impl import EquifaxPCRLTApi
# from flask_cors import CORS


@app.route('/',methods = ['get'])
def test():
    return "Maass Core V1 Running on 8003"


@app.route('/validatereq', methods=['POST'])
def validateReq():
   
    jsonData = request.json
    # jsonData = request.get_json()
    print("asdfgh")

    if(jsonData['req_type'] == "LOGIN"):
        valresp = validateJSON(jsonData,users.userSchema )
        
    elif(jsonData['req_type'] == "LOGOUT"):
        valresp = validateJSON(jsonData, users.userSchema)

    elif(jsonData['req_type'] == "DROPDOWN"):
        valresp = validateJSON(jsonData, users.userSchema)

    elif(jsonData['req_type'] == "GETMERCHANTS"):
        valresp = validateJSON(jsonData, merchants.merchSchema)
    elif(jsonData['req_type'] == "LOANDETAILS"):
        valresp = validateJSON(jsonData, loandetail.loanschema)
    else:
        valresp = CommonResponse(errorResponse=True)
    return valresp


@app.route('/checkuserLogin', methods=['POST'])
def checkuserLogin(request):
    return login(request)

@app.route('/hashrequest', methods=['POST'])
def hashrequest():
    data = request.get_json()
    return hashifyrequest(data)

@app.route('/hashresponse', methods=['POST'])
def hashresponse(request):
    return hashifyresponse(request)

@app.route('/createchecksum', methods=['POST'])
def createchecksum(request):
    return createchecksumfrmdata(request)

@app.route('/logrequest', methods=['POST'])
def logrequest():
    req = json.loads(request.data.decode('utf-8').replace("'",'"'))
    logdata = req['datalog']
       
    
    return loggersystem(req['level'], req['collection'], logdata, req['logtype'], req['reqtype'], req['timestamp'])


@app.route('/pancheck', methods = ['POST'])
def pancheck():
    return pancheckApi(request)


# CIR 360 REQUEST API

@app.route('/cirRequest',methods = ['POST'])
def cir360Request():
    apiObj = EquifaxPCRLTApi()
    return apiObj.cir360ReportApi(request)

# rule engine
@app.route('/rule_engine', methods = ['POST'])
def rule_engine_service():
    return rule_engine(request) 