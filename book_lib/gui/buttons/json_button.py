""" Module containing GUI's JsonButton class"""
import Tkinter as tk
import tkFileDialog as fd

FILETYPES = (
    ('json files', '*.json'),
)


class JsonButton(object):
    """
    JsonButton class responsible for opening a json file,
    and performing a search/scrape based on the titles in it
    """

    def __init__(self, window, router):
        """
        :param window: Tk
        :param router: Router
        """
        self.router = router
        self.__json_label = tk.Label(
            window,
            text="Read from JSON",
            font=('Arial', 8, 'bold')
        )
        self.__json_label.grid(
            row=19, column=0, padx=10, pady=5, sticky="W")
        self.__json_button = tk.Button(
            window, width=10,
            activebackground="#6c757d",
            text='Open file',
            font=('Arial', 10),
            command=self.get_file_path
        )
        self.__json_button.grid(
            row=20, sticky="W", padx=10)
        self.__selected_text = tk.StringVar()
        self.__selected_label = tk.Label(
            window,
            font=('Arial', 10)
        )
        self.__selected_label.grid(
            row=20, sticky="W", padx=120)

    def get_file_path(self):
        """
        get the file path
        """
        filepath = fd.askopenfilename(filetypes=FILETYPES)
        self.router.arg_parser.json = filepath
        self.__selected_label['text'] = filepath.split('/')[-1]

    def clear_selected_label(self):
        """
        clear the label with the name of the last used file
        """
        self.__selected_label['text'] = ''
