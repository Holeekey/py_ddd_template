from sqlalchemy.orm import Session
from common.domain.utils.is_none import is_none
from common.infrastructure.database.database import SessionLocal
from user.application.models.user import User
from user.application.repositories.user_repository import IUserRepository
from user.infrastructure.repositories.models.postgres.sqlalchemy.user_model import UserModel

class UserRepositorySqlAlchemy(IUserRepository):
    def __init__(self):
        self.db: Session = SessionLocal()

    def map_model_to_user(self, user_orm: UserModel)-> User:
        return User(
            id=user_orm.id,
            username=user_orm.username,
            email=user_orm.email,
            password=user_orm.password,
            first_name=user_orm.first_name,
            last_name=user_orm.last_name
        )

    async def find_one(self, id: int):
        for user in self.users:
            if user.id == id:
                return user
        return None
    
    async def find_by_username(self, username: str):
        user_orm = self.db.query(UserModel).filter(UserModel.username == username).first()
        if is_none(user_orm):
            return None
        return self.map_model_to_user(user_orm)

    async def find_by_email(self, email: str):
        user_orm = self.db.query(UserModel).filter(UserModel.email == email).first()
        if is_none(user_orm):
            return None
        return self.map_model_to_user(user_orm)

    async def find_all(self):
        return self.users

    async def save(self, user: User):
        user_orm = UserModel(
            id=user.id,
            username=user.username,
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name
        )
        self.db.add(user_orm)
        self.db.commit()
        self.db.refresh(user_orm)
        return user
    