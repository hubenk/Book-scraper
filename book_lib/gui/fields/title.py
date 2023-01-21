""" Module containing GUI's Title class """
import Tkinter as tk


class Title(object):
    """
        Title class is used for collecting the user input
        for title search within the GUI
        """

    def __init__(self, window):
        """
        :param window: Tk
        """
        self.__title_label = tk.Label(
            window,
            text="Title",
            font=('Arial', 10, 'bold')
        )
        self.__title_label.grid(
            row=3, column=0, padx=10, sticky="W")

        self.ttl_var = tk.StringVar()
        self.__title_text_box = tk.Entry(
            window,
            textvariable=self.ttl_var,
            relief="groove",
            width=20,
            font=('Arial', 12)
        )
        self.__title_text_box.grid(
            row=4, column=0, padx=10, sticky='W')
        self.__title_text_box.bind(
            "<Button-1>", lambda e: self.__title_text_box.delete(0, tk.END))
        # self.__title_text_box.insert('end', "Enter title: ")

    def retrieve_title(self):
        """ :return title string """
        return None \
            if len(self.__title_text_box.get()) == 0 \
            else self.__title_text_box.get().lower()
