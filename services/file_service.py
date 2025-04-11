from utils.constants import ERROR_READING_FILE_MESSAGE, ERROR_WRITING_FILE_MESSAGE

class FileService:
    def __init__(self, logger):
        """
        Initialize the File Service with a logger.
        
        Args:
            logger: LoggingService instance to log file operations and errors.
        """
        self.logger = logger
    
    def read_file(self, file_path):
        """
        Read the contents of a file as input for the AI query.
        
        Args:
            file_path (str): Path to the file to read.
        
        Returns:
            str: Contents of the file.
        
        Raises:
            Exception: If there's an error reading the file (e.g., file not found).
        """
        self.logger.log(f"Reading file: {file_path}")
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except Exception as e:
            self.logger.log(ERROR_READING_FILE_MESSAGE.format(e))
            raise
    
    def write_file(self, file_path, content):
        """
        Write the AI response to a file.
        
        Args:
            file_path (str): Path to the file to write to.
            content (str): Content to write to the file.
        
        Raises:
            Exception: If there's an error writing to the file (e.g., permission denied).
        """
        self.logger.log(f"Writing to file: {file_path}")
        try:
            with open(file_path, 'w') as file:
                file.write(content)
        except Exception as e:
            self.logger.log(ERROR_WRITING_FILE_MESSAGE.format(e))
            raise 