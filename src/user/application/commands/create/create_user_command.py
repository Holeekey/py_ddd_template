from common.application.id_generator.id_generator import IDGenerator
from common.application.result.application_result import AppResult
from common.application.service.application_service import IApplicationService
from user.application.commands.create.types.dto import CreateUserDto
from user.application.commands.create.types.response import CreateUserResponse
from user.application.repositories.user_repository import IUserRepository
from user.application.info.user_created_info import user_created_info
from user.application.models.user import User


class CreateUserCommand(IApplicationService):

    def __init__(self, id_generator: IDGenerator, user_repository: IUserRepository):
        self._user_repository = user_repository
        self._id_generator = id_generator

    def execute(self, data: CreateUserDto) -> AppResult[CreateUserResponse]:

        user = User(
            id=self._id_generator.generate(),
            first_name=data.first_name,
            last_name=data.last_name,
            email=data.email,
            password=data.password,
            username=data.username,
        )

        self._user_repository.save(user=user)

        return AppResult.success(
            value=CreateUserResponse(id=user.id), info=user_created_info
        )
