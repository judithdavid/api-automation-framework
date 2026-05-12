import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Production-grade logger.

    Features:
    - Singleton logger per name
    - Console + file logging
    - Safe log directory creation
    - Log rotation (prevents huge files)
    - No duplicate handlers
    - No log propagation (avoids duplication)
    """

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    # logger.setLevel(level)
    import os

    log_level = os.getenv("LOG_LEVEL", "INFO").upper()

    level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "ERROR": logging.ERROR
    }

    logger.setLevel(level_map.get(log_level, logging.INFO))

    # --- Project root detection ---
    project_root = Path(__file__).resolve().parents[1]
    log_dir = project_root / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / "test.log"

    # --- Formatter ---
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # --- Console Handler ---
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # --- File Handler with rotation ---
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=3
    )
    file_handler.setFormatter(formatter)

    # --- Attach handlers ---
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Prevent double logging from root logger
    logger.propagate = False

    return logger