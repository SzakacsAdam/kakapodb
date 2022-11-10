from abc import ABC
from abc import abstractmethod
from os import mkdir
from os.path import exists
from os.path import isdir
from os.path import isfile
from typing import Generic
from typing import TypeVar

T = TypeVar("T")


class _ValidatorDescriptor(Generic[T], ABC):
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


class DirectoryPath(_ValidatorDescriptor[str]):
    __slots__ = ("name", "create",)

    def __init__(self, create: bool = False) -> None:
        super().__init__()
        self.create: bool = create

    def validate(self, path: str) -> None:
        if not isinstance(path, str):
            raise ValueError()
        if isfile(path):
            raise FileExistsError()
        if not exists(path) and not isdir(path):
            if self.create is False:
                raise FileNotFoundError()
            if self.create is True:
                mkdir(path)
