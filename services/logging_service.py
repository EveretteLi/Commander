from utils.constants import LOG_PREFIX

class LoggingService:
    def __init__(self, verbose):
        """
        Initialize the Logging Service with verbosity setting.
        
        Args:
            verbose (bool): If True, detailed logs will be printed to console.
        """
        self.verbose = verbose
    
    def log(self, message):
        """
        Log a message if verbose mode is enabled.
        
        Args:
            message (str): The message to log.
        """
        if self.verbose:
            print(f"{LOG_PREFIX}{message}") 