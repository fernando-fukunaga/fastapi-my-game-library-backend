import logging

from sqlalchemy.orm import Session
from src.infra.database.repositories.abstract_user_repository import AbstractUserRepository
from src.errors import errors
from src.entities.user_entity import UserEntity
from src.adapters.sqlalchemy.entity_adapters import sqlalchemy_user_adapter
from src.infra.database.models.sqlalchemy_models import UserSQLAlchemyModel

logger = logging.getLogger(__name__)


class SQLAlchemyUserRepository(AbstractUserRepository):

    def __init__(self, session: Session) -> None:
        self.session = session

    def insert_user(self, user: UserEntity) -> UserEntity | None:
        try:
            self.session.add(sqlalchemy_user_adapter(user))
            self.session.commit()
        except Exception as e:
            logger.error(f"Something went wrong with the database while trying to insert user: {e}")
            return None

        return user

    def select_user(self, attribute: str, value: str) -> UserEntity | None:
        try:
            user = self.session.query(
                UserSQLAlchemyModel
            ).filter_by(**{attribute: value}).first()
        except Exception as e:
            logger.error(f"Something went wrong with the database while trying to select user: {e}")
            return None
        
        if not user:
            return None
        
        return user
