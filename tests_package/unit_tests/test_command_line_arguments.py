import unittest
from unittest import TestCase
from book_lib.command_line_arguments.command_line_arguments import CommandLineArguments
from tests_package.unit_tests.engine_tests.mocked_data import MockedData


class TestCommandLineArguments(unittest.TestCase):

    def setUp(self):
        self.parser = CommandLineArguments.create_parser(
            {'-T': {'type': str.lower, 'name': '--something', 'nargs': None,
                    'help': 'some help'}})
        self.mocked = MockedData

    def test_argument_parser(self):
        parsed = self.parser.parse_args(['--something', 'test'])
        self.assertEqual(parsed.something, 'test')


if __name__ == "__main__":
    unittest.main()
