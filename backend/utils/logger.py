
import logging

def setup_logging(level=logging.INFO):

    logging.basicConfig(
        level=level,  
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
    return logging.getLogger(__name__)