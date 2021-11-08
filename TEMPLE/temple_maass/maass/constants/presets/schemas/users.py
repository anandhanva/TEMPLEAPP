userSchema = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'username': {'type':'string'},
                     'password': {'type':'string'}},
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hash': {'type':'string'},
    'checksum': {'type':'string'}}


checkUserRespdatasuccess = {
                    "status":200,
                    "respType":"Success",
                    "response": "Access Granted"
}


checkUserRespdatafail = {
                    "status":500,
                    "respType":"Failed",
                    "response": "Access Denied"
}