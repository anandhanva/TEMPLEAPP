import json 
import re
from maass.constants import config
from maass.constants.constfns import AESCipher,checkSum

from maass.constants.presets.schemas import users

# Perform process to hash request dictionary and seperate the same with pipe symbol
def hashifyrequest(request):
    print("request",request)
    hashstr = re.sub("{","||||",str(request)) # replace open brackets
    hashstr = re.sub("}","||||",hashstr) # replace close brackets
    hashstr = re.sub(":","|",hashstr) # replace semicolons
    hashstr = re.sub(" ","",hashstr) # replace spaces
    hashstr = re.sub("\"", '"', hashstr) # replace slash and quote with quote
    hashstr = hashstr.strip()
    hashifyrequestdata = re.sub(",","||",hashstr) # replace commas

    print("HASH STRING",hashifyrequestdata)

    print("REQUEST",request)

    
    #get Key
    key = config.ENCRYPTION_KEY

    #Perform hash computation
    hashifiedrequestdata = AESCipher(key).encrypt(request)

    hashresp = users.checkUserRespdatasuccess
    hashresp['hashstr'] = str(hashifiedrequestdata)
    hashresp['src'] = str(hashifyrequestdata)
    print("Hash Response", hashresp)
    return hashresp

# Perform process to hash response dictionary and seperate the same with pipe symbol
def hashifyresponse(response):
    hashstr1 = json.dumps(response)   # convert dict to string
    hashstr1 = re.sub("{","||||",hashstr1) # replace open brackets
    hashstr1 = re.sub("}","||||",hashstr1) # replace close brackets
    hashstr1 = re.sub(":","|","",hashstr1) # replace semicolons
    hashstr1 = re.sub(" ","",hashstr1) # replace spaces
    hashifyresponsedata = re.sub(",","||",hashstr1) # replace commas
    #get Key
    key = config.ENCRYPTION_KEY
    #Perform hash computation
    hashifiedresponsedata = AESCipher(key).encrypt(hashifyresponsedata)
    return hashifiedresponsedata