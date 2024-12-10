import tkinter as tk

from theme import *


class MemberFrame:
    def __init__(self, frame: tk.Frame):
        self.frame = frame

    def member_content(self):
        frame_members = tk.Frame(master=self.frame, bg=BACKGROUND)
        frame_members.grid(row=0, column=1, sticky="nsew")
        frame_members.columnconfigure(0, weight=1)

        members_label = tk.Label(
            master=frame_members,
            text='Members',
            bg=BACKGROUND,
            fg=FOREGROUND,
            font=FONT
        )
        members_label.grid(row=0, column=0, pady=10)
        member_button1 = tk.Button(
            master=frame_members,
            text="Ralph Maron Eda",
            bg=FOREGROUND,
            fg=BACKGROUND,
            font=FONT
        )
        member_button2 = tk.Button(
            master=frame_members,
            text="Triesha Mae Olunan",
            bg=FOREGROUND,
            fg=BACKGROUND,
            font=FONT
        )
        member_button3 = tk.Button(
            master=frame_members,
            text="Jezlyn Cabbab",
            bg=FOREGROUND,
            fg=BACKGROUND,
            font=FONT
        )

        member_button1.grid(row=1, column=0, pady=5)
        member_button2.grid(row=2, column=0, pady=5)
        member_button3.grid(row=3, column=0, pady=5)
