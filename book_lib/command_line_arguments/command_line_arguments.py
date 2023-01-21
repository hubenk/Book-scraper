""" Module containing CommandLineArguments class. """

import argparse

ARGUMENTS = {
    '-g': {'type': str.lower, 'name': '--genre', 'nargs': '+',
           'help': 'genre'},
    '-d': {'type': str.lower, 'name': '--description', 'nargs': '+',
           'help': 'description keywords'},
    '-f': {'type': str.lower, 'name': '--filter', 'nargs': '+',
           'help': 'filter'},
    '-n': {'type': int, 'name': '--number', 'nargs': None,
           'help': 'number of books'},
    '-s': {'type': str.lower, 'name': '--sort', 'nargs': '+',
           'help': 'sort(ascending/descending)'},
    '-t': {'type': str.lower, 'name': '--title', 'nargs': None,
           'help': 'book title'},
    '-F': {'type': str.lower, 'name': '--json', 'nargs': None,
           'help': 'book titles to search (json)'},
    '-X': {'type': str.lower, 'name': '--gui', 'nargs': None,
           'help': 'user interface'},
}


class CommandLineArguments(object):
    """
    Class responsible for reading and parsing command line arguments.
    """

    def __init__(self):
        self.__argument_parser = self.create_parser(ARGUMENTS)

    def __str__(self):
        return self.__argument_parser

    @staticmethod
    def create_parser(args_map):
        """
        Creates arg parser from arguments dict
        :param args_map: ARGUMENTS dict
        :return: parsed data
        """
        parser = argparse.ArgumentParser(description="Book Scraper")
        for arg in args_map:
            parser.add_argument(arg, args_map[arg]['name'],
                                type=args_map[arg]['type'],
                                nargs=args_map[arg]['nargs'],
                                help=args_map[arg]['help'],
                                default=None)
        return parser

    @property
    def argument_parser(self):
        """:return argument parser"""
        return self.__argument_parser.parse_args()
