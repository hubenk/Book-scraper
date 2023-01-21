""" Module containing GUI's Filter class """
import Tkinter as tk

OPTIONS = (
    "Price",
    "Available",
    "Rating",
    "None"
)


class Filter(object):
    """
    Filter class used for collecting the users preferred
    filter input within the GUI
    """

    def __init__(self, window):
        """
        :param window: MainFrame
        """
        self.filter_label = tk.Label(
            window, text="Filter by",
            font=('Arial', 10, 'bold')
        )
        self.filter_label.grid(
            row=6, column=0, padx=10, sticky="W")

        self.__selected = tk.StringVar()
        self.selected = OPTIONS[3]
        self.drop_menu = tk.OptionMenu(
            window,
            self.selected,
            *OPTIONS)
        self.drop_menu.config(
            width=7, font=('Arial', 8),
            activebackground="#6c757d",
        )
        self.drop_menu.grid(
            row=6, column=0, padx=110, sticky='W')

        self.value = tk.StringVar()
        self.value.trace('w', self.check_value)
        self.value_to_compare = tk.Entry(
            window,
            textvariable=self.value,
            width=11,
            relief="groove",
            font=('Arial', 10)
        )
        self.value_to_compare.grid(
            row=7, column=0, padx=114, sticky='W')
        self.value_to_compare.bind(
            "<Button-1>", lambda e: self.value_to_compare.delete(0, tk.END))

        self.__operator_var = tk.StringVar()
        self.selected_operator = self.operations()[0]
        self.operations_menu = tk.OptionMenu(
            window,
            self.selected_operator,
            *self.operations())
        self.operations_menu.config(
            width=7,
            font=('Arial', 8),
            activebackground="#6c757d")
        self.operations_menu.grid(
            row=7, column=0, padx=10, sticky='W')

    def check_value(self, *args):
        """
        validate whether value is integer,
        and set's it to '0' if not

        :param args: necessary for dealing with
        Exception in Tkinter callback
        Traceback (most recent call last):
          File "...Tkinter.py", line 1547, in __call__
            return self.func(*args)
        TypeError: check_value() takes exactly 1 argument (4 given)

        """
        if not self.value.get().isdigit():
            print("Invalid input! Please enter an integer value!")
            self.value.set('0')

    @property
    def selected(self):
        """ :return selected option from filter drop down menu """
        return self.__selected

    @selected.setter
    def selected(self, value):
        """ setter for the filter option"""
        self.selected.set(value)

    def __selected_choice(self):
        """ :return the selected filter """
        return self.selected.get()

    @property
    def selected_operator(self):
        """ :return the selected operator StringVar"""
        return self.__operator_var

    @selected_operator.setter
    def selected_operator(self, value):
        """ setter for the operator """
        self.selected_operator.set(value)

    def __selected_operator(self):
        """ :return the selected operator """
        return self.selected_operator.get()

    def retrieve_filter_data(self):
        """
        :return: tuple containing the <filter> , <operator> and <value>
        """
        return None if self.__selected_choice() == 'None' \
                       or self.__selected_operator() == 'None' else (
            self.__selected_choice().lower(),
            self.__selected_operator(),
            int(self.value.get())
        )

    @staticmethod
    def operations():
        """ utility method for operations tuple"""
        operations_tuple = (
            'None',
            '>',
            '<',
            '=',
            '<=',
            '>='
        )
        return operations_tuple
