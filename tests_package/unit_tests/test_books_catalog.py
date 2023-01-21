import unittest
from unittest import TestCase
from tests_package.unit_tests.input_values.set_up_test import SetUpTest
from book_lib.books_catalog.books_catalog import BooksCatalog
from book_lib.books_catalog.book import Book


class TestBookCatalog(TestCase):
    def setUp(self):
        self.setUpValues = SetUpTest()
        self.test_book = self.setUpValues.single_test_book
        self.book_catalog = self.setUpValues.library

    def test_add_to_library(self):
        self.assertTrue(self.test_book, Book)

    def test_library_generator(self):
        test_generator = BooksCatalog([])
        test_generator.add_to_library(self.test_book)
        actual_result = self.book_catalog.library_generator
        expected_result = test_generator.library_generator
        self.assertTrue(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
