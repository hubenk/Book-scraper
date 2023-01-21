import unittest
from unittest import TestCase

import requests

from book_lib.communicator.communicator import Communicator
from book_lib.search_engine.search_engine import URL


class TestCommunicator(TestCase):
    def setUp(self):
        self.valid_url = URL["home_page"]
        self.communicator = Communicator([self.valid_url])
        self.single_response = Communicator(self.valid_url)

    def test_get_responses(self):
        expected_result_response_200 = requests.get(self.valid_url)
        self.assertEqual(str([expected_result_response_200]), str(self.communicator.get_responses()))

    def test_get_single_response(self):
        expected_result_response_200 = requests.get(self.valid_url)
        self.assertEqual(str(expected_result_response_200), str(self.single_response.get_single_response()))

    def test_pool(self):
        expected_result_valid_url = [self.valid_url]
        self.assertEqual(expected_result_valid_url, self.communicator.pool)


if __name__ == "__main__":
    unittest.main()
