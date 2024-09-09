import logging


class Logger:
    def __init__(self, log_file='log.log', level=logging.DEBUG):
        self.log_file = log_file
        self.level = level
        logging.basicConfig(
            format="[{asctime}][{levelname}] {message}",
            style="{",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.DEBUG
        )

    def log(self, message):
        """Log a message with a timestamp."""
        logging.log(level=self.level, msg=message)
