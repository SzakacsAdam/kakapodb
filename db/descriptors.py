from abc import ABC
from abc import abstractmethod
from typing import Generic
from typing import TypeVar

T = TypeVar("T")


class ValidatorDescriptor(ABC, Generic[T]):
    __slots__ = ("name",)

    def __set_name__(self, owner, name: str) -> None:
        self.name: str = f"_{name}"

    def __get__(self, obj, obj_type: None) -> T:
        return getattr(obj, self.name)

    def __set__(self, obj, value: T) -> None:
        self.validate(value)
        setattr(obj, self.name, value)

    def __delete__(self, obj) -> None:
        delattr(obj, self.name)

    @abstractmethod
    def validate(self, value: T):
        raise NotImplementedError()
