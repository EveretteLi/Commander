"""
Constants module for the Commander CLI application.
This module contains all string constants used throughout the application.
"""

# CLI description and usage
CLI_DESCRIPTION = "Commander CLI for interacting with DeepSeek AI"
CLI_EPILOG = """
Examples:
  cdr "what's good"              # Send a simple query to DeepSeek AI
  cdr "write a script" -s -v     # Enforce response as shell script with verbose logging
  cdr -r input.txt -w output.md  # Read input from file and write output to file
  cdr -h                         # Display help information
"""

# Argument help messages
QUERY_HELP = "Query to send to DeepSeek AI"
SEEK_HELP = "Enforce response as Shell script"
VERBOSE_HELP = "Enables detailed output logging"
READ_HELP = "Read file as input"
WRITE_HELP = "Write file as output"

# Custom help messages
CUSTOM_HELP_HEADER = "Help information for Commander CLI:"
CUSTOM_HELP_COMMANDS = [
    "  cdr [query]          - Talk to DeepSeek AI",
    "  cdr --seek (-s)      - Enforce response as Shell script",
    "  cdr --help (-h)      - Displays help information",
    "  cdr --verbose (-v)   - Enables detailed output logging",
    "  cdr --read (-r) file - Read file as input",
    "  cdr --write (-w) file- Write file as output"
]
CUSTOM_HELP_EXAMPLES_HEADER = "\nExamples:"
CUSTOM_HELP_EXAMPLES = [
    "  cdr \"what's good\"              # Send a simple query to DeepSeek AI",
    "  cdr \"write a script\" -s -v     # Enforce response as shell script with verbose logging",
    "  cdr -r input.txt -w output.md   # Read input from file and write output to file"
]

# Log messages
LOG_PREFIX = "[LOG]: "
NO_QUERY_MESSAGE = "No query provided. Use --help for usage information."
FILE_READ_MESSAGE = "Read query from {}"
FILE_WRITE_MESSAGE = "Response written to {}"
PROCESSING_QUERY_MESSAGE = "Processing query: {}"
ERROR_SHELL_SCRIPT_MESSAGE = "Error: Cannot convert response to Shell script"
ERROR_READING_FILE_MESSAGE = "Error reading file: {}"
ERROR_WRITING_FILE_MESSAGE = "Error writing file: {}" 