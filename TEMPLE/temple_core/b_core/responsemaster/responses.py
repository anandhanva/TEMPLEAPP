import flask
from flask import Response
import json


def upGetResponse():
    print("resppp")
    resp = Response(response=json.dumps({"Status":"UP"}),status=200,mimetype='application/json')

    print("resppp")

    return resp

def standardErrorResponseToBE(src,error):
    respdict = {}
    respdict['Source']=src
    respdict['ERROR']=str(error)
    resp = Response(response=json.dumps(respdict),status=200,mimetype='application/json')

    return resp

