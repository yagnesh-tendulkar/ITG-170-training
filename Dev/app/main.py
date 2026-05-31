import logging
from fastapi import FastAPI
from app.logging.config import setup_app_logging
from app.exceptions.handlers import add_global_exception_handlers
from app.database.connection import boot_database
from app.routes.developer import router as developer_router

# Initialize logging records first
setup_app_logging()
logger = logging.getLogger("app_main")

app = FastAPI(title="Production Level Developer Platform API")

# Register global exception handlers
add_global_exception_handlers(app)

@app.on_event("startup")
def on_startup():
    # Automatically creates 'dev_platform.db' if missing
    boot_database()
    logger.info("Application complete bootstrap phase finalized successfully.")

# Include endpoints from our routes module
app.include_router(developer_router)