import tkinter as tk

from theme import *


class DoorFrame:
    def __init__(self, frame: tk.Frame):
        self.frame = frame

    def door_content(self):
        frame_doors = tk.Frame(master=self.frame, bg=BACKGROUND)
        frame_doors.grid(row=0, column=2, sticky="nsew")
        frame_doors.columnconfigure(0, weight=1)

        doors_label = tk.Label(
            master=frame_doors,
            text='Doors',
            bg=BACKGROUND,
            fg=FOREGROUND,
            font=FONT
        )
        doors_label.grid(row=0, column=0, pady=10)

        door_button1 = tk.Button(
            master=frame_doors,
            text="Door 1",
            bg=FOREGROUND,
            fg=BACKGROUND,
            font=FONT
        )
        door_button2 = tk.Button(
            master=frame_doors,
            text="Door 2",
            bg=FOREGROUND,
            fg=BACKGROUND,
            font=FONT
        )
        door_button3 = tk.Button(
            master=frame_doors,
            text="Door 3",
            bg=FOREGROUND,
            fg=BACKGROUND,
            font=FONT
        )

        door_button1.grid(row=1, column=0, pady=5)
        door_button2.grid(row=2, column=0, pady=5)
        door_button3.grid(row=3, column=0, pady=5)
