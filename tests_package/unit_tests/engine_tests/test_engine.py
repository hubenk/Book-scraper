""" Module containing unittests for SearchEngine class """
import unittest
from mock import patch

from bs4 import BeautifulSoup
from book_lib.books_catalog.books_catalog import BooksCatalog
from book_lib.search_engine.search_engine import SearchEngine
from book_lib.communicator.communicator import Communicator
from mocked_data import MockedData
from tests_package.unit_tests.engine_tests.test_book_dict import TEST_BOOK_DICT, TEST_BOOK_RESPONSE


class SearchEngineTests(unittest.TestCase):
    def setUp(self):
        super(SearchEngineTests, self).setUp()
        self.mocked_arg_parser = MockedData.get_mocked_arg_parser()
        self.mocked_test_html = MockedData.mocked_html_path_builder()
        self.expected_description = MockedData.get_expected_description()
        self.engine = SearchEngine(BooksCatalog(self.mocked_arg_parser), self.mocked_arg_parser)
        self.soup = BeautifulSoup(self.mocked_test_html, 'lxml')

    def test_get_catalog_pages(self):
        with patch('book_lib.communicator.communicator.Communicator.get_responses') as method:
            self.engine.get_catalog_pages(1, 2)
            method.assert_called()

    def test_get_category_pages(self):
        with patch('book_lib.communicator.communicator.Communicator.get_responses') as method:
            self.engine.get_category_pages(['Travel'])
            method.assert_called()

    def test_extract_book_links(self):
        with patch('book_lib.communicator.communicator.Communicator.get_responses') as method:
            response = Communicator(
                'https://books.toscrape.com/catalogue/category/books/travel_2').get_single_response()
            self.engine.extract_book_links([response])
            method.assert_called()

    def test_fetch_book_data(self):
        self.assertListEqual(self.engine.fetch_book_data([TEST_BOOK_RESPONSE]), [TEST_BOOK_DICT])

    def test_get_title(self):
        self.assertTrue(self.engine.get_title(self.soup), 'A Light in the Attic')

    def test_get_price(self):
        self.assertEqual(self.engine.get_price(self.soup), 51.77)

    def test_get_availability(self):
        self.assertEqual(self.engine.get_availability(self.soup), 22)

    def test_get_description(self):
        self.assertSequenceEqual(self.engine.get_description(self.soup), self.expected_description)

    def test_get_genre(self):
        self.assertEqual(self.engine.get_genre(self.soup), "Poetry")

    def test_get_rating(self):
        self.assertEqual(self.engine.get_rating(self.soup), 3)

    def test_get_upc(self):
        self.assertSequenceEqual(self.engine.get_upc(self.soup), "a897fe39b1053632")

    def test_get_product_type(self):
        self.assertEqual(self.engine.get_product_type(self.soup), "Books")

    def test_get_price_excl_tax(self):
        self.assertEqual(self.engine.get_price_excl_tax(self.soup), '51.77')

    def test_get_price_incl_tax(self):
        self.assertEqual(self.engine.get_price_incl_tax(self.soup), '51.77')

    def test_get_tax(self):
        self.assertEqual(self.engine.get_tax(self.soup), '0.00')

    def test_get_stock(self):
        self.assertEqual(self.engine.get_stock(self.soup), 'In stock (22 available)')

    def test_get_reviews(self):
        self.assertEqual(self.engine.get_reviews(self.soup), '0')


if __name__ == "__main__":
    unittest.main()
