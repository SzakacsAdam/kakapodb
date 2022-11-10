from os import getcwd
from os.path import join
from typing import Dict, List

from kakapodb.db.database import Database
from kakapodb.db.utils import DirectoryPath
from kakapodb.db.utils import aio_os


class DataBaseManager:
    _DEFAULT_NAME: str = "kakapoDB"
    _DEFAULT_DIR_SRC: str = join(getcwd(), _DEFAULT_NAME)
    src = DirectoryPath(create=True)

    def __init__(self, src_dir: str = _DEFAULT_DIR_SRC) -> None:
        self.src = src_dir
        self._databases: Dict[str, Database] = {}

    async def _load_databases(self) -> None:
        folders: List[str] = await aio_os.listdir(self.src)
        if len(folders) == 0:
            return
        src: str = self.src
        databases: Dict[str, Database] = self._databases
        for folder in folders:
            path: str = join(src, folder)
            databases[folder] = Database(path)
