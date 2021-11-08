
import requests
import sys
import json
import logging
from maass.constants.config import Config
from maass.constants.constfns import MyDict






class ServerSideImpl():

    def yesBankRequest(reqdata2,URL):

        ybReqJson = MyDict(reqdata2)

        logging.info("EQUIFAX PROVIDER :REQUEST:: " + str(ybReqJson)) 

        ybResponseJson = ServerSideImpl.postrequestManager(URL,ybReqJson)

        logging.info("EQUIFAX PROVIDER : RESPONSE:: " + str(ybResponseJson))

        return ybResponseJson


    def postrequestManager(endPoinUrl,ybReqJson):

        headers = Config.getHeader()

        payload = json.dumps(ybReqJson)

        logging.info("HEADER ::::::> "+str(headers))
        logging.info("END URL :::::>"+str(Config.getEquifaxUrl()+endPoinUrl))
        logging.info("DATA :::::>"+str(ybReqJson))

        

        # payload = json.loads(payload1)



        try:
            response = requests.request("POST", Config.getEquifaxUrl()+endPoinUrl, headers=headers, data=payload)


            # response = json.dumps(response)
            # print("type ",type(response))

            # if  'error' in response['CCRResponse']['CIRReportDataLst']:
            #     return ""

            return response.text

        except requests.exceptions.HTTPError as err:
            return str(err)
        except requests.Timeout as e:
            return "Request Timed Out"
        except requests.RequestException as e:
            return "Request Exception detected :"
        except requests.ConnectionError as e:
            return str(e)
        except requests.exceptions as err:
            return str(err)


