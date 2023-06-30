import logging

logging.basicConfig(filename='pg.log', level=logging.INFO)
# # from fastapi import FastAPI
# # import logging
# #
# # app = FastAPI()
# # logger = logging.getLogger(__name__)
# # logger.setLevel(level=logging.DEBUG)
# # file_handler = logging.FileHandler("login.log")
# # formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
# # file_handler.setFormatter(formatter)
# # logger.addHandler(file_handler)
# import logging
#
#
# def get_logger():
#     """Function for logging"""
#     __logger__ = logging.getLogger("")
#     __logger__.setLevel(logging.DEBUG)
#
#     formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s')
#
#     file_handler = logging.FileHandler("employee.log")
#     file_handler.setLevel(logging.DEBUG)
#     file_handler.setFormatter(formatter)
#     __logger__.addHandler(file_handler)
#
#     # console_handler = logging.StreamHandler()
#     # console_handler.setLevel(logging.DEBUG)
#     # console_handler.setFormatter(formatter)
#     # __logger__.addHandler(console_handler)
#
#     return __logger__
#
#
# logger = get_logger()
