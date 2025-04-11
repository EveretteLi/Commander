class LoggingService:
    def __init__(self, verbose):
        self.verbose = verbose
    
    def log(self, message):
        if self.verbose:
            print(f"[LOG]: {message}") 