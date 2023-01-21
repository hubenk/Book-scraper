""" Module containing Book class.

    Book's class is used for representation of a Book.
    """


class Book(object):
    """
    Book class responsible for representation of a Book
    """

    def __init__(self, title, price, available, description,
                 genre, rating, upc, product_type, price_excl_tax,
                 price_incl_tax, tax, in_stock, reviews):
        """
        :param title: Book's title
        :param price: Book's price
        :param available: In stock availability
        :param description: Book's description
        :param genre: Book's genre
        :param rating: Rating
        :param upc: Universal Product Code
        :param product_type: e.g. Book, magazine
        :param price_excl_tax: Price excluding tax
        :param price_incl_tax: Price including tax
        :param tax: Tax
        :param in_stock: In stock availability
        :param reviews: Number of reviews
        """
        self.__title = title
        self.__price = price
        self.__available = available
        self.__genre = genre
        self.__rating = rating
        self.__description = description
        self.__upc = upc
        self.__product_type = product_type
        self.__price_excl_t = price_excl_tax
        self.__price_incl_t = price_incl_tax
        self.__tax = tax
        self.__in_stock = in_stock
        self.__reviews = reviews

    def __str__(self):
        return """
        Title: {title}
        Price: {price}
        Availability: {available}
        Genre: {genre}
        Rating: {rating}
        UPC: {upc}
        Product Type: {product_type}
        Price Excl Tax: {price_excl}
        Price Incl Tax: {price_incl}
        Tax: {tax}
        In stock: {in_stock}
        Reviews: {reviews}
        Description: {desc}
        """.format(title=self.title, price=self.price,
                   available=self.available, genre=self.genre,
                   rating=self.rating, desc=self.description,
                   upc=self.upc, product_type=self.product_type,
                   price_excl=self.price_excl_tax, in_stock=self.in_stock,
                   price_incl=self.price_incl_tax, tax=self.tax,
                   reviews=self.reviews)

    @property
    def to_dict(self):
        """:return book as a dict"""
        return {
            "title": self.title, "price": self.price,
            "available": self.available, "genre": self.genre,
            "rating": self.rating, "description": self.description,
            "upc": self.upc, "product type": self.product_type,
            "price_excl_tax": self.price_excl_tax,
            "price_incl_tax": self.price_incl_tax,
            "in_stock": self.in_stock, "tax": self.tax,
            "reviews": self.reviews}

    @property
    def title(self):
        """:return: Book's title"""
        return self.__title

    @property
    def price(self):
        """:return: Book's price"""
        return self.__price

    @property
    def available(self):
        """:return: In stock availability"""
        return self.__available

    @property
    def description(self):
        """:return: Book's description"""
        return self.__description

    @property
    def genre(self):
        """:return: Book's genre"""
        return self.__genre

    @property
    def rating(self):
        """:return: Book's rating"""
        return self.__rating

    @property
    def upc(self):
        """:return: Universal Product code"""
        return self.__upc

    @property
    def product_type(self):
        """:return: Product type"""
        return self.__product_type

    @property
    def price_excl_tax(self):
        """:return: Book's price excluding tax"""
        return self.__price_excl_t

    @property
    def price_incl_tax(self):
        """:return: Book's price  including tax"""
        return self.__price_incl_t

    @property
    def tax(self):
        """:return: Tax"""
        return self.__tax

    @property
    def in_stock(self):
        """:return: In stock availability"""
        return self.__in_stock

    @property
    def reviews(self):
        """:return: Number of reviews"""
        return self.__reviews
