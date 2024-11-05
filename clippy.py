import argparse
import pyperclip
import os
import json

config_path = os.path.join(os.path.expanduser("~"), ".config", "clippy.json")


def load_bookmarks():
    try:
        with open(config_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # Create an empty file if it doesn’t exist
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, "w") as file:
            json.dump({}, file)
        return load_bookmarks()  # Retry loading


def display_bookmarks():
    bookmarks = load_bookmarks()
    for key, value in bookmarks.items():
        print(f"{key}: {value}")
    return bookmarks


# Example of copying a bookmarked item to clipboard
def copy_bookmark_to_clipboard(key):
    bookmarks = load_bookmarks()
    if key in bookmarks:
        pyperclip.copy(bookmarks[key])
        print(f"Copied {key}: {bookmarks[key]} to clipboard")
    else:
        print(f"No bookmark found for '{key}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--display", help="display available keys in the clipboard", action="store_true")
    parser.add_argument('-a', '--add', nargs=2, metavar=('KEY', 'VALUE'), help="Add a bookmark with key and value")
    parser.parse_args()
