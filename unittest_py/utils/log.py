import inspect
import logging
import os


logger = None


def get_logger():
    global logger

    if logger is None:
        log_level = os.environ.get('DBG_LEVEL', 'DEBUG').upper()

        # if log level is set to debug than insert additional log information
        if log_level == 'DEBUG':
            console_formatter = logging.Formatter('%(asctime)s::%(levelname)s\t[%(filename)s]\t%(message)s')
        else:
            console_formatter = logging.Formatter('%(asctime)s::%(levelname)s\t%(message)s')

        console_log_handler = logging.StreamHandler()
        console_log_handler.setFormatter(console_formatter)
        console_log_handler.setLevel(log_level)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(console_log_handler)

    return logger


def log_call(instance=None):
    if instance is None:
        get_logger().debug('%s()', inspect.stack()[1][3])
    else:
        get_logger().debug('%s.%s()', type(instance).__name__, inspect.stack()[1][3])


def enable_file_logging(filename: str, level: int):
    console_formatter = logging.Formatter('%(asctime)s::%(levelname)s\t[%(filename)s]\t%(message)s')
    fh = logging.FileHandler(filename)
    fh.setLevel(level)
    fh.setFormatter(console_formatter)
    get_logger().addHandler(fh)

