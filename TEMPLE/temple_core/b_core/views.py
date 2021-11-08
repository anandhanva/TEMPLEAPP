from flask.globals import request, session
from flask.wrappers import Request
from flask import Response
import requests
from b_core import app
import json
from b_core.statics import urlconstants,staticfunctions
from b_core.platformlayers import bllayer, constantslayer,qrmanage
from b_core.responsemaster import responses
# from temple.temple_core.b_core.statics.staticfunctions import coretobe_response
from flask.json import jsonify

baseUrl="/android"

@app.route('/', methods=['POST','GET'])
def base():
    return responses.upGetResponse()

#USER APIS

#USER LOGIN
@app.route(urlconstants.ENDPOINT+'/login', methods = ['POST'])
def login():
    
    return bllayer.processLoginRequest(request.json)

#USER OTPVERIFICATION
@app.route(urlconstants.ENDPOINT+'/otpverification', methods = ['POST'])
def otpVerification():
    
    return bllayer.processOtpVerificationt(request.json)

#USER HOME
@app.route(urlconstants.ENDPOINT+'/home_be', methods = ['POST'])
def otpverification():
    
    return bllayer.processhomeapi(request.json)

#LIST POOJA PRADHISHTA
@app.route(urlconstants.ENDPOINT+'/list_poojapradhishta', methods = ['POST'])
def listpoojaprathishta():
    
    return bllayer.processpoojapradhishtaapi(request.json)

#LIST POOJA ALL
@app.route(urlconstants.ENDPOINT+'/list_poojaall', methods = ['POST'])
def listpoojaall():
    
    return bllayer.listpoojallapi(request.json)

#VIEW CART POOJA
@app.route(urlconstants.ENDPOINT+'/selected_pooja', methods = ['POST'])
def viewpooja():
    
    return bllayer.viewpoojaapi(request.json)

#CREATE POOJA FORM
@app.route(urlconstants.ENDPOINT+'/addpooja_form', methods = ['POST'])
def createpoojaform():
    
    return bllayer.createpoojaformapi(request.json)

#LIST OFFERING PRATHISHTA
@app.route(urlconstants.ENDPOINT+'/list_offeringprathishta', methods = ['POST'])
def listofferingprathsishta():
    
    return bllayer.listofferingprathsishtaapi(request.json)

#LIST OFFERING
@app.route(urlconstants.ENDPOINT+'/list_offering', methods = ['POST'])
def listoffering():
    
    return bllayer.listofferingapi(request.json)

#VIEW CART OFFERING
@app.route(urlconstants.ENDPOINT+'/selected_offering', methods = ['POST'])
def viewoffering():
    
    return bllayer.viewofferingapi(request.json)

#CREATE OFFERING FORM
@app.route(urlconstants.ENDPOINT+'/add_offering', methods = ['POST'])
def createofferingform():
    
    return bllayer.createofferingformapi(request.json)

#VIEW CART
@app.route(urlconstants.ENDPOINT+'/cart', methods = ['POST'])
def viewcart():
    
    return bllayer.viewcartapi(request.json)

#LIST KANIKKA
@app.route(urlconstants.ENDPOINT+'/list_kanikka', methods = ['POST'])
def listkanikka():
    
    return bllayer.listkanikkaapi(request.json)

#ADD KANIKKA
@app.route(urlconstants.ENDPOINT+'/add_kanikka', methods = ['POST'])
def addkanikka():
    
    return bllayer.addkanikkaapi(request.json)

#VIEW TEMPLE TIMIMG
@app.route(urlconstants.ENDPOINT+'/temple_timing', methods = ['POST'])
def viewtempletimimg():
    
    return bllayer.viewtempletimimgapi(request.json)

#VIEW PRASADHAM
@app.route(urlconstants.ENDPOINT+'/view_presadam', methods = ['POST'])
def viewprasadham():
    
    return bllayer.viewprasadhamapi(request.json)

#ADD PRASADHAM
@app.route(urlconstants.ENDPOINT+'/add_presadam', methods = ['POST'])
def addprasadham():
    
    return bllayer.addprasadhamapi(request.json)

#VIEW HISTORY
@app.route(urlconstants.ENDPOINT+'/history', methods = ['POST'])
def viewhistory():
    
    return bllayer.viewhistoryapi(request.json)

#ATTRACTION NEAR BY
@app.route(urlconstants.ENDPOINT+'/attract_nearby', methods = ['POST'])
def viewattraction():
    
    return bllayer.viewattractionapi(request.json)


#STAY NEAR BY
@app.route(urlconstants.ENDPOINT+'/near_stay', methods = ['POST'])
def viewneareststay():
    
    return bllayer.viewneareststayapi(request.json)

#VIEW LORDS
@app.route(urlconstants.ENDPOINT+'/list_lords', methods = ['POST'])
def viewlords():
    
    return bllayer.viewlordsapi(request.json)

#VIEW AIR TRANSPORT
@app.route(urlconstants.ENDPOINT+'/transp_air', methods = ['POST'])
def viewairtransport():
    
    return bllayer.viewairtransportapi(request.json)


#VIEW TRAIN TRANSPORT
@app.route(urlconstants.ENDPOINT+'/transp_train', methods = ['POST'])
def viewtraintransport():
    
    return bllayer.viewtraintransportapi(request.json)


#VIEW ROAD TRANSPORT
@app.route(urlconstants.ENDPOINT+'/transp_road', methods = ['POST'])
def viewroadtransport():
    
    return bllayer.viewaroadtransportapi(request.json)


#VIEW CONTACT DETAILS
@app.route(urlconstants.ENDPOINT+'/contactus_be', methods = ['POST'])
def viewcontact():
    
    return bllayer.viewcontactapi(request.json)