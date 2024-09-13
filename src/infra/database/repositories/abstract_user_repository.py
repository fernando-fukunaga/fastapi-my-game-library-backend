from abc import ABC, abstractmethod
from src.entities.user_entity import UserEntity


class AbstractUserRepository(ABC):
    @abstractmethod
    def insert_user(self, user: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def select_user(self, attribute: str, value: str) -> UserEntity:
        pass
