import asyncio
from asyncio import AbstractEventLoop
from concurrent.futures import Executor
from functools import partial
from functools import wraps
from typing import Callable
from typing import Optional


def sync_to_async(func: Callable):
    @wraps(func)
    async def run(*args, loop: Optional[AbstractEventLoop] = None,
                  executor: Optional[Executor] = None,
                  **kwargs):
        if loop is None:
            loop: AbstractEventLoop = asyncio.get_event_loop()
        pfunc: Callable = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)

    return run
