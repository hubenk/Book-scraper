from book_lib.communicator.communicator import Communicator

TEST_BOOK_DICT = {'available': 22, 'rating': 3,
                  'description': "It's hard to imagine a "
                                 "world without A Light in "
                                 "the Attic. This "
                                 "now-classic collection "
                                 "of poetry and drawings "
                                 "from Shel Silverstein "
                                 "celebrates its 20th "
                                 "anniversary with this "
                                 "special edition. "
                                 "Silverstein's humorous "
                                 "and creative verse can "
                                 "amuse the dowdiest of "
                                 "readers. Lemon-faced "
                                 "adults and fidgety kids "
                                 "sit still and read these "
                                 "rhythmic words and laugh "
                                 "and smile and love th "
                                 "It's hard to imagine a "
                                 "world without A Light in "
                                 "the Attic. This "
                                 "now-classic collection "
                                 "of poetry and drawings "
                                 "from Shel Silverstein "
                                 "celebrates its 20th "
                                 "anniversary with this "
                                 "special edition. "
                                 "Silverstein's humorous "
                                 "and creative verse can "
                                 "amuse the dowdiest of "
                                 "readers. Lemon-faced "
                                 "adults and fidgety kids "
                                 "sit still and read these "
                                 "rhythmic words and laugh "
                                 "and smile and love that "
                                 "Silverstein. Need proof "
                                 "of his genius? "
                                 "RockabyeRockabye baby, "
                                 "in the treetopDon't you "
                                 "know a treetopIs no safe "
                                 "place to rock?And who "
                                 "put you up there,"
                                 "And your cradle, "
                                 "too?Baby, "
                                 "I think someone down "
                                 "here'sGot it in for you. "
                                 "Shel, you never sounded "
                                 "so good. ...more",
                  'price-incl-tax': '51.77',
                  'in-stock': u'In stock (22 available)',
                  'price': 51.77, 'tax': '0.00',
                  'genre': 'Poetry',
                  'price-excl-tax': '51.77',
                  'title': 'A Light in the Attic',
                  'upc': u'a897fe39b1053632',
                  'reviews': u'0', 'product-type': 'Books'}

TEST_BOOK_RESPONSE = Communicator('https://books.toscrape.com/catalogue/'
                                  'a-light-in-the-attic_1000/index.html').get_single_response()
