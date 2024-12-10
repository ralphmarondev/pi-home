import tkinter as tk

from theme import *


class Home:
    def __init__(self, root: tk.Tk):
        self.root = root

    def mainWindow(self):
        frame = tk.Frame(bg=BACKGROUND)
        frame.pack(fill=tk.X)  # fillMaxWidth() in kotlin

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        lights_label = tk.Label(
            master=frame,
            text='Lights',
            bg=BACKGROUND,
            fg=FOREGROUND,
            font=FONT
        )
        members_label = tk.Label(
            master=frame,
            text='Members',
            bg=BACKGROUND,
            fg=FOREGROUND,
            font=FONT
        )
        doors_label = tk.Label(
            master=frame,
            text='Doors',
            bg=BACKGROUND,
            fg=FOREGROUND,
            font=FONT
        )

        lights_label.grid(
            row=0,
            column=0,
            sticky=tk.EW
        )
        members_label.grid(
            row=0,
            column=1,
            sticky=tk.EW
        )
        doors_label.grid(
            row=0,
            column=2,
            sticky=tk.EW
        )
