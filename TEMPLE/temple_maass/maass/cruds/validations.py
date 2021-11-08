import json 
import jsonschema
from jsonschema import validate
# from maass.constants.presets.schemas import userSchema
from maass.constants.presets.schemas.users import userSchema

def validateJSON(jsonData, schemaname):
    try:
        validate(instance=jsonData, schema=schemaname)
    except jsonschema.exceptions.ValidationError as err:
        return {"response": "failure"}
    return {"response":"success"}
