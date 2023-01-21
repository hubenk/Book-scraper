""" Module containing GUI's Keywords class"""
import Tkinter as tk


class Keywords(object):
    """ Keywords class is used for collecting
    the users keywords input within the GUI"""

    def __init__(self, window):
        """
        :param window: Tk
        """
        self.__keywords_label = tk.Label(
            window,
            text="Keywords",
            font=('Arial', 10, 'bold')
        )
        self.__keywords_label.grid(
            row=9, column=0, padx=10, sticky="W")

        self.k_words = tk.StringVar()
        self.__keywords_text_box = tk.Entry(
            window,
            textvariable=self.k_words,
            relief="groove",
            width=20,
            font=('Arial', 12)
        )
        self.__keywords_text_box.grid(
            row=10, column=0, padx=10, sticky='W')

    def retrieve_keywords(self):
        """ :return a list of keywords """
        if len(''.join(self.__keywords_text_box.get())) == 0:
            return
        return [kw.strip().lower()
                for kw in self.__keywords_text_box.get().split(' ')]
