#!/usr/bin/env python3
import argparse

def do_work(args):
    """Performs the main work of the script based on the parsed arguments."""
    if args.verbose:
        print("Verbose mode is enabled.")

    if args.file:
        print(f"The specified file is: {args.file}")

    if args.positional_args:
        print("Positional arguments:")
        for arg in args.positional_args:
            print(f"- {arg}")

def main():
    parser = argparse.ArgumentParser(description="A simple example program that prints provided arguments.")

    # Optional arguments
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("-f", "--file", type=str, help="Specify an input file")

    # Positional arguments
    parser.add_argument("positional_args", nargs="*", help="A list of positional arguments")

    args = parser.parse_args()

    do_work(args)

if __name__ == "__main__":
    main()