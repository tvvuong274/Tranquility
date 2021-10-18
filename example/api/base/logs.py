import logging
from loguru import logger
from idm_config.root_local import LOGGER_PRINT
#
# # logging configuration
#
# LOGGING_LEVEL = logging.DEBUG if LOGGER_PRINT else logging.INFO
# LOGGERS = ("uvicorn.asgi", "uvicorn.access")
#
# logging.getLogger().handlers = [InterceptHandler()]
# for logger_name in LOGGERS:
#     logging_logger = logging.getLogger(logger_name)
#     logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]
#
# logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
#
# def logger(string, log_name='service', type='info'):
#     if LOGGER_PRINT:
#         logger = logging.getLogger(log_name)
#
#         file_log_handler = logging.FileHandler('media/log/{}.log'.format(log_name))
#
#         logger.addHandler(file_log_handler)
#
#         formatter = logging.Formatter('%(asctime)-15s - %(levelname)s - %(message)s')
#         file_log_handler.setFormatter(formatter)
#
#         # stderr_log_handler = logging.StreamHandler()
#         # logger.addHandler(stderr_log_handler)
#
#         # nice output format
#
#         # stderr_log_handler.setFormatter(formatter)
#
#         if type == 'info':
#             logger.info(string)
#         elif type == 'error':
#             logger.error(string)
#
#         logger.handlers.pop()
#     else:
#         print(string)
