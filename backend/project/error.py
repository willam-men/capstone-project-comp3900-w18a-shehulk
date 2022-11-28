from json import dumps
from werkzeug.exceptions import HTTPException

class AccessError(HTTPException):
    code = 403
    description = 'No message specified'

class InputError(HTTPException):
    code = 400
    description = 'No message specified'

class NotFoundError(HTTPException):
    code = 404
    description = 'No message specified'
     
class InternalServerError(HTTPException):
    code = 500
    message = 'No message specified'

def default_handler(err):
    response = err.get_response()
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.description,
    })
    response.content_type = 'application/json'
    return response
