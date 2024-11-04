import argparse


def main():




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--display", help="display available keys in the clipboard", action="store_true")
    parser.add_argument("-a", "--add", nargs=2, metavar=('KEY', 'VALUE'), help="Add a key to the clipboard", action="store_true")
    parser.parse_args()

    main()
