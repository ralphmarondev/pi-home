import tkinter as tk

from config import Config
from home import Home


def main():
    print('Hello there, Ralph Maron Eda is here!')
    root = tk.Tk()
    root.title('Pi-Home')
    root.geometry('800x500')
    root.configure(bg='#333333')

    config = Config(root)
    config.set_fullscreen()
    config.toggle_fullscreen()

    home = Home(root)
    home.mainWindow()

    root.mainloop()


if __name__ == '__main__':
    main()
