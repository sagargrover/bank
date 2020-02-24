dictConfig = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s Module:%(module)s --- %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s - %(message)s'
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'verbose',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/debug.log',
            'maxBytes': 100000000,
            'backupCount': 1
        },
        'access': {
            'level': 'INFO',
            'formatter': 'simple',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/access_log.log',
            'maxBytes': 100000000,
            'backupCount': 1
        },
        'error': {
            'level': 'ERROR',
            'formatter': 'verbose',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/error.log',
            'maxBytes': 100000000,
            'backupCount': 1
        },
    },
    'loggers': {
        'debug_logger': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
        'stream_logger': {
            'handlers': ['access'],
            'level': 'INFO',
            'propagate': False
        },
        'error_logger': {
            'handlers': ['error'],
            'level': 'ERROR',
            'propagate': False
        }
    }
}