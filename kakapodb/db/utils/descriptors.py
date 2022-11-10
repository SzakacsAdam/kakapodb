from abc import ABC
from abc import abstractmethod
from os import mkdir
from os.path import exists
from os.path import isdir
from os.path import isfile
from typing import Generic
from typing import TypeVar

T = TypeVar("T")


class _ValidatorDescriptor(ABC, Generic[T]):
    __slots__ = ("name",)

    def __init__(self) -> None:
        self.name: str = ''

    def __set_name__(self, owner, name: str) -> None:
        self.name: str = f"_{name}"

    def __get__(self, obj, obj_type: None) -> T:
        return getattr(obj, self.name)

    def __set__(self, obj, value: T) -> None:
        self.validate(value)
        setattr(obj, self.name, value)

    @abstractmethod
    def validate(self, value: T) -> None:
        raise NotImplementedError()


class DirectoryPath(_ValidatorDescriptor):
    __slots__ = ("create",)

    def __init__(self, create: bool = False) -> None:
        super().__init__()
        self.create: bool = create

    def __set_name__(self, owner, name: str) -> None:
        self.name: str = f"_{name}"

    def __get__(self, obj, obj_type: None) -> str:
        return getattr(obj, self.name)

    def __set__(self, obj, value: str) -> None:
        self.validate(value)
        setattr(obj, self.name, value)

    def validate(self, path: str) -> None:
        if not isinstance(path, str):
            raise ValueError()
        if isfile(path):
            raise FileExistsError()
        if not exists(path) and self.create is False:
            raise FileNotFoundError()
        if not isdir(path) and self.create is False:
            raise FileNotFoundError()
        mkdir(path)
