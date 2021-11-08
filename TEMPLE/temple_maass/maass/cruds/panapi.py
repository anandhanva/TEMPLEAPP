from maass import app
from maass.constants.constfns import performRequest
from maass.constants import config
from maass.constants.db import MongoAPI
import json


def pancheckApi(req):

    try:

        requestDataJson = json.loads(req.data.decode('utf-8'))
        pan = requestDataJson['IDValue']
        name = requestDataJson['FirstName']

        server = config.panRequestServer
        header = config.panRequestHeader
        endpoint = config.panRequestEndpoint
        reqdata ={"pan":pan,
                    "name":name}
        reqType = config.panRequestReqType
        methodType = config.panRequestMethod

        try:

            panResp = performRequest(server, header, endpoint, reqdata, reqType, methodType)
        except Exception as e:
            return str(e)
        except ValueError as e:
            return str(e)

        print("PAN RESPONSE",panResp)
        panResp = json.loads(panResp)
        storedata = {}
        storedata['code'] = panResp["code"]
        storedata['result'] = panResp["data"]
        storedata['message'] = panResp["message"]
        storedata['transactionId'] = panResp["transactionId"]
        storedata['pricingStrategy'] = panResp["pricingStrategy"]
        storedata['pan_resp'] = panResp
        
        try:
            storedata['collection'] = config.Pan_Table
            storedata['database'] = config.DB_NAME
            store = MongoAPI(storedata).write(storedata)

        except Exception as e:
            return str(e)
        except ValueError as e:
            return str(e)


        return panResp

    except Exception as e :
        return str(e)
    except ValueError as e:
        return str(e)
