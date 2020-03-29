"""Defines class for processing CLI interactions."""

import argparse


class SDParser:
    """Class for handling CLI interaction."""

    def __init__(self):
        """See class docstring."""
        self.parser = argparse.ArgumentParser()

        self._add_optionals(self.parser)
        self.subparsers = self._add_subparser(self.parser)

        self.gen_parser = self._add_gen_parser(self.subparsers)
        # self.demo_parser = self._add_demo_parser(self.subparsers)
        # self.module_parser = self._add_module_parser(self.subparsers)
        # self.script_parser = self._add_script_parser(self.subparsers)

        self.arguments = self.parser.parse_args()

    def handle_arguments(self, arguments, debug=False):
        """Handle the parsed arguments."""
        if debug:
            print(arguments)

        if arguments.version is True:

            self.print_version()
            exit()

        elif arguments.subcommand == "gen":

            output = self.generate(arguments.schema)

            print(output)

            exit()

        else:

            print("internal error")

    def print_version(self) -> None:
        """Print the package verison."""
        from . import __name__, __version__

        print(__name__, __version__)

    def generate(self, user_schema_path):
        """Generate documentation based on schema."""
        from .generate import generate

        return generate(user_schema_path)

    def _add_optionals(self, root_parser: argparse.ArgumentParser) -> None:
        # optional arguments before sub-commands
        root_parser.add_argument(
            "-V",
            "--version",
            action="store_true",
            help="print version information and exit",
        )

    def _add_subparser(
        self, root_parser: argparse.ArgumentParser
    ) -> argparse._SubParsersAction:
        # create subparsers object
        subparsers = root_parser.add_subparsers(
            dest="subcommand", help="available sub-commands"
        )
        return subparsers

    def _add_gen_parser(
        self, child_parser: argparse._SubParsersAction
    ) -> argparse.ArgumentParser:
        # create the parser for the "gen" command
        parser_gen = child_parser.add_parser(
            "gen",
            help="generate markdown based on a schema",
            description="generate markdown based on a schema",
        )
        parser_gen.add_argument(
            "-s",
            "--schema",
            action="store",
            help="schema to generate documentation for (filepath)",
        )
        return parser_gen
