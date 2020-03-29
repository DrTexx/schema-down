#!/usr/bin/env python3 -e

"""Handle CLI interactions."""

# package
from .parser import SDParser


def main() -> None:
    """Handle CLI interaction for Volux."""

    sdparser = SDParser()
    sdparser.handle_arguments(sdparser.arguments, debug=True)


if __name__ == "__main__":

    main()
