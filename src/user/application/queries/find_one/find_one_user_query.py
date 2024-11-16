from common.application.result.application_result import AppResult
from common.application.service.application_service import IApplicationService
from common.domain.utils.is_none import is_none
from user.application.info.user_found_info import user_found_info
from user.application.queries.find_one.types.response import FindOneUserResponse
from user.application.repositories.user_repository import IUserRepository
from user.application.queries.find_one.types.dto import FindOneUserDto
from user.application.errors.not_found import user_not_found_error

class FindOneUserQuery(IApplicationService):
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def execute(self, data: FindOneUserDto) -> AppResult[FindOneUserResponse]:
        user = await self.user_repository.find_one(data.id)

        if is_none(user):
            return AppResult.failure(error=user_not_found_error)

        return AppResult.success(
            FindOneUserResponse(
                id=user.id,
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email
            ),
            info=user_found_info
        )