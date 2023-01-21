import unittest
from unittest import TestCase

from tests_package.unit_tests.input_values.set_up_test import SetUpTest


class TestBook(TestCase):
    def setUp(self):
        self.book = SetUpTest()

    def test_to_dict(self):
        expected_result = {
            "title": "Test_Name", "price": 101,
            "available": 21, "genre": "Drama",
            "rating": 3, "description": "Simple test description",
            "upc": "a897fe", "product type": "Test_book",
            "price_excl_tax": 99,
            "price_incl_tax": 304,
            "in_stock": 78, "tax": 201,
            "reviews": 5004}
        self.assertEqual(expected_result, self.book.single_test_book.to_dict)

    def test_title(self):
        expected_result = "Test_Name"
        self.assertEqual(expected_result, self.book.single_test_book.title)

    def test_price(self):
        expected_result = 101
        self.assertEqual(expected_result, self.book.single_test_book.price)

    def test_available(self):
        expected_result = 21
        self.assertEqual(expected_result, self.book.single_test_book.available)

    def test_description(self):
        expected_result = "Simple test description"
        self.assertEqual(expected_result, self.book.single_test_book.description)

    def test_genre(self):
        expected_result = "Drama"
        self.assertEqual(expected_result, self.book.single_test_book.genre)

    def test_rating(self):
        expected_result = 3
        self.assertEqual(expected_result, self.book.single_test_book.rating)

    def test_upc(self):
        expected_result = "a897fe"
        self.assertEqual(expected_result, self.book.single_test_book.upc)

    def test_product_type(self):
        expected_result = "Test_book"
        self.assertEqual(expected_result, self.book.single_test_book.product_type)

    def test_price_excl_tax(self):
        expected_result = 99
        self.assertEqual(expected_result, self.book.single_test_book.price_excl_tax)

    def test_price_incl_tax(self):
        expected_result = 304
        self.assertEqual(expected_result, self.book.single_test_book.price_incl_tax)

    def test_tax(self):
        expected_result = 201
        self.assertEqual(expected_result, self.book.single_test_book.tax)

    def test_in_stock(self):
        expected_result = 78
        self.assertEqual(expected_result, self.book.single_test_book.in_stock)

    def test_reviews(self):
        expected_result = 5004
        self.assertEqual(expected_result, self.book.single_test_book.reviews)


if __name__ == "__main__":
    unittest.main()
