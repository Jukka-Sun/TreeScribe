# TreeScribe

A Python script to extract directory tree structure and code, with an interactive CLI to select directories. The result is saved to a file and copied to the clipboard. This tool is excellent for reviewing code and interactions with tools like ChatGPT, Anthropic, and similar AI-based assistants.

## Features

- Interactive CLI to select directories.
- Extracts and lists file structures and contents.
- Copies the output to the clipboard.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/treex.git
   cd treex
   ```

2. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the script with the root directory and the output file:
```sh
python extractor.py <root_dir> <output_file>
```

Example:
```sh
python extractor.py . output.txt
```

Select the directories you want to include using the arrow keys and space bar, then press enter. The output will be saved to the specified file and copied to the clipboard.

## License

This project is licensed under the MIT License.
