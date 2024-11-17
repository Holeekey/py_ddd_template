from pydantic import BaseModel


class CreateUserDto(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
