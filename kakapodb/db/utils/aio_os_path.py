from os import path

from kakapodb.db.utils.aio_helper import sync_to_async

exists = sync_to_async(path.exists)
isfile = sync_to_async(path.isfile)
isdir = sync_to_async(path.isdir)
