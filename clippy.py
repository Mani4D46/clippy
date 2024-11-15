#!/usr/bin/env python

import argparse
import pyperclip
import os
import json
from termcolor import colored

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
        print(f"{colored(key, "blue")}: {value}")
    return

def display_clipboard():
    bookmarks = load_bookmarks()
    for key, value in bookmarks.items():
        print(value)
    return

def add_bookmark(key, value):
    bookmarks = load_bookmarks()

    if key in bookmarks:
        print(f"{colored("󱫈", "red")} Key '{key}' already exists. Use a different key.")
        return

    bookmarks[key] = value
    with open(config_path, "w") as file:
        json.dump(bookmarks, file, indent=4)
    print(f"{colored("󱫉", "green")} Bookmark added: {key} -> {value}")


def copy_bookmark(key):
    bookmarks = load_bookmarks()
    if key in bookmarks:
        pyperclip.copy(bookmarks[key])
        print(f"{colored("󱫆", "green")} Copied {key}: {bookmarks[key]} to clipboard")
    else:
        print(f"{colored("󱫊", "red")} No bookmark found for '{key}'")


def remove_bookmark(key):
    bookmarks = load_bookmarks()

    if key not in bookmarks:
        print(f"{colored("󱫈", "red")} Key '{key}' does not exist. Use a different key.")
        return

    bookmarks.pop(key)
    with open(config_path, "w") as file:
        json.dump(bookmarks, file, indent=4)
    print(f"{colored("󱫇", "green")} Bookmark removed: {key}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--display", help="display available keys with vals in the clipboard", action="store_true")
    parser.add_argument("-cb", "--clipboard", help="display only available vals in the clipboard", action="store_true")
    parser.add_argument("-n", "--noquit", help="doesn't quit after doing the job", action="store_true")
    parser.add_argument('-a', '--add', nargs=1, metavar=('KEY'), help="Add a bookmark with key and auto recognized pasted content")
    parser.add_argument('-b', '--bookmark', nargs=2, metavar=('KEY', 'VALUE'), help="Add a bookmark with key and self entered value")
    parser.add_argument('-c', '--copy', nargs=1, metavar=('KEY'), help="Copy the value of a selected key")
    parser.add_argument('-r', '--remove', nargs=1, metavar=('KEY'), help="Delete a selected key")

    # For TUI users:
    parser.add_argument("-at", "--addtui", help="same as -a but gives an input field", action="store_true")
    parser.add_argument("-bt", "--bookmarktui", help="same as -b but gives input fields", action="store_true")
    parser.add_argument("-ct", "--copytui", help="same as -c but gives an input field", action="store_true")
    parser.add_argument("-rt", "--removetui", help="same as -r but gives an input field", action="store_true")

    args = parser.parse_args()

    if args.display:
        print(colored(" Here is your clipboard:", "green"))
        display_bookmarks()
    if args.clipboard:
        print(colored("  Clipboard: ", "black", "on_white"))
        display_clipboard()
    elif args.add:
        key = ', '.join(map(str, args.add))  # Join list elements into a single string
        value = str(pyperclip.paste())
        add_bookmark(key, value)
    elif args.bookmark:
        key, value = args.bookmark
        add_bookmark(key, value)
    elif args.copy:
        key = ', '.join(map(str, args.copy))
        copy_bookmark(key)
    elif args.remove:
        key = ', '.join(map(str, args.remove))
        remove_bookmark(key)

    # TUI parsing
    elif args.addtui:
        key = input(colored(" Enter key: ", "black", "on_white") + " ")
        value = str(pyperclip.paste())
        add_bookmark(key, value)
    elif args.bookmarktui:
        key = input(colored(" Enter key:   ", "black", "on_white") + " ")
        value = input(colored(" Enter value: ", "black", "on_white") + " ")
        add_bookmark(key, value)
    elif args.copytui:
        key = input(colored(" Enter key: ", "black", "on_white") + " ")
        copy_bookmark(key)
    elif args.removetui:
        key = input(colored(" Enter key: ", "black", "on_white") + " ")
        remove_bookmark(key)

    
    if args.noquit:
        input()
