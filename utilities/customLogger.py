import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log", format='%(asctime)s: %(levename)s: %(message)s',
                            datefmt='%m/%d%Y %I:%M:%S %P')
        logging.basicConfig()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
