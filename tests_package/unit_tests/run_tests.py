import unittest
from tests_package.unit_tests.engine_tests import test_engine
import test_book
import test_books_catalog
import test_communicator


if __name__ == "__main__":
    unittest.main(test_engine.SearchEngineTests)