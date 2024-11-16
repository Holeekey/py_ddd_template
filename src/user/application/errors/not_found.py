from common.application.error.application_error import ApplicationError
from user.application.errors.codes.user_error_codes import UserErrorCodes

user_not_found_error = ApplicationError(
    code=UserErrorCodes.NOT_FOUND.value,
    message="User not found"
)