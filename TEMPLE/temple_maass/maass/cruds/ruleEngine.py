from maass import app
import json
import logging
from maass.constants.constfns import performRequest,ruleSetUp
from maass.constants import config
from maass.constants.db import MongoAPI


def rule_engine(req):

    logging.info(" :: RULE ENGINE :: ")

    requestDataJson = json.loads(req.data.decode('utf-8'))
    merch_id = requestDataJson['builddmerchid']
    

    try:
        # merchant data from table "merchants" using merchant id
        getdata={
            "builddmerchid":merch_id
        }
        data={}
        data['collection'] = config.merchant_table
        data['database'] = config.DB_NAME
        merchdata = MongoAPI(data).readOne(getdata)
        del merchdata['_id']
        print("MERCHANT DATA",merchdata)

        if merchdata == "NULL":
            return {"response":"merchant not found"}

      

    except Exception as e:
        return str(e)
    except ValueError as e:
        return str(e)
    
        
    rule_id = merchdata['rule_id']
    try:
        # rule id  from table "merchants"
        getruledata={
            "rule_id":rule_id
        }
        data={}
        data['collection'] = config.rule_table
        data['database'] = config.DB_NAME
        ruledata = MongoAPI(data).readOne(getruledata)
        del ruledata['_id']
        print("RULE DATA",ruledata)

        if ruledata == "NULL":
            return {"response":"Error while fetching data"}
    
    except Exception as e:
        return str(e)
    except ValueError as e:
        return str(e)

    # min_age=ruledata['min_age']
    # max_age=ruledata['max_age']
    # bureau_min=ruledata['bureau_min']
    # bureau_max=ruledata['bureau_max']


# customers details using customer "phone number" from table "customers"


    logging.info(" :: CUSTOMER DETAILS :: ")

    
    cust_phn= requestDataJson['Customer']['phone']

       
    try:
        # customer data  from table "customers"
        getcustdata={
            "cust_phone":cust_phn
        }
        data={}
        data['collection'] = config.customer_table
        data['database'] = config.DB_NAME
        custdata = MongoAPI(data).readOne(getcustdata)

        del custdata['_id']

        print("CUSTOMER DATA",custdata)

        if custdata == "NULL":
            return {"response":"customer not found"}

      
    except Exception as e:
        return str(e)
    except ValueError as e:
        return str(e)
            
    try:
        checkRule = ruleSetUp(ruledata,custdata)
        print("CHECK RIUE",checkRule)
        return checkRule
    except Exception as e:
        return str(e)
    except ValueError as e:
        return str(e)


        


        
        
        
        

          

            








       
    