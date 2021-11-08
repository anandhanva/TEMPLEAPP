# Log the activity in Maass Logger Micro Service
from re import M
from b_core.statics import staticfunctions
import flask
from b_core.platformlayers import standardresponses
def maasslogger(data, msg, modulename, logtype):
    #Log the error and the request data parameters
    config = {}
    srvr = standardresponses.commonValues[modulename]
    print("MODULENAME",modulename)
    config[modulename] = {}
    config[modulename]['parameters'] = srvr
    reqdta = {}
    reqdta['data'] = data
    reqdta['msg'] = msg
    config[modulename]["requestdata"] = reqdta
    config[modulename]["loggr"] = logtype
    maasslog = staticfunctions.performRequest(config[modulename])
    return maasslog