from fastapi import FastAPI
import logging
import logging.config

# set log level
# logging.basicConfig(level=logging.DEBUG)

# setup logging
logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)


# app
app = FastAPI()
