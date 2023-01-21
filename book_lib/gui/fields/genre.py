""" Module containing GUI's Genre class"""
import Tkinter as tk


class Genre(object):
    """
    Genre class is used for collecting  the users preferred
    genre(S) input within the GUI
    """

    def __init__(self, window):
        """
        :param window: Tk
        """
        self.__genre_label = tk.Label(
            window,
            text="Genre(s)",
            font=('Arial', 10, 'bold')
        )
        self.__genre_label.grid(
            row=0, column=0, padx=10, sticky="W")

        self.__selected = tk.StringVar()
        self.selected = self.genres()[0]
        self.drop_menu = tk.OptionMenu(
            window,
            self.selected,
            *self.genres()
        )
        self.drop_menu.config(
            width=7,
            font=('Arial', 8),
            activebackground="#6c757d"
        )
        self.drop_menu.grid(
            row=1, column=0, padx=10, sticky='W')

        self.genre_var = tk.StringVar()
        self.__genre_text_box = tk.Entry(
            window,
            textvariable=self.genre_var,
            relief="groove",
            width=20,
            font=('Arial', 12)
        )
        self.__genre_text_box.bind(
            "<Button-1>", lambda e: self.__genre_text_box.delete(0, tk.END)
        )
        self.__genre_text_box.grid(
            row=2, column=0, padx=10, pady=3, sticky='W')

    @property
    def selected(self):
        """ :return StringVar from dropdown menu"""
        return self.__selected

    @selected.setter
    def selected(self, value):
        """ setter for selected genre """
        self.selected.set(value)

    def __selected_choice(self):
        """ :return the selected genre """
        return self.selected.get()

    def retrieve_genre(self):
        """ :returns either a specific genre from the dropdown menu
                     OR the user input from the entry,
                     or None, if nothing is selected or given
                     as a user input"""
        if self.__selected_choice() == "None":
            if len(''.join(self.__genre_text_box.get())) == 0:
                return
            else:
                return [genre.strip().lower()
                        for genre in self.__genre_text_box.get().split(',')]
        return [genre.strip().lower()
                for genre in self.__selected_choice().split(',')]

    @staticmethod
    def genres():
        """ utility method storing a tuple of genres """
        genres_tuple = (
            "None",
            "Travel",
            "Mystery",
            "Historical Fiction",
            "Sequential Art",
            "Classics",
            "Philosophy",
            "Romance",
            "Womens Fiction",
            "Fiction",
            "Childrens",
            "Religion",
            "Nonfiction",
            "Music",
            "Default",
            "Science Fiction",
            "Sports and Games",
            "Add a comment",
            "Fantasy",
            "New Adult",
            "Young Adult",
            "Science",
            "Poetry",
            "Paranormal",
            "Art",
            "Psychology",
            "Autobiography",
            "Parenting",
            "Adult Fiction",
            "Humor",
            "Horror",
            "History",
            "Food and Drink",
            "Christian Fiction",
            "Business",
            "Biography",
            "Thriller",
            "Contemporary",
            "Spirituality",
            "Academic",
            "Self Help",
            "Historical",
            "Christian",
            "Suspense",
            "Short Stories",
            "Novels",
            "Health",
            "Politics",
            "Cultural",
            "Erotica",
            "Crime",
        )
        return genres_tuple
