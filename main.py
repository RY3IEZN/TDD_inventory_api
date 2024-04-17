from fastapi import FastAPI
import logging
import logging.config
from app.routes import category_routes

# set log level
# logging.basicConfig(level=logging.DEBUG)

# setup logging
logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)


# app
app = FastAPI()

# include the router
app.include_router(category_routes.router, prefix="/api/v1/category", tags=["Category"])
