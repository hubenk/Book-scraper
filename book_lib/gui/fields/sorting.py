""" Module containing GUI's Sorting class """
import Tkinter as tk

OPTIONS = (
    "Title",
    "Available",
    "Rating",
    "Price",
    "None"
)


class Sorting(object):
    """
        Sorting class is used for collecting  the users preferred
        sorting input within the GUI
    """

    def __init__(self, window):
        """
        :param window: Tk
        """
        self.genre_label = tk.Label(
            window,
            text="Sort by",
            font=('Arial', 10, 'bold')
        )
        self.genre_label.grid(
            row=14, column=0, padx=10, sticky="W")

        self.__selected = tk.StringVar()
        self.selected = OPTIONS[4]
        self.drop_menu = tk.OptionMenu(
            window,
            self.selected,
            *OPTIONS)
        self.drop_menu.config(
            width=7,
            font=('Arial', 8),
            activebackground="#6c757d"
        )
        self.drop_menu.grid(
            row=15, column=0, padx=10, sticky='W')

        self.__radio_var = tk.StringVar()
        self.radio_ascending = tk.Radiobutton(
            window,
            activebackground="#6c757d",
            text="  Ascending  ",
            variable=self.__radio_var,
            font=('Arial', 10),
            value='a', width=10)
        self.radio_ascending.grid(
            row=16, column=0, padx=10, sticky='W')

        self.radio_descending = tk.Radiobutton(
            window,
            activebackground="#6c757d",
            text="  Descending",
            variable=self.__radio_var,
            font=('Arial', 10),
            value='d', width=10)
        self.radio_descending.grid(
            row=17, column=0, padx=10, sticky='W')

    @property
    def selected(self):
        """ :return StringVar option for sorting """
        return self.__selected

    @selected.setter
    def selected(self, value):
        """ Setter for StringVar option for sorting """
        self.selected.set(value)

    def __selected_choice(self):
        """ :return selected option for sorting """
        return self.selected.get()

    def retrieve_sorting_data(self):
        """ :return a tuple containing the chosen sort,
         and optional ascending or descending option """
        return None \
            if self.__selected_choice() == 'None' \
            else (self.__selected_choice().lower(),
                  self.__radio_var.get())
