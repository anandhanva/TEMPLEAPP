import flask 
from flask import Flask
from flask import request
import sys
import json
from pprint import pprint
from maass.constants.constfns import performRequest,flatten_json
from maass.constants import endPoints
import logging

from maass.serversideApi.serverSideImpl import ServerSideImpl
from flask import Response
# from maass.dbService.Db_service import DbServiceImpl
from maass.constants import config
from maass.constants.db import MongoAPI
# from maass.commonUtil.commonUtil import flatten_json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('EQUIFAX API :: ')

# Database = DbServiceImpl
# Database.initialize_maass()


class EquifaxPCRLTApi():
   
# CIR 360 Report

    def cir360ReportApi(self,req):
        try:
            

            logging.info(" :: CIR 360 REQUEST API RECEIVED  FROM EXT API :: ")
            # print("raw req", req.__dict__)
            
            # requestDataJson = req.form.get("api_name")
            requestDataJson = json.loads(req.data.decode('utf-8').replace("'",'"'))
            logging.info("REQUESTING DATA"+str(requestDataJson))
        
            number = requestDataJson['req_data']['Number']
            first_name = requestDataJson['req_data']['FirstName']
            IDValue = requestDataJson['req_data']['IDValue']

            if 'Score' in requestDataJson['req_data']:

                try:
                    # table_name = 'cir_score_response'
                    settings = {}

                    where_dict =  {
                            "Number":number,
                            "FirstName":first_name,
                            "IDValue":IDValue,
                            }
                    settings['collection']=config.cir_table_name
                    settings['database']=config.DB_NAME
                    print("SETTINGS",settings)
                    print("DICT",where_dict)
                    dbCheck = MongoAPI(settings).readOne(where_dict)
                    print("DB CHECK",dbCheck)


                    if dbCheck is None:
                        callCir = EquifaxPCRLTApi().callCir360(requestDataJson)
                        where_dict =  {
                            "Number":number,
                            "FirstName":first_name,
                            "IDValue":IDValue,
                            }
                        where_dict['collection']=config.cir_table_name
                        where_dict['database']=config.DB_NAME
                        dbCheck = MongoAPI(where_dict).readOne(where_dict)

                        # dbCheck = Database.getOneData(table_name, where_dict)
                        del dbCheck['_id']
                        dbCheck['cir360response'] = json.loads(dbCheck['cir360response'])

                        # dbCheck = json.loads(dbCheck)
                        flatit = flatten_json(dbCheck)
                        return flatit
                    elif 'cir360response' in dbCheck:
                        del dbCheck['_id']
                        logging.info("checkWorked")
                        # dbCheck['cir360response'] = json.loads(dbCheck['cir360response'])
                        flatit = flatten_json(dbCheck)

                        return flatit


                    else:
                        return "SOME PROB OCCURED"

                except Exception as e:
                    logging.info("exception:"+str(e))
                    return str(e)

                except ValueError as e:
                    logging.info("exception:"+str(e))

            else:

                try:
                    table_name = 'cir360response'
                    settings = {}
                    dbCheck = {}

                    where_dict =  {
                            "Number":number,
                            "FirstName":first_name,
                            "IDValue":IDValue,
                            }
                    settings['collection']=table_name
                    settings['database']=config.DB_NAME
                    print("SETINGS",settings)
                    print("where_dict",where_dict)
                    dbCheck = MongoAPI(settings).readOne(where_dict)
                    print("dcdddcd",dbCheck)

                    # dbCheck = Database.getOneData(table_name, where_dict)
                    del dbCheck['_id']


                    if 'cir360response' in dbCheck:
                        logging.info("checkWorked")
                        # dbCheck['cir360response'] = json.loads(dbCheck['cir360response'])
                        return flatten_json(dbCheck)
                        
                    else:
                        callCir = EquifaxPCRLTApi().callCir360(requestDataJson)
                        settings = {}
                        where_dict =  {
                            "Number":number,
                            "FirstName":first_name,
                            "IDValue":IDValue,
                            }

                        where_dict['collection']=config.cir_table_name
                        where_dict['database']=config.DB_NAME
                        dbCheck = MongoAPI(where_dict).readOne(where_dict)

                        # dbCheck = Database.getOneData(table_name, where_dict)
                        del dbCheck['_id']
                        dbCheck['cir360response'] = dbCheck['cir360response']

                        # dbCheck = json.loads(dbCheck)
                        return flatten_json(dbCheck)
                    

                
                except Exception as e:
                    logging.info("exception:"+str(e))
                    return str(e)

        
        except ValueError as e:
            logging.info("EQUIFAX EXCEPTION"+str(e))
            return Response(str(e))


        except Exception as e:
            logging.info(str(e))
            return Response(str(e))



    def callCir360(self,requestDataJson):
        
        try:
            number = requestDataJson['req_data']['Number']
            first_name = requestDataJson['req_data']['FirstName']
            IDValue = requestDataJson['req_data']['IDValue']
            
            URL = endPoints.CIR360


            table_name = 'cir360'
            dbCheck = {}
            settings = {}
            
            where_dict = {
                'RequestBody.InquiryPhones.Number':requestDataJson['req_data']['Number'],
                'RequestBody.FirstName':requestDataJson['req_data']['FirstName'],
                'RequestBody.IDDetails.IDValue':requestDataJson['req_data']['IDValue']
                }

            settings['collection']= table_name
            settings['database']=config.DB_NAME
            dbCheck = MongoAPI(settings).readOne(where_dict)
    
            # dbCheck = Database.getOneData(table_name, where_dict)
            del dbCheck['_id']


            if 'Score' in requestDataJson['req_data']:
            # if 'Score' in req.form.keys():

                Score = [
                {
                    "Type": "ERS",
                    "Version": "3.1"
                }
                ]
                logging.info("REQUEST FOR SCORE")
                dbCheck['RequestHeader']['UserId'] = "STS_CCOERS"
                dbCheck['Score'] = Score

                
            else:
                pass

                
            if dbCheck and len(dbCheck)>1:

                logging.info("EQUIFAX DATA"+str(dbCheck))
            else:
                logging.info("database check failed")
                

        except Exception as e:
            logging.info("exception:"+str(e))

            return str(e)
        logging.info("BEFORE SENDING"+str(dbCheck))
        eqResp = ServerSideImpl.postrequestManager(URL, dbCheck)
        eqResp = json.loads(eqResp)
        logging.info("REPONSE = "+str(eqResp))

        if 'Score' in requestDataJson['req_data']:
            try:
                table_name = 'cir_score_response'
                settings = {}
                where_dict = {
                    "Number":number,
                    "FirstName":first_name,
                    "IDValue":IDValue,
                    "cir360response":eqResp
                    }

                settings['collection']=config.cir_table_name
                settings['database']=config.DB_NAME
                dbCheck = MongoAPI(settings).write(where_dict)
    
                # dbCheck = Database.insertOneData(table_name, where_dict)
                
            except Exception as e:
                logging.info(str(e))
                return Response(str(e))
        else:

            try:
                table_name = 'cir360response'
                settings = {}
                where_dict = {
                    "Number":number,
                    "FirstName":first_name,
                    "IDValue":IDValue,
                    "cir360response":eqResp
                    }
                settings['collection']=config.cir_table_name
                settings['database']=config.DB_NAME
                dbCheck = MongoAPI(settings).write(where_dict)

                # dbCheck = Database.insertOneData(table_name, where_dict)
                
            except Exception as e:
                logging.info(str(e))
                return Response(str(e))
            
        return eqResp
        


# # INDIVIDUAL INPUT REQUEST

#     def individualInputRequestApi(self,req):

#         try:
#             URL = endPoints.CIR360
#             logging.info(" :: INDIVIDUAL INPUT REQUEST API RECEIVED  FROM EXT API :: ")

#             requestDataJson = json.loads(req.data.decode('utf-8').replace("'",'"'))
            

#             # # COMPRESS THE VARIABLE
#             # req_header_dict = requestDataJson['req_data']['RequestHeader']

#             # # PRODUCT CODE EXTRACTED INTO A LIST
#             # ProductCode = list()
#             # prodcodelist = requestDataJson['req_data']['RequestHeader']['ProductCode']
#             # for count in range(0,len(prodcodelist)):
#             #     ProductCode.append(prodcodelist[count])   
#             # print(ProductCode)

#             # # MAKE REQUEST HEADER
#             # reqHeader = commonUtil.my_dictionary()
#             # reqHeader.add("CustomerId",req_header_dict['CustomerId'])
#             # reqHeader.add("UserId",req_header_dict['UserId'])
#             # reqHeader.add("Password",req_header_dict['Password'])
#             # reqHeader.add("MemberNumber",req_header_dict['MemberNumber'])
#             # reqHeader.add("SecurityCode",req_header_dict['SecurityCode'])
#             # reqHeader.add("ProductCode",ProductCode)
#             # reqHeader.add("CustRefField",req_header_dict['CustRefField'])
#             # logging.info("REQ HEADER WILL BE :::" + str(reqHeader))


#             # adressType = list()
#             # InquiryAdress = list()


#             # InquiryAdressList = requestDataJson['req_data']['RequestBody']['InquiryAddresses']


#             # for count in range(0,len(InquiryAdressList)):
            
#             #     adressType.append(InquiryAdressList['AddressType'])
                
#             #     AdressData.add("seq", InquiryAdressList['seq'])
#             #     AdressData.add("AddressType", adressType)
#             #     AdressData.add("AddressLine1", InquiryAdressList['AddressLine1'])
#             #     AdressData.add("AddressLine2", InquiryAdressList['AddressLine2'])
#             #     AdressData.add("Locality", InquiryAdressList['Locality'])
#             #     AdressData.add("City", InquiryAdressList['City'])
#             #     AdressData.add("State", InquiryAdressList['State'])
#             #     AdressData.add("Postal", InquiryAdressList['Postal'])
#             #     InquiryAdress.append(InquiryAdressList[AdressData][count])
#             #     # InquiryAdress.append(prodcodelist[count]
#             # print("INQ",InquiryAdress)
            

#             # IDData = commonUtil.my_dictionary()

#             # # ########
#             # IDDetails = []
            
#             # for element in requestDataJson['req_data']['RequestBody']['IDDetails']:

#             #     IDData.add("seq",requestDataJson['req_data']['RequestBody']['IDDetails']['seq'])
#             #     IDData.add("IDType",requestDataJson['req_data']['RequestBody']['IDDetails']['IDType'])
#             #     IDData.add("IDValue",requestDataJson['req_data']['RequestBody']['IDDetails']['IDValue'])

#             #     IDDetails.append(IDData)


#             # CustomFieldData = commonUtil.my_dictionary()
#             # CustomFieldData.add("key",requestDataJson['req_data']['RequestBody']['CustomFields']['key'])
#             # CustomFieldData.add("value",requestDataJson['req_data']['RequestBody']['CustomFields']['value'])


#             # CustomFields = []
#             # CustomFields.append(CustomFieldData)

#             # reqBody = commonUtil.my_dictionary()
#             # reqBody.add("InquiryPurpose",requestDataJson['req_data']['RequestBody']['InquiryPurpose'])
#             # reqBody.add("TransactionAmount",requestDataJson['req_data']['RequestBody']['TransactionAmount'])
#             # reqBody.add("FirstName",requestDataJson['req_data']['RequestBody']['FirstName'])
#             # reqBody.add("MiddleName",requestDataJson['req_data']['RequestBody']['MiddleName'])
#             # reqBody.add("LastName",requestDataJson['req_data']['RequestBody']['LastName'])
#             # reqBody.add("InquiryAddresses",InquiryAdress)
#             # reqBody.add("IDDetails",IDDetails)
#             # reqBody.add("DOB",requestDataJson['req_data']['RequestBody']['DOB'])
#             # reqBody.add("CustomFields",CustomFields)
            

#             # ScoreData = commonUtil.my_dictionary()
#             # ScoreData.add("Type",requestDataJson['req_data']['Score']['Type'])
#             # ScoreData.add("Version",requestDataJson['req_data']['Score']['Version'])

#             # Score = []
#             # Score.append(ScoreData)

#             # reqData.add("RequestHeader",reqHeader)
#             # reqData.add("RequestBody",reqBody)
#             # reqData.add("Score",Score)


#             # print("passdata",reqData)
#             reqData = requestDataJson['req_data']
#             print("reqqq",reqData)

#             ybResp = ServerSideImpl.yesBankRequest(reqData,URL)
            
#             return ybResp
        
#         except ValueError as e:
#             logging.info(("EQUIFAX EXCEPTION"))
#             print(str(e))
#             return e


#         except Exception as e:
#             print(str(e))
#             return e

#     def flatCirApi(self,req):

#         try:
#             logging.info("FLATTENED CIR REQUEST TO DB")
#             requestDataJson = json.loads(req.data.decode('utf-8').replace("'",'"'))
#             logging.info("REQUESTING DATA"+str(requestDataJson))
#             Number = requestDataJson['req_data']['Number']
#             FirstName = requestDataJson['req_data']['FirstName']
#             if 'Score' in requestDataJson['req_data']:

#                 try:
#                     table_name = 'cir_score_response'
#                     respUpdate = {}
#                     where_dict = {
#                         "Number":Number,
#                         "FirstName":FirstName
#                         }
                    
#                     where_dict['collection']=config.cir_table_name
#                     where_dict['database']=config.DB_NAME
#                     dbCheck = MongoAPI(where_dict).readOne(where_dict)
                    
#                     # dbCheck = Database.getOneData(table_name, where_dict)
#                     del dbCheck['_id']
                    
#                 except Exception as e:
#                     logging.info(str(e))
#                     return Response(str(e))
#                 flatdata = dbCheck['cir360response']
#                 parseData = flatten_json(flatdata)
#                 # print("HETTTT",parseData['InquiryResponseHeader'])
#                 dbCheck['cir360response'] = parseData
#                 return dbCheck
                

#             else:
#                 print("HEYYY")
#                 try:
#                     table_name = 'cir360response'
#                     respUpdate = {}
#                     where_dict = {
#                         "Number":Number,
#                         "FirstName":FirstName
#                         }

#                     where_dict['collection']=config.cir_table_name
#                     where_dict['database']=config.DB_NAME
#                     dbCheck = MongoAPI(where_dict).readOne(where_dict)    
#                     # dbCheck = Database.getOneData(table_name, where_dict)
#                     del dbCheck['_id']
                    
#                 except Exception as e:
#                     logging.info(str(e))
#                     return Response(str(e))
#                 flatdata = dbCheck['cir360response']
#                 parseData = flatten_json(flatdata)
#                 # print("HETTTT",parseData['InquiryResponseHeader'])
#                 dbCheck['cir360response'] = parseData
#                 return dbCheck
#         except ValueError as e:
#             logging.info("EQUIFAX EXCEPTION")
#             print(str(e))
#             return e

#         except Exception as e:
#             logging.info("EQUIFAX EXCEPTION"+str(e))
#             return e
