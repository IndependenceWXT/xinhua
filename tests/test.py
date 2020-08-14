import logging
logger = logging.getLogger('__file__')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(ch)
logger.info('creating an instance of auxiliary_module.Auxiliary')
if __name__ == '__main__':
    logger.info('creating an instance of auxiliary_module.Auxiliary')