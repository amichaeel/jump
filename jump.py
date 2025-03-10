#!/usr/bin/env python3
import os
import sys
import json
import subprocess
from pathlib import Path

# Configuration file path
CONFIG_DIR = os.path.expanduser("~/.config/jump")
CONFIG_FILE = os.path.join(CONFIG_DIR, "aliases.json")


def ensure_config_exists():
    """Create config directory and file if they don't exist."""
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as f:
            json.dump({}, f)


def load_aliases():
    """Load aliases from config file."""
    ensure_config_exists()
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)


def save_aliases(aliases):
    """Save aliases to config file."""
    ensure_config_exists()
    with open(CONFIG_FILE, 'w') as f:
        json.dump(aliases, f, indent=2)


def add_alias(path, alias_name):
    """Add a new alias."""
    aliases = load_aliases()
    path = os.path.expanduser(path)

    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist.")
        return False

    aliases[alias_name] = path
    save_aliases(aliases)
    print(f"Added alias '{alias_name}' -> '{path}'")
    return True


def remove_alias(alias_name):
    """Remove an existing alias."""
    aliases = load_aliases()

    if alias_name in aliases:
        del aliases[alias_name]
        save_aliases(aliases)
        print(f"Removed alias '{alias_name}'")
        return True
    else:
        print(f"Error: Alias '{alias_name}' not found.")
        return False


def list_aliases():
    """List all defined aliases."""
    aliases = load_aliases()

    if not aliases:
        print("No aliases defined.")
        return

    print("Defined aliases:")
    for name, path in aliases.items():
        print(f"  {name} -> {path}")


def get_alias_path(alias_name):
    """Get the path for a given alias."""
    aliases = load_aliases()

    if alias_name in aliases:
        return aliases[alias_name]
    else:
        return None


def generate_shell_script():
    """Generate the shell function to source in .bashrc/.zshrc."""
    script = """
# Jump directory alias function (use j as shorthand)
j() {
  if [ "$1" = "add" ]; then
    if [ -n "$2" ] && [ -n "$3" ]; then
      python3 PATH_TO_SCRIPT add "$2" "$3"
    else
      echo "Usage: j add <path> <alias>"
    fi
  elif [ "$1" = "rm" ]; then
    if [ -n "$2" ]; then
      python3 PATH_TO_SCRIPT rm "$2"
    else
      echo "Usage: j rm <alias>"
    fi
  elif [ "$1" = "ls" ]; then
    python3 PATH_TO_SCRIPT ls
  elif [ "$1" = "help" ]; then
    python3 PATH_TO_SCRIPT help
  elif [ -n "$1" ]; then
    local dir=$(python3 PATH_TO_SCRIPT get "$1")
    if [ -n "$dir" ]; then
      cd "$dir"
    else
      echo "Unknown alias: $1"
    fi
  else
    echo "Usage: j <alias> or j add <path> <alias> or j rm <alias> or j ls"
  fi
}
"""
    script = script.replace("PATH_TO_SCRIPT", os.path.abspath(__file__))
    return script


def print_help():
    """Print help information."""
    print("jump - Directory alias manager (use j command)")
    print("\nUsage:")
    print("  j <alias>              - Navigate to the directory for the given alias")
    print("  j add <path> <alias>   - Add a new alias")
    print("  j rm <alias>           - Remove an alias")
    print("  j ls                   - List all aliases")
    print("  j help                 - Show this help message")
    print("  j setup                - Show setup instructions")


def print_setup():
    """Print setup instructions."""
    print("Jump - Directory Alias Manager Setup Instructions")
    print("\nTo set up the j command, add the following to your ~/.bashrc or ~/.zshrc file:")
    print("\n" + generate_shell_script())
    print("\nThen reload your shell configuration with:")
    print("  source ~/.bashrc  # or source ~/.zshrc")


def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) == 4:
        add_alias(sys.argv[2], sys.argv[3])
    elif command == "rm" and len(sys.argv) == 3:
        remove_alias(sys.argv[2])
    elif command == "ls":
        list_aliases()
    elif command == "get" and len(sys.argv) == 3:
        path = get_alias_path(sys.argv[2])
        if path:
            print(path, end='')
    elif command == "help":
        print_help()
    elif command == "setup":
        print_setup()
    else:
        print_help()


if __name__ == "__main__":
    main()
