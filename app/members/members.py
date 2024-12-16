import tkinter as tk

from app.theme import *


class MemberFrame:
    def __init__(self, frame: tk.Frame):
        self.frame = frame

    def content(self):
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

        members = [
            'Ralph Maron Eda',
            'Nympha Lebantino'
        ]
        for index, member in enumerate(members):
            member_label = tk.Label(
                master=frame_members,
                text=member,
                bg=BACKGROUND,
                fg=FOREGROUND,
                font=FONT
            )
            member_label.grid(row=index + 1, column=0, pady=5)
