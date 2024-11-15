from common.application.error.application_error import ApplicationError
from user.application.errors.codes.user_error_codes import UserErrorCodes

email_already_exists_error = ApplicationError(
    code=UserErrorCodes.EMAIL_ALREADY_EXISTS.value,
    message="User email already used"
)