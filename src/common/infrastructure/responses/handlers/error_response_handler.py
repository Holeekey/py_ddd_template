from fastapi import HTTPException
from common.application.error.application_error import ApplicationError


def error_response_handler(error: ApplicationError) -> Exception:
    
    status_code: int

    if(error.code.endswith('NF')):
        status_code = 404
    elif(error.code.endswith('UN')):
        status_code = 403
    else:
        status_code = 400

    detail = {
        'code': error.code,
        'message': error.message,
        'info': error.info
    } if error.info else {
        'code': error.code,
        'message': error.message,
    }

    return HTTPException(status_code=status_code, detail=detail)