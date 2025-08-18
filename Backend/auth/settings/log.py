import logging
import logging.config

logger = logging.getLogger(__name__)
logging.getLogger("uvicorn.error").propagate = False

logging.basicConfig(filename = "logs/App.log", level = logging.INFO)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False, 
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(message)s",
            "use_colors": True,
        },
        "file": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "sqlalchemy_file": {
            "formatter": "file",
            "class": "logging.FileHandler",
            "filename": "logs/sqlalchemy.log",
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "uvicorn": {"handlers": ["default"], "level": "INFO"},
        "uvicorn.error": {"level": "INFO"},
        "uvicorn.access": {"handlers": ["default"], "level": "INFO", "propagate": False},

        
        "sqlalchemy.engine": {
            "handlers": ["sqlalchemy_file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

logging.config.dictConfig(LOGGING_CONFIG)