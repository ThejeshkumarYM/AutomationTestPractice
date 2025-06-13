import logging
import os

# class logcol:
#     @staticmethod
#     def loggen():
#         path=os.path.abspath(os.curdir) + '\\Nopcommerce\\logs\\automation.log'
#         logging.basicConfig(filename=path,
#                             format='%(asctime)s : %(levelname)s : %(message)s',
#                             datefmt='%Y-%m-%d %H:%M:%S')
#         logger=logging.getLogger()
#         logger.setLevel(logging.DEBUG)
#         return logger

class logcol:
    @staticmethod
    def loggen():
        log_dir = os.path.abspath(os.curdir) + '\\logs\\'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        path = log_dir + 'automation.log'

        logging.basicConfig(filename=path,
                            format='%(asctime)s : %(levelname)s : %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger