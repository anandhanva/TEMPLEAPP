import json 
import re
from maass.constants import config
from maass.constants.constfns import checkSum


def createchecksumfrmdata(data):
    chksumstr = json.dumps(data)   # convert dict to string
    chksumstr = re.sub("{","|",chksumstr) # replace open brackets
    chksumstr = re.sub("}","|",chksumstr) # replace close brackets
    chksumstr = re.sub(":","|","",chksumstr) # replace semicolons
    checksumify = re.sub(",","||",chksumstr) # replace commas
    return checkSum(checksumify)