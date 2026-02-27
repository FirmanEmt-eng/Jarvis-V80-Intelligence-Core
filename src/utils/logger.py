import logging
import os
from datetime import datetime

def setup_v80_logger():
    """
    Standard Logging for Jarvis V80 Intelligence.
    Outputs to both console and a session-based log file.
    """
    # Pastikan folder logs ada
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Nama file log berdasarkan tanggal hari ini
    log_file = f"{log_dir}/v80_ops_{datetime.now().strftime('%Y%m%d')}.log"

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)s | %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    logger = logging.getLogger("JarvisV80")
    logger.info("--- Jarvis V80 Logger Initialized ---")
    return logger

# Singleton instance
v80_log = setup_v80_logger()
