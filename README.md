landing page: https://www.notion.so/1c881def9d8280059df9e6608a300d36?v=1c881def9d8280a68565000cab31ce00

# Commander CLI

A command-line interface (CLI) tool for interacting with DeepSeek AI. This tool allows users to send queries to DeepSeek AI, enforce responses as shell scripts, read input from files, write output to files, and enable verbose logging for detailed output.

## Project Structure

The Commander CLI is organized into a modular structure to ensure separation of concerns and maintainability. Below is an overview of the project structure:

- **`cdr.py`**: The main entry point of the CLI. It handles argument parsing and orchestrates the interaction between different services.
- **`services/`**: Contains classes that encapsulate specific functionalities:
  - **`ai_service.py`**: Manages interactions with DeepSeek AI. Currently, it uses a placeholder for the API call, which would be replaced with actual API integration.
  - **`file_service.py`**: Handles file operations for reading input from files and writing output to files.
  - **`logging_service.py`**: Provides logging functionality, which can be toggled with the verbose flag to display detailed output.
- **`models/`**: Holds data structures for cleaner data management:
  - **`argument_model.py`**: A data class to store parsed command-line arguments, making it easier to pass them between components.
- **`utils/`**: Reserved for utility functions that might be needed across different services or modules:
  - **`helpers.py`**: A placeholder for any helper functions, currently containing a dummy function.

This structure ensures that each component has a specific responsibility, making the codebase easier to maintain and extend.

## Usage

To use the Commander CLI, you can run the `cdr.py` script with various flags and arguments. Below are the available commands and options:

### Basic Command

```bash
python cdr.py [query]
```

- **`query`**: The query or prompt to send to DeepSeek AI. If no query is provided, the tool will prompt for help.

### Flags and Options

| Flag                | Description                          | Example                       | Note                                      |
|---------------------|--------------------------------------|-------------------------------|-------------------------------------------|
| `--seek (-s)`       | Enforce response as Shell script    | `python cdr.py -s`            | Returns error if cannot get Shell script |
| `--help (-h)`       | Displays help information           | `python cdr.py -h`            |                                           |
| `--verbose (-v)`    | Enables detailed output logging     | `python cdr.py -v`            |                                           |
| `--read (-r)`       | Read file as input                  | `python cdr.py -r prompt.txt` | No file type specified = txt file        |
| `--write (-w)`      | Write file as output                | `python cdr.py -w response.md`| No file type specified = txt file        |

### Examples

1. **Send a simple query to DeepSeek AI:**
   ```bash
   python cdr.py "what's good"
   ```

2. **Enforce response as a shell script with verbose logging:**
   ```bash
   python cdr.py "write a script" -s -v
   ```

3. **Read input from a file and write output to another file:**
   ```bash
   python cdr.py -r input.txt -w output.md
   ```

4. **Display help information:**
   ```bash
   python cdr.py -h
   ```

## Installation

Currently, this project is a Python script that can be run directly. To use it:

1. Clone or download the repository to your local machine.
2. Ensure you have Python installed (version 3.x recommended).
3. Navigate to the project directory:
   ```bash
   cd path/to/commander
   ```
4. Run the CLI with the desired arguments as shown in the usage section.

## Future Enhancements

- Integrate the actual DeepSeek AI API for real query processing.
- Add more robust error handling and input validation.
- Expand utility functions in `utils/helpers.py` for additional features.

## Contributing

If you'd like to contribute to this project, feel free to submit pull requests or open issues for bugs, feature requests, or improvements.

## License

This project is open-source and available under the MIT License (or specify your preferred license).
