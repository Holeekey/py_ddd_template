from common.application.error.application_error import ApplicationError
from user.application.errors.codes.user_error_codes import UserErrorCodes

username_already_exists_error = ApplicationError(
    code=UserErrorCodes.USERNAME_ALREADY_EXISTS.value,
    message="Username already used"
)