
LOGGING_CONFIG = {
    "version": 1,
    "loggers": {
        "credit_card_validator": {
            "level": "DEBUG",
            "handlers": ["console_handler", "file_handler"],
            "propagate": False
        },
        # "": {
        #     "level": "DEBUG",
        #     "handlers": ["console_handler", "file_handler"],
        #     "propogate": False
        # },
        # "flask": {
        #     "level": "INFO",
        #     "handlers": ["console_handler", "file_handler"],
        #     "propogate": False
        # },
        # this logger will write logs into file
        "debug": {
            "level": "INFO",
            "handlers": ["file_handler"],
            "propagate": False,
        },
    },
    "handlers": {
        "console_handler": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "simple"
        },
        "file_handler": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "debug.log",
            "maxBytes": 1024,
            "backupCount": 3,
            "formatter": "simple",
        }
    },
    "formatters": {
        "simple": {
            "format": "%(pathname)s:%(lineno)d %(name)s %(asctime)s - %(levelname)s - %(message)s",
        },
    },
}
