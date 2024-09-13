from src.entities.user_entity import UserEntity
from src.infra.database.models.sqlalchemy_models import UserSQLAlchemyModel


def sqlalchemy_user_adapter(user: UserEntity | UserSQLAlchemyModel) -> UserEntity | UserSQLAlchemyModel:
    if type(user) is UserEntity:
        return UserSQLAlchemyModel(
            id=user.id,
            name=user.name,
            email=user.email,
            username=user.username,
            password=user.password
        )

    return UserEntity(
        id=user.id,
        name=user.name,
        email=user.email,
        username=user.username,
        password=user.password
    )
