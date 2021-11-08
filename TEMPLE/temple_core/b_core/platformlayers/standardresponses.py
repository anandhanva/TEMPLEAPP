from b_core.statics.urlconstants import LOGIN
from b_core.statics import ipconstants


commonValues = {}


commonValues['HASH_MO'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.hashServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/hashrequest",
                            "reqtype" : "HASHREQ",
                            "methodtype" : "POST"
                        }
#LOGIN
commonValues['LOGIN'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/login",
                            "reqtype" : "LOGINREQ",
                            "methodtype" : "POST"
                        }

#otp Verification
commonValues['OTPVERIFICATION'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/otpverification",
                            "reqtype" : "OTPVERIFICATIONREQ",
                            "methodtype" : "POST"
                        }


#home
commonValues['HOME'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/home_be",
                            "reqtype" : "HOMEREQ",
                            "methodtype" : "POST"
                        }

#list pooja pradhishta
commonValues['LISTPOOJAPRADHISHTA'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_poojapradhishta",
                            "reqtype" : "LISTPOOJAPRADHISHTAREQ",
                            "methodtype" : "POST"
                        }

#list pooja all
commonValues['LISTPOOJAALL'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_poojaall",
                            "reqtype" : "LISTPOOJAALLREQ",
                            "methodtype" : "POST"
                        }

#view pooja cart
commonValues['VIEWPOOJA'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/view_pooja",
                            "reqtype" : "VIEWPOOJAREQ",
                            "methodtype" : "POST"
                        }

#create pooja form
commonValues['CREATEPOOJAFORM'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/addpooja_form",
                            "reqtype" : "VIEWPOOJAREQ",
                            "methodtype" : "POST"
                        }

#list offering prathishta
commonValues['LISTOFFERINGPRATHISHTA'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_offeringprathishta",
                            "reqtype" : "LISTOFFERINGPRATHISHTAREQ",
                            "methodtype" : "POST"
                        }

#list offering
commonValues['LISTOFFERING'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_offering",
                            "reqtype" : "LISTOFFERINGREQ",
                            "methodtype" : "POST"
                        }

#view offering cart
commonValues['VIEWOFFERING'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/view_offering",
                            "reqtype" : "VIEWOFFERINGREQ",
                            "methodtype" : "POST"
                        }

#create offering form
commonValues['CREATEOFFERINGFORM'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/add_offering",
                            "reqtype" : "CREATEOFFERINGFORMREQ",
                            "methodtype" : "POST"
                        }

#view cart
commonValues['VIEWCART'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/cart",
                            "reqtype" : "VIEWCARTREQ",
                            "methodtype" : "POST"
                        }

#LIST KANIKKA
commonValues['LISTKANIKKA'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_kanikka",
                            "reqtype" : "LISTKANIKKAREQ",
                            "methodtype" : "POST"
                        }

#ADD KANIKKA
commonValues['ADDKANIKKA'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/add_kanikka",
                            "reqtype" : "ADDKANIKKAREQ",
                            "methodtype" : "POST"
                        }

#VIEW TEMPLE TIMIMG
commonValues['VIEWTEMPLETIMING'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/temple_timing",
                            "reqtype" : "VIEWTEMPLETIMINGREQ",
                            "methodtype" : "POST"
                        }

#VIEW PRASADHAM
commonValues['VIEWPRASADHAM'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/view_presadam",
                            "reqtype" : "VIEWPRASADHAMREQ",
                            "methodtype" : "POST"
                        }

#ADD PRASADHAM
commonValues['ADDPRASADHAM'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/add_presadam",
                            "reqtype" : "ADDPRASADHAMREQ",
                            "methodtype" : "POST"
                        }


#VIEW HISTORY
commonValues['VIEWHISTORY'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/history",
                            "reqtype" : "VIEWHISTORYREQ",
                            "methodtype" : "POST"
                        }


#VIEW ATTRACTION NEAR
commonValues['VIEWATTRACTION'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/attract_nearby",
                            "reqtype" : "VIEWATTRACTIONREQ",
                            "methodtype" : "POST"
                        }


#VIEW STAY NEAR
commonValues['VIEWSTAY'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/near_stay",
                            "reqtype" : "VIEWSTAYREQ",
                            "methodtype" : "POST"
                        }

#LIST LORDS
commonValues['LISTLORDS'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_lords",
                            "reqtype" : "LISTLORDSREQ",
                            "methodtype" : "POST"
                        }

#VIEW AIR TRANSPORT
commonValues['VIEWAIRTRANSPORT'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/transp_air",
                            "reqtype" : "VIEWAIRTRANSPORTREQ",
                            "methodtype" : "POST"
                        }

#VIEW TRAIN TRANSPORT
commonValues['VIEWTRAINTRANSPORT'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/transp_train",
                            "reqtype" : "VIEWTRAINTRANSPORTREQ",
                            "methodtype" : "POST"
                        }

#VIEW ROAD TRANSPORT
commonValues['VIEWROADTRANSPORT'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/transp_road",
                            "reqtype" : "VIEWROADTRANSPORTREQ",
                            "methodtype" : "POST"
                        }

#VIEW AIR TRANSPORT
commonValues['VIEWAIRTRANSPORT'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/transp_air",
                            "reqtype" : "VIEWAIRTRANSPORTREQ",
                            "methodtype" : "POST"
                        }


#VIEW AIR TRANSPORT
commonValues['VIEWAIRTRANSPORT'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/transp_air",
                            "reqtype" : "VIEWAIRTRANSPORTREQ",
                            "methodtype" : "POST"
                        }
#VIEW CONTACT
commonValues['VIEWCONTACT'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/contactus_be",
                            "reqtype" : "VIEWCONTACTREQ",
                            "methodtype" : "POST"
                        }