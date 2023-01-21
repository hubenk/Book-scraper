""" Module containing SearchEngine class. """
import re
from bs4 import BeautifulSoup
from book_lib.communicator.communicator import Communicator
from book_lib.books_catalog.books_catalog import Book

URL = {
    'home_page': "https://books.toscrape.com/",
    'catalogue_dir': "https://books.toscrape.com/catalogue/",
    'catalogue': "https://books.toscrape.com/catalogue/page-1.html",
    'categories': "https://books.toscrape.com/catalogue/category/books/",
    'start_page': 1,
    'end_page': 51,
}
SKIP_LINK = '/books_1/index.html'


class SearchEngine(object):
    """
    Class responsible for collecting data from a given website.
    """

    def __init__(self, library, book_count, filters=None):
        """
        :param library: An instance of BookCatalog passed by the Router
        :param arg_parser: Command line arguments
        ( .number = '-b' filter from command_line_arguments )
        :param filters: Instance of Filter class passed by Router
        """
        self.__library = library
        self.__filters = filters
        self.__book_count = book_count

    @staticmethod
    def get_catalog_pages(
            start_page=URL['start_page'], end_page=URL['end_page']):
        """
        Goes through all catalog pages and creates list of page links,
        passes it to Communicator and
        :returns: list of responses
        """
        # End page is not hard-coded. DEADLY SLOW!
        # links_pool = []
        # current_page = URL['start_page']
        # while Communicator("{catalog}page-{num}.html".format(
        #         catalog=URL['catalogue_dir'], num=current_page)
        # ).get_single_response().status_code == 200:
        #     links_pool.append("{catalog}page-{num}.html".format(
        #         catalog=URL['catalogue_dir'], num=current_page))

        links_pool = (
            "{catalog}page-{num}.html".format(
                catalog=URL['catalogue_dir'], num=p_num)
            for p_num in range(start_page, end_page))

        return Communicator(links_pool).get_responses()

    def get_category_pages(self, genre_list):
        """ Get category links and returns response
         via Communicator's get_responses method"""
        category_links = []
        response = Communicator(URL['home_page']).get_single_response()
        soup = BeautifulSoup(response.text, "lxml")
        categories = soup.find('div', class_='side_categories')

        for a_tag in categories.find_all('a', href=True):
            if not a_tag['href'].endswith(SKIP_LINK) \
                    and a_tag.text.strip().lower() in genre_list:
                category_links.append(URL['home_page']
                                      + a_tag['href'].rstrip('index.html'))
                for g_link in self.generate_inner_pages(category_links[-1]):
                    category_links.append(g_link)

        return Communicator(category_links).get_responses()

    @staticmethod
    def generate_inner_pages(link):
        """ Search and collects next pages links
        (Used by get_category_pages) """
        all_links = []
        response = Communicator(link).get_single_response()
        soup = BeautifulSoup(response.text, 'lxml')
        next_page = soup.find('li', class_='next')

        while next_page:
            yield link + next_page.find('a')['href']
            all_links.append(link + next_page.find('a')['href'])
            response = Communicator(all_links[-1]).get_single_response()
            soup = BeautifulSoup(response.text, 'lxml')
            next_page = soup.find('li', class_='next')

    @staticmethod
    def extract_book_links(page_responses):
        """
        Takes all book links in a given page,
        collects them in a list, passes it to the Communicator and
        :returns: a list of responses
        """
        book_links = []
        for page in page_responses:
            soup = BeautifulSoup(page.text, 'lxml')
            page_info = soup.find_all(
                'li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
            for link in page_info:
                temp = URL['catalogue_dir'] + link.find('a').get('href')
                temp = temp.replace('../../../', '')
                book_links.append(temp)

        return Communicator(book_links).get_responses()

    def fetch_book_data(self, book_responses, filters=None):
        """
        Take the data from the links,
        apply filters (if any) and constructs dictionaries.
        :returns: list of book dictionaries
        """
        books = []

        for book in book_responses:
            soup = BeautifulSoup(book.content, 'lxml')

            if filters and not filters.apply_filters(soup):
                continue

            book_data = {
                'title': self.get_title(soup),
                'price': self.get_price(soup),
                'available': self.get_availability(soup),
                'description': self.get_description(soup),
                'genre': self.get_genre(soup),
                'rating': self.get_rating(soup),
                'upc': self.get_upc(soup),
                'product-type': self.get_product_type(soup),
                'price-excl-tax': self.get_price_excl_tax(soup),
                'price-incl-tax': self.get_price_incl_tax(soup),
                'tax': self.get_tax(soup),
                'in-stock': self.get_stock(soup),
                'reviews': self.get_reviews(soup),
            }
            books.append(book_data)

        return books

    def __save_book(self, books, count=None):
        """
        Save book in BookCatalog structure.
        """
        for book in books:
            if count and len(self.library.library) >= count:
                return
            new_book = Book(book['title'], book['price'],
                            book['available'], book['description'],
                            book['genre'], book['rating'],
                            book['upc'], book['product-type'],
                            book['price-excl-tax'], book['price-incl-tax'],
                            book['tax'], book['in-stock'],
                            book['reviews'])
            self.library.add_to_library(new_book)

    def scrape_catalog(self, genre=None, filters=None):
        """
        * Page by page *
        Creates Book object from book_data elements and saves it in BookCatalog
        """
        if genre is not None:
            pages = self.get_category_pages(genre)
            book_links = self.extract_book_links(pages)
            book_data = self.fetch_book_data(book_links, filters=filters)
            self.__save_book(book_data, count=self.book_count)
        else:
            if self.book_count and self.book_count > 0:
                start_page = URL['start_page']
                while len(self.library.library) < self.book_count:
                    end_page = start_page + 1
                    if end_page > URL['end_page']:
                        break
                    pages = self.get_catalog_pages(
                        start_page=start_page, end_page=end_page)
                    book_links = self.extract_book_links(pages)
                    book_data = self.fetch_book_data(
                        book_links, filters=filters
                    )
                    self.__save_book(book_data, count=self.book_count)
                    start_page += 1
            else:
                pages = self.get_catalog_pages()
                book_links = self.extract_book_links(pages)
                book_data = self.fetch_book_data(book_links, filters=filters)
                self.__save_book(book_data, count=self.book_count)

    @property
    def library(self):
        """ :return: book's catalog library """
        return self.__library

    @property
    def filters(self):
        """ :return: filters """
        return self.__filters

    @property
    def book_count(self):
        """ :return: count """
        return self.__book_count

    @book_count.setter
    def book_count(self, value):
        self.__book_count = value

    @staticmethod
    def get_title(soup):
        """ :return: (str) book's title """
        return soup.find("h1").text.encode('utf-8')

    @staticmethod
    def get_price(soup):
        """ :return: (float) book's price """
        return float(soup.find('p', class_='price_color').get_text()[1:])

    @staticmethod
    def get_availability(soup):
        """ :return: (int) book's availability """
        return int(re.search(r'\d+', soup.find(
            'p', class_='instock availability').get_text()).group())

    @staticmethod
    def get_description(soup):
        """ :return: (str) book's description """
        return soup.select('article p', class_=False)[3].text.encode('utf-8')

    @staticmethod
    def get_genre(soup):
        """ :return: (str) book's genre """
        return soup(
            href=re.compile(r'/category/books/'))[0].text.encode('utf-8')

    @staticmethod
    def get_rating(soup):
        """ :return: (int) book's rating """
        word_rating = soup.find(
            class_="star-rating").get_attribute_list("class")[-1]
        ratings = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        return ratings[word_rating]

    @staticmethod
    def get_upc(soup):
        """ :return: (str) product UPC """
        return soup.find('td', class_=False).text

    @staticmethod
    def get_product_type(soup):
        """ :return: (str) product type """
        return soup('td')[1].text.encode('utf-8')

    @staticmethod
    def get_price_excl_tax(soup):
        """ :return: (str) price excluding tax  """
        return soup('td')[2].text[1:].encode('utf-8')

    @staticmethod
    def get_price_incl_tax(soup):
        """ :return: (str) price including tax  """
        return soup('td')[3].text[1:].encode('utf-8')

    @staticmethod
    def get_tax(soup):
        """ :return: (str) product tax """
        return soup('td')[4].text[1:].encode('utf-8')

    @staticmethod
    def get_stock(soup):
        """ :return: (str) product in stock """
        return soup('td')[5].text

    @staticmethod
    def get_reviews(soup):
        """ :return: (str) product reviews """
        return soup('td')[6].text
