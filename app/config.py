import os
import logging


class Config:
    pass


logging.basicConfig(
    level=os.getenv('APP_LOG_LEVEL') or 'INFO',
    format="%(asctime)s::%(levelname)s::%(filename)s::%(message)s",
)
