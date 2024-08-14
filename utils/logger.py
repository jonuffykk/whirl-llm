import logging
from core.config import settings

def setup_logging():
    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=settings.LOG_FILE,
    )

logger = logging.getLogger(__name__)