# Jump

A lightweight CLI directory alias manager that helps you navigate your filesystem faster.

## Overview

Jump allows you to create shortcuts (aliases) to frequently accessed directories and quickly navigate to them using a simple command. Instead of typing `cd /path/to/your/very/long/directory/name`, you can simply use `j myalias`.

## Features

* Create aliases for any directory path
* Navigate to aliased directories with a single command
* List all defined aliases
* Remove aliases when no longer needed
* Easy to set up and use

## Installation

1. Download the `jump.py` script to your preferred location
2. Make it executable:
   ```bash
   chmod +x /path/to/jump.py
   ```
3. Run the setup command to get installation instructions:
   ```bash
   python3 /path/to/jump.py setup
   ```
4. Add the generated shell function to your `~/.bashrc` or `~/.zshrc` file
5. Reload your shell configuration:
   ```bash
   source ~/.bashrc  # or source ~/.zshrc
   ```

## Usage

Once installed, you can use the following commands:

* `j <alias>` - Navigate to the directory for the given alias
* `j add <path> <alias>` - Add a new alias
* `j rm <alias>` - Remove an alias
* `j ls` - List all aliases
* `j help` - Show help message
* `j setup` - Show setup instructions

### Examples

```bash
# Add an alias for your projects directory
j add ~/projects projects

# Navigate to your projects directory
j projects

# Add an alias for a deeply nested directory
j add ~/work/client/2023/project/src/components components

# Navigate to that directory with a single command
j components

# List all your defined aliases
j ls

# Remove an alias you no longer need
j rm components
```

## Configuration

Jump stores all aliases in a JSON file located at `~/.config/jump-cli/aliases.json`. This file is created automatically when you add your first alias.

## License

[MIT License](https://claude.ai/chat/LICENSE)

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to report bugs or request features.

## Author

This tool was created to simplify navigation between frequently used directories and boost productivity.
