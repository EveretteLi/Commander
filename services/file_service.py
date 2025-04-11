class FileService:
    def __init__(self, logger):
        self.logger = logger
    
    def read_file(self, file_path):
        self.logger.log(f"Reading file: {file_path}")
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except Exception as e:
            self.logger.log(f"Error reading file: {e}")
            raise
    
    def write_file(self, file_path, content):
        self.logger.log(f"Writing to file: {file_path}")
        try:
            with open(file_path, 'w') as file:
                file.write(content)
        except Exception as e:
            self.logger.log(f"Error writing file: {e}")
            raise 