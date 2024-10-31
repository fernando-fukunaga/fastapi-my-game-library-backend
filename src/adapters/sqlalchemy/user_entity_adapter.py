from src.entities.user_entity import UserEntity
from src.infra.database.models.sqlalchemy_models import UserSQLAlchemyModel
from src.adapters.sqlalchemy.abstract_entity_adapter import AbstractEntityAdapter


class UserEntityAdapter(AbstractEntityAdapter):

    def to_entity(self, sqlalchemy_model):
        return UserEntity(
            id=sqlalchemy_model.id,
            name=sqlalchemy_model.name,
            email=sqlalchemy_model.email,
            username=sqlalchemy_model.username,
            password=sqlalchemy_model.password
        )

    def to_sqlalchemy_model(self, entity):
        return UserSQLAlchemyModel(
            id=entity.id,
            name=entity.name,
            email=entity.email,
            username=entity.username,
            password=entity.password
        )
