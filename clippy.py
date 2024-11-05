import argparse
import pyperclip
import os

config_path = os.path.join(os.path.expanduser("~"), "config", "clippy.json")


def load_bookmarks():
    try:
        with open(config_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # Create an empty file if it doesn’t exist
        with open(config_path, "w") as file:
            json.dump({}, file)
        return load_bookmarks()  # Retry loading


def main():


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--display", help="display available keys in the clipboard", action="store_true")
    parser.add_argument("-a", "--add", nargs=2, metavar=('KEY', 'VALUE'), help="Add a key to the clipboard", action="store_true")
    parser.parse_args()

    main()
