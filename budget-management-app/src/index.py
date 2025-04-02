from tkinter import Tk
from ui.ui import UI
from repositories.user_repository import user_repository


def main():
    window = Tk()
    window.title("Budget application")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
