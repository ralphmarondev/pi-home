import tkinter as tk


class Home:
    def __init__(self, root: tk.Tk):
        self.root = root

    def say_hello(self):
        hello_label = tk.Label(
            self.root,
            text='Hello there,\nRalph Maron Eda is here!',
            bg='#333333',
            fg='#ffffff',
            font=('monospace', 24)
        )
        hello_label.pack(pady=20)
