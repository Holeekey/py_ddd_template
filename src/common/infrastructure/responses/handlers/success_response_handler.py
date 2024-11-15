from typing import TypeVar
from common.application.result.application_result import ResultInfo
from common.infrastructure.responses.info import ResponseInfo
from common.infrastructure.responses.response import Response

T = TypeVar("T")

def success_response_handler(t: T, info: ResultInfo)-> Response:
    response_info = ResponseInfo(code=info.code, message=info.message)
    return Response(info=response_info, response=t) 