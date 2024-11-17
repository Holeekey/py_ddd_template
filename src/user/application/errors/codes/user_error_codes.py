from enum import Enum


class UserErrorCodes(Enum):
    USERNAME_ALREADY_EXISTS = "US-E-001"
    EMAIL_ALREADY_EXISTS = "US-E-002"
    NOT_FOUND = "US-E-NF"
