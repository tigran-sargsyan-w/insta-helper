import logging
import sys

from logger_writer import LoggerWriter


class FileUtils:
    def __init__(self, log_filename="app.log"):
        # Setting up logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_filename, mode='w'),
                logging.StreamHandler(sys.stdout)  # Redirect all print to log
            ]
        )
        self.logger = logging.getLogger(__name__)
        sys.stdout = LoggerWriter(self.logger, logging.INFO)
        sys.stderr = LoggerWriter(self.logger, logging.ERROR)

    def log(self, message):
        self.logger.info(message)

    @staticmethod
    def read_usernames(filename):
        try:
            with open(filename, 'r') as file:
                content = file.read().strip()
                usernames = content.split(',')
                usernames = [username.strip() for username in usernames]
            return usernames
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return []

