from maass.constants import config
import logging
from maass.constants.db import MongoAPI
import json

def loggersystem(level,tablename, logdata, logtype, reqtype, timestamp):

    print("loggggdata",logdata)

    logstatus = ""
    try:
        logdata['level'] = level
        logdata['logtype'] = logtype
        logdata['logdata'] = str(logdata)
        logdata['reqtype'] = reqtype
        logdata['timestamp'] = timestamp
        logdata['database'] = config.DB_NAME
        logdata['collection'] = tablename

        print("LOOOOOOGGGGGG",logdata)
        loggr = MongoAPI(logdata).write(logdata)
        
        if(loggr['Status'] == "Successfully Inserted"):
            return config.loggrRespdatasuccess
        else:
            return config.loggrRespdatafail

    except ValueError as e:
        logging.error(str(e))
        return config.loggrRespdatafail
    except Exception as e:
        logging.error(str(e))
        return config.loggrRespdatafail

