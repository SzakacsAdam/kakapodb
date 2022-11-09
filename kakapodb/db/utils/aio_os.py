import os

from kakapodb.db.utils.aio_helper import sync_to_async

access = sync_to_async(os.access)
