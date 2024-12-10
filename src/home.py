import tkinter as tk

from doors import DoorFrame
from lights import LightFrame
from members import MemberFrame
from theme import *


class Home:
    def __init__(self, root: tk.Tk):
        self.root = root

    def mainWindow(self):
        frame = tk.Frame(bg=BACKGROUND)
        frame.pack(fill=tk.X)  # fillMaxWidth() on kotlin

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        lights = LightFrame(frame)
        members = MemberFrame(frame)
        doors = DoorFrame(frame)

        lights.light_content()
        members.member_content()
        doors.door_content()
