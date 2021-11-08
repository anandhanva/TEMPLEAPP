from maass.constants import endPoints


ENCRYPTION_KEY = "WHENTHESKIESAREBLUESEEYOUONCEAGA"
DB_NAME = "buildd"
COLLECTION_NAME = "apix"


EQUIFAX_BASE_URL_LOCAL = "http://http://127.0.0.1:8002/cardmanager/ewire/v1"
EQUIFAX_BASE_URL_UAT = "https://ists.equifax.co.in"
EQUIFAX_BASE_URL_PROD =  "https://uatsky.yesbank.in/app/uat/api-banking"


MONGODB_SERVER = "3.109.80.214"
MONGO_USER = "buildd"
MONGO_PASS = "sublimeAcc3ss"


# pls configure base url before production

EQUIFAX_BASE_URL = EQUIFAX_BASE_URL_UAT

loggrRespdatasuccess = {
                    "status":200,
                    "respType":"Success",
                    "response": "Successfully Logged"
}

loggrRespdatafail = {
                    "status":500,
                    "respType":"Failure",
                    "response": "Failure in  Logging"
}


panRequestServer = "in-api.advance.ai/in/openapi/verification/v2"
panRequestHeader = {'X-ADVAI-KEY':"489ca1aebfc8e6b7",'Content-Type':'application/json'}
panRequestReqType = "SSL"
panRequestMethod = "POST"
panRequestEndpoint = '/pan-status-check'

# rule engine
ruleengineRequestServer = "in-api.advance.ai/in/openapi/verification/v2"
ruleengineRequestHeader = {"Content-Type":"application/json"}
ruleengineRequestReqType = "SSL"
ruleengineRequestMethod = "POST"
ruleengineRequestEndpoint = '/user'


# equifax

# equifaxRequestServer = "in-api.advance.ai/in/openapi/equifax/v2"
# equifaxRequestHeader = {"Content-Type":"application/json"}
# equifaxRequestReqType = "SSL"
# equifaxnRequestMethod = "POST"
# equifaxRequestEndpoint = endPoints.CIR360


Pan_Table = 'pandata'

cir_table_name='cir_score_response'

# rule engine
merchant_table="merchants"
rule_table="rulesets"
customer_table="customers"

class Config:


    @staticmethod
    def getEquifaxUrl():
        equifaxUrl = EQUIFAX_BASE_URL
        return equifaxUrl
    

    @staticmethod
    def getHeader():

        # here we need to receive username and password for the setting Authorization header as encrypted
        # now hard-coded

        headers = {
        'Content-Type': 'application/json'
        }
        
        return headers