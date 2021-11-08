import datetime
from flask import Flask
from flask import request,Response
import requests

import hashlib
import json
import logging
from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

BLOCK_SIZE = 16

# COMMON RESPONSE CLASS
class CommonResponse:
    ewire_reqid : str
    timestamp : datetime
    ewire_custid : str

    resp_code : str
    message : str
    resp_type : str
    resp_frm_yesb : dict
    resp_frm_ewire : dict

    def __init__(self, data):

        self.resp_code = data["req_code"]
        self.resp_type = data["req_type"]
        self.message = data["message"]
        
        try:
            if data["ewire_reqid"] is None or data["ewire_custid"] is None:
                 raise Exception("Attribute error,request param null")
                    
            self.ewire_reqid = data["ewire_reqid"]
            self.ewire_custid = data["ewire_custid"]
            self.resp_frm_bank = data["resp_frm_bank"]
            self.resp_frm_ewire = data["resp_frm_ewire"]
            self.resp_frm_cbs = data["resp_frm_cbs"]
            self.resp_frm_ext = data["resp_frm_ext"]
            self.resp_frm_maass = data["resp_frm_maass"]
            self.resp_frm_blockc = data["resp_frm_blockc"]
            self.resp_frm_mojaloop = data["resp_frm_mojaloop"]
            self.resp_frm_rulengn = data["resp_frm_rulengn"]
            self.timestamp = str(datetime.datetime.now())

        except ValueError :
            raise Exception("ValueError exception  while assigning timeStamp")
        except TypeError:
            raise Exception("TypeError exception while assigning timeStamp")
        except Exception as e:
            print(e)
            raise Exception("exception while assigning timeStamp")

def dpad(data):
    length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return (data + chr(length)*length).encode('utf8')

def dunpad(data):
    return data[:-ord(data[-1])]

class AESCipher:
    def __init__(self, key):
        self.key = md5(key.encode('utf8')).digest()

  

    def encrypt(self, data):
        IV = Random.new().read(BLOCK_SIZE)
        aes = AES.new(self.key, AES.MODE_CBC, IV)
        return b64encode(IV + aes.encrypt(dpad(data))).decode('utf-8')

    def decrypt(self, data):
        encrypted = b64decode(data)
        IV = encrypted[:BLOCK_SIZE]
        aes = AES.new(self.key, AES.MODE_CBC, IV)
        return dunpad(aes.decrypt(encrypted[BLOCK_SIZE:]))


def checkSum(value):

        hashvalue = hashlib.md5(value.encode('utf-8')).hexdigest()
        # hashValue = hashlib.sha512(value.encode('utf-8')).hexdigest().lower()
        return hashvalue


def performRequest(server, headerz, endpoint, reqdata, reqType, methodType):
   
    if(reqType == "SSL"):
        url = "https://" + server + endpoint

    else:
        url = "http://" + server + endpoint

    responseofreq = ""

    if(methodType == "POST"):
        
        print("DATA",str(reqdata))
        print("URL",str(url))
        print("HEADER",str(headerz))
        payload = json.dumps(reqdata)

        try:
            r = requests.post(url, data = payload, headers=headerz)
            
            if(r.status_code == 200):
                return r.text
            else:
                return {"Error":"Api Failed"}
            responseofreq = r
        except Exception as e:
            return  str(e)
    else:
        if(methodType == "GET"):
            r = requests.get(url, data=reqdata, headers=headerz)
            if(r.status_code == 200):
                return "Success response to be created"
            else:
                return "failure response to be created"
            responseofreq = r
    return responseofreq


# equifax service
class my_dictionary(dict):
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value


class MyDict(dict):
  def __str__(self):
    return json.dumps(self)


def classToJsonObj(obj):
    # apiRespStr = json.dumps(obj.__dict__)
    apiRespStr = json.dumps(obj.__dict__ ,
            sort_keys=True,
            indent=1,
            cls=DjangoJSONEncoder)
    return eval(apiRespStr)



def flatten_json(nested_json):
    """
        Flatten json object with nested keys into a single level.
        Args:
            nested_json: A nested json object.
        Returns:
            The flattened json object if successful, None otherwise.
    """
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out







# rules for rule engine
def ruleSetUp(ruledata,custdata):
    print("::::ruledata",ruledata)
    print("::::custdata",custdata)


    if ruledata['rule_id'] == "EWRULE01":

        if (ruledata['age_min']<= custdata['age'] <= ruledata['age_max']):
            if(ruledata['bureau_min'] <= custdata['bureau_score'] <= ruledata['bureau_max']):
                print("SUCCESS")
                resp = {
                    "status":"BNPL Approved",
                    "custname":custdata['cust_name']
                }
                return resp
            else:
                resp = {
                    "status":"BNPL Declined",
                    "custname":custdata['cust_name']
                }
                return resp

        else:
            return {"response":"cannot allocate for a person in this age group"}
