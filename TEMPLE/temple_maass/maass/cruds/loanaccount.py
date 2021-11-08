from maass.constants.db import MongoAPI

def createloanaccount(data):
    # Create a new account in the respective table
    createdaccount = MongoAPI.write(data)
    if(createdaccount['Status'] == 'Successfully Inserted'):
        # import customer data
        custdatacond = data['cust_mobnum']
        custdata = ''
        custdata['loanaccnumber'] = ""
        custdata['Filter'] = custdatacond 
        updatecustomertable = MongoAPI.update(custdata)
        if(updatecustomertable['Status'] == 'Successfully Updated'):
            checkkycstatus = MongoAPI.readOne({"cust_mobnum" : custdatacond})
            if(checkkycstatus):
                if(checkkycstatus['kyc_status'] == 1 or checkkycstatus['kyc_status'] == 2):
                    s = ""
            # Check the KYC information
            # Generate sequential account number based on partner
            # Append all requisite data into array
    loanaccdets = ""
    return loanaccdets


