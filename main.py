""" Main """
import sys
from book_lib.gui.main_frame import MainFrame
from book_lib.router.router import Router

if __name__ == "__main__":
    ROUTER = Router()
    if '-X' in sys.argv:
        APP = MainFrame(ROUTER)
        APP.mainloop()
    else:
        ROUTER.start_app()
        ROUTER.print_result()
