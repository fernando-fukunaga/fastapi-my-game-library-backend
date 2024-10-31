from abc import ABC, abstractmethod


class AbstractEntityAdapter(ABC):

    @abstractmethod
    def to_entity(self, sqlalchemy_model):
        pass

    def to_sqlalchemy_model(self, entity):
        pass
