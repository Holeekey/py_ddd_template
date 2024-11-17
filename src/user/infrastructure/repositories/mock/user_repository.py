from typing import List
from user.application.models.user import User
from user.application.repositories.user_repository import IUserRepository


class UserRepositoryMock(IUserRepository):

    users: List[User]

    def __init__(self):
        self.users = []

    async def find_one(self, id: int):
        for user in self.users:
            if user.id == id:
                return user
        return None

    async def find_by_username(self, username: str):
        for user in self.users:
            if user.username == username:
                return user
        return None

    async def find_by_email(self, email: str):
        for user in self.users:
            if user.email == email:
                return user
        return None

    async def find_all(self):
        return self.users

    async def save(self, user: User):
        self.users.append(user)
        return user
