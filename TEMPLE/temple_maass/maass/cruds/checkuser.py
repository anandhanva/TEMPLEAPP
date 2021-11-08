import json
from maass.constants.constfns import AESCipher,checkSum
from maass.constants.presets.schemas import users
import logging
from maass.constants import config

def login(self,req):

    try:
        logging.info(" :: LOGIN API RECEIVED  FROM EXT API :: ")
        
        requestDataJson = json.loads(req.data.decode('utf-8').replace("'",'"'))

        for i in requestDataJson.keys:
            print(i)

        HashString = "|req_type:"+requestDataJson['req_type']+"|req_code:"+requestDataJson['req_code']+"|api_name:"+requestDataJson['apiname']+"|ewire_reqid:"+requestDataJson['ewire_reqid']+"|partner_reqid:"+requestDataJson['partner_reqid']+"|req_timestamp:"+requestDataJson['req_timestamp']+"|requestdata:||username:"+requestDataJson['requestdata']['username']+"||password:"+requestDataJson['requestdata']['password']+"||authtoken:"+requestDataJson['authtoken']+"|ewire_endpoint:"+requestDataJson['ewire_endpoint']+"|ewire_custid:"+requestDataJson['ewire_custid']+"|txntype:"+requestDataJson['txntype']+"|"
        print("THIS IS HASH STRING :::::::>",HashString)
        key = config.ENCRYPTION_KEY

        hashalgo = AESCipher(key).encrypt(HashString)

        print(" :::::::::::> ",hashalgo)
        givenHash = requestDataJson['hashstr']
        print("requesthash",givenHash)
        decodeHash1 = AESCipher(config.ENCRYPTION_KEY).decrypt(givenHash)
        decodeHash2 =AESCipher(config.ENCRYPTION_KEY).decrypt(hashalgo)
        print("DECODEHASH1",decodeHash1)
        print("DECODEHASH2",decodeHash2)
        if decodeHash1 == decodeHash2:
            logging.info("HASHH PASSED")             

            checksum = checkSum(requestDataJson['hashstr'])
            print("hEYYOCHEKSUM::",checksum)

            checkit1 = requestDataJson['checksum']            

            if checkit1 == checksum:
                logging.info("CHECKSUM PASSED")
                return users.checkUserRespdatasuccess
            else:
                logging.info("CHECKSUM FAILED")

                return users.checkUserRespdatafail

        else:

            logging.info("HASH FAILED")
            hashss = users.checkUserRespdatafail
            hashss['Error'] = "HASH FAILED"
            return hashss

    except ValueError as e:
        return str(e)
    except Exception as e:
        return str(e)