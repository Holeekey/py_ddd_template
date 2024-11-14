from user.application.models.user import User
from user.application.repositories.user_repository import IUserRepository


class UserRepositoryMock(IUserRepository):
    def __init__(self):
        self.users = []

    def find_one(self, id: int):
        for user in self.users:
            if user.id == id:
                return user
        return None

    def find_all(self):
        return self.users

    def save(self, user: User):
        self.users.append(user)
        return user