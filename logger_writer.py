class LoggerWriter:
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level

    def write(self, message):
        if message.strip():  # Avoiding empty lines
            self.logger.log(self.level, message.strip())

    def flush(self):
        pass  # For compatibility with sys.stdout and sys.stderr
