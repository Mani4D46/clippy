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


def add_bookmark(key, value):
    bookmarks = load_bookmarks()
    
    if key in bookmarks:
        print(f"Key '{key}' already exists. Use a different key.")
        return

    bookmarks[key] = value
    with open(config_path, "w") as file:
        json.dump(bookmarks, file, indent=4)  # Save to file
    print(f"Bookmark added: {key} -> {value}")


# Example of copying a bookmarked item to clipboard
def copy_bookmark(key):
    bookmarks = load_bookmarks()
    if key in bookmarks:
        pyperclip.copy(bookmarks[key])
        print(f"Copied {key}: {bookmarks[key]} to clipboard")
    else:
        print(f"No bookmark found for '{key}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--display", help="display available keys in the clipboard", action="store_true")
    parser.add_argument('-a', '--add', nargs=1, metavar=('KEY'), help="Add a bookmark with key and auto recognized pasted content")
    parser.add_argument('-b', '--bookmark', nargs=2, metavar=('KEY', 'VALUE'), help="Add a bookmark with key and self entered value")
    parser.add_argument('-c', '--copy', nargs=1, metavar=('KEY'), help="Copy the value of a selected key")
    args = parser.parse_args()

    if args.display:
        display_bookmarks()
    elif args.add:
        key = ', '.join(map(str, args.add))  # Join list elements into a single string
        value = str(pyperclip.paste())
    elif args.bookmark:
        key, value = args.bookmark
        add_bookmark(key, value)
    elif args.copy:
        key = ', '.join(map(str, args.copy))
        copy_bookmark(key)
