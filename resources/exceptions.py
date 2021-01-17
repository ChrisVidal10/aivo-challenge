class ValidationError(Exception):

    def __init__(self, parameter):
        exceptions["ValidationError"]["message"] = "Parametro '{a}' debe ser de tipo {b}".format(a=parameter[0], b=parameter[2].__name__)

exceptions = {
    "ValidationError": {
        "status": 400
    }
}
