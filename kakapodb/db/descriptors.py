from typing import Generic, Optional
from typing import TypeVar

T = TypeVar("T")


class _SRC(Generic[T]):
    __slots__ = ("name",)

    def __set_name__(self, owner, name: str) -> None:
        self.name: str = f"_{name}"

    def __get__(self, obj, obj_type: None) -> T:
        return getattr(obj, self.name)

    def __set__(self, obj, value: T) -> None:
        setattr(obj, self.name, value)

    def __delete__(self, obj) -> None:
        delattr(obj, self.name)


class _SrcFile:

    def __init__(self, create: bool = False) -> None:
        self._src: Optional[str] = None

    @property
    def src(self) -> str:
        return self._src

    async def set_src(self, src: str) -> None:
        self._src = src


if __name__ == '__main__':
    import asyncio


    async def main():
        file = _SrcFile()
        print(file.src)
        await file.set_src("alma")
        print(file.src)


    asyncio.run(main())
