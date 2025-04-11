#!/usr/bin/env python3
"""
Commander CLI - A command-line interface for interacting with DeepSeek AI.
This module provides a functional approach to CLI operations with improved naming.
"""

import sys
import argparse
from typing import Optional, List, Callable, Dict, Any, Tuple

from services.ai_service import AIService
from services.file_service import FileService
from services.logging_service import LoggingService
from models.argument_model import ArgumentModel
from utils.constants import (
    CLI_DESCRIPTION, CLI_EPILOG, QUERY_HELP, SEEK_HELP, VERBOSE_HELP,
    READ_HELP, WRITE_HELP, CUSTOM_HELP_HEADER, CUSTOM_HELP_COMMANDS,
    CUSTOM_HELP_EXAMPLES_HEADER, CUSTOM_HELP_EXAMPLES, LOG_PREFIX,
    NO_QUERY_MESSAGE, FILE_READ_MESSAGE, FILE_WRITE_MESSAGE,
    PROCESSING_QUERY_MESSAGE, ERROR_SHELL_SCRIPT_MESSAGE,
    ERROR_READING_FILE_MESSAGE, ERROR_WRITING_FILE_MESSAGE
)

def create_argument_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser with improved naming.
    
    Returns:
        argparse.ArgumentParser: Configured argument parser instance.
    """
    argument_parser = argparse.ArgumentParser(
        description=CLI_DESCRIPTION,
        epilog=CLI_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    argument_parser.add_argument(
        'user_query',
        nargs='?',
        help=QUERY_HELP
    )
    argument_parser.add_argument(
        '-s', '--seek',
        action='store_true',
        help=SEEK_HELP
    )
    argument_parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help=VERBOSE_HELP
    )
    argument_parser.add_argument(
        '-r', '--read',
        help=READ_HELP
    )
    argument_parser.add_argument(
        '-w', '--write',
        help=WRITE_HELP
    )
    
    return argument_parser

def display_help_information() -> None:
    """
    Display formatted help information for the CLI.
    Pure function with no side effects except printing.
    """
    print(f"\n{CUSTOM_HELP_HEADER}\n")
    for command in CUSTOM_HELP_COMMANDS:
        print(command)
    print(f"{CUSTOM_HELP_EXAMPLES_HEADER}")
    for example in CUSTOM_HELP_EXAMPLES:
        print(example)
    print()

def create_argument_model(parsed_args: argparse.Namespace) -> ArgumentModel:
    """
    Create an ArgumentModel instance from parsed arguments.
    Pure function that transforms input to output without side effects.
    
    Args:
        parsed_args: Parsed command line arguments.
    
    Returns:
        ArgumentModel: Immutable argument model instance.
    """
    return ArgumentModel(
        query=parsed_args.user_query,
        seek=parsed_args.seek,
        help_flag=False,
        verbose=parsed_args.verbose,
        read_file=parsed_args.read,
        write_file=parsed_args.write
    )

def read_input_from_file(file_service: FileService, file_path: str) -> str:
    """
    Read input from a file using the file service.
    Pure function that transforms file path to content.
    
    Args:
        file_service: FileService instance for file operations.
        file_path: Path to the input file.
    
    Returns:
        str: Content read from the file.
    """
    return file_service.read_file(file_path)

def write_output_to_file(file_service: FileService, file_path: str, content: str) -> None:
    """
    Write content to a file using the file service.
    
    Args:
        file_service: FileService instance for file operations.
        file_path: Path to the output file.
        content: Content to write to the file.
    """
    file_service.write_file(file_path, content)

def process_user_query(
    ai_service: AIService,
    user_query: str,
    enforce_shell: bool = False
) -> str:
    """
    Process a user query through the AI service.
    Pure function that transforms query to response.
    
    Args:
        ai_service: AIService instance for AI operations.
        user_query: Query to process.
        enforce_shell: Whether to enforce shell script output.
    
    Returns:
        str: AI service response.
    """
    return ai_service.get_response(user_query, enforce_shell)

def handle_error(logger: LoggingService, error_message: str) -> None:
    """
    Handle and log an error message.
    
    Args:
        logger: LoggingService instance for logging.
        error_message: Error message to log.
    """
    logger.log(error_message)
    print(f"{LOG_PREFIX}{error_message}")

def main() -> None:
    """
    Main entry point for the CLI application.
    Orchestrates the flow of the application using functional composition.
    """
    # Initialize services
    argument_parser = create_argument_parser()
    parsed_arguments = argument_parser.parse_args()
    
    # Create logging service first for error handling
    logging_service = LoggingService(parsed_arguments.verbose)
    
    try:
        # Create argument model
        cli_arguments = create_argument_model(parsed_arguments)
        
        # Initialize services with logger
        file_service = FileService(logging_service)
        ai_service = AIService(logging_service)
        
        # Handle help flag
        if cli_arguments.help_flag:
            display_help_information()
            return
        
        # Get user query
        user_query = cli_arguments.query
        if cli_arguments.read_file:
            user_query = read_input_from_file(file_service, cli_arguments.read_file)
            logging_service.log(FILE_READ_MESSAGE.format(cli_arguments.read_file))
        
        if not user_query:
            handle_error(logging_service, NO_QUERY_MESSAGE)
            return
        
        # Process query and get response
        ai_response = process_user_query(
            ai_service,
            user_query,
            cli_arguments.seek
        )
        
        # Handle output
        if cli_arguments.write_file:
            write_output_to_file(file_service, cli_arguments.write_file, ai_response)
            logging_service.log(FILE_WRITE_MESSAGE.format(cli_arguments.write_file))
        else:
            print(ai_response)
            
    except Exception as error:
        handle_error(logging_service, str(error))
        sys.exit(1)

if __name__ == "__main__":
    main() 