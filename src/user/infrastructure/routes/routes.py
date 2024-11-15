from fastapi import APIRouter

from common.application.decorators.error_decorator import ErrorDecorator
from common.infrastructure.id_generator.random.random_id_generator import (
    RandomIdGenerator,
)
from common.infrastructure.id_generator.uuid.uuid_generator import UUIDGenerator
from common.infrastructure.responses.handlers.success_response_handler import success_response_handler
from common.infrastructure.responses.handlers.error_response_handler import error_response_handler
from user.application.commands.create.create_user_command import CreateUserCommand
from user.infrastructure.repositories.mock.user_repository import UserRepositoryMock
from user.infrastructure.routes.types.dto.create.create_user_dto import CreateUserDto


user_router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

userRepository = UserRepositoryMock()

@user_router.get("/one/{id}")
async def find_one_user(id):
    return {"id": id, "name": "John Doe"}

@user_router.post("")
async def create_user(body: CreateUserDto):

    # idGenerator = RandomIdGenerator()
    idGenerator = UUIDGenerator()

    result = await ErrorDecorator(
        service=CreateUserCommand(
            id_generator=idGenerator, user_repository=userRepository
        ),
        error_handler= error_response_handler,
    ).execute(data=body)

    return result.unwrap()

