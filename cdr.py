import argparse
import sys
from services.ai_service import AIService
from services.file_service import FileService
from services.logging_service import LoggingService
from models.argument_model import ArgumentModel

def parse_arguments():
    """
    Parse command-line arguments using argparse.
    This function sets up the argument parser with all the flags and options
    that the CLI supports, including query input, flags for shell script enforcement,
    help, verbosity, and file input/output.
    
    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Commander CLI for interacting with DeepSeek AI")
    parser.add_argument("query", nargs='?', help="Query to send to DeepSeek AI")
    parser.add_argument("--seek", "-s", action="store_true", help="Enforce response as Shell script")
    parser.add_argument("--help", "-h", action="store_true", help="Displays help information")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enables detailed output logging")
    parser.add_argument("--read", "-r", help="Read file as input")
    parser.add_argument("--write", "-w", help="Write file as output")
    return parser.parse_args()

def main():
    """
    Main entry point of the CLI application.
    This function orchestrates the entire flow of the program:
    - Parses command-line arguments.
    - Initializes services based on the arguments.
    - Handles the logic for help display, file reading/writing, and AI interaction.
    """
    # Parse the command-line arguments into a structured format
    args = parse_arguments()
    
    # Create an ArgumentModel instance to hold the parsed arguments for easy access
    argument_model = ArgumentModel(
        query=args.query,
        seek=args.seek,
        help_flag=args.help,
        verbose=args.verbose,
        read_file=args.read,
        write_file=args.write
    )
    
    # Initialize the logging service, which controls output verbosity
    logger = LoggingService(argument_model.verbose)
    
    # If help flag is set, display usage information and exit
    if argument_model.help_flag:
        print("Help information for Commander CLI:")
        print("  cdr [query]          - Talk to DeepSeek AI")
        print("  cdr --seek (-s)      - Enforce response as Shell script")
        print("  cdr --help (-h)      - Displays help information")
        print("  cdr --verbose (-v)   - Enables detailed output logging")
        print("  cdr --read (-r) file - Read file as input")
        print("  cdr --write (-w) file- Write file as output")
        sys.exit(0)
    
    # Initialize file and AI services for handling respective operations
    file_service = FileService(logger)
    ai_service = AIService(logger)
    
    # Start with the query from command line, if provided
    query = argument_model.query
    
    # If a file is specified for reading, override the query with file contents
    if argument_model.read_file:
        query = file_service.read_file(argument_model.read_file)
    
    # If a query exists (either from command line or file), process it with AI service
    if query:
        response = ai_service.get_response(query, enforce_shell=argument_model.seek)
        # If a file is specified for writing, save the response there
        if argument_model.write_file:
            file_service.write_file(argument_model.write_file, response)
        else:
            # Otherwise, print the response to the console
            print(response)
    else:
        # If no query is provided, log a message prompting for help
        logger.log("No query provided. Use --help for usage information.")

if __name__ == "__main__":
    """
    Standard Python idiom to ensure main() is called only if the script is run directly,
    not if it's imported as a module.
    """
    main() 