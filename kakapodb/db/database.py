from os import getcwd
from os.path import join
from typing import Dict

from kakapodb.db.collection import Collection
from kakapodb.db.utils import DirectoryPath


class Database:
    _DEFAULT_NAME: str = "default"
    _DEFAULT_DIR_SRC: str = join(getcwd(), _DEFAULT_NAME)
    src = DirectoryPath(create=True)

    def __init__(self, src_dir: str = _DEFAULT_DIR_SRC) -> None:
        self.src = src_dir
        self.collections: Dict[str, Collection] = {

        }
