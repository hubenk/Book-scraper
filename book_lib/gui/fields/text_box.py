""" Module containing GUI's TextBox class """
import Tkinter as tk


class TextBox(tk.Frame):
    """
    TextBox class is used for displaying
    the scraped data
    """

    def __init__(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        """
        # ensure a consistent GUI size
        tk.Frame.__init__(self, **kwargs)
        self.grid_propagate(False)
        # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # create a Text widget
        self.txt = tk.Text(self)
        self.txt.grid(row=0, column=0, sticky="nsew")

        # create a Scrollbar and associate it with txt
        scroll = tk.Scrollbar(self, command=self.txt.yview)
        scroll.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scroll.set

    def clear(self):
        """ utility function to clear the text box """
        self.txt.delete('1.0', 'end')
