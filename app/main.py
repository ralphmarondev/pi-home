import tkinter as tk

from app.config import Config
from app.door.doors import DoorFrame
from app.light.lights import LightFrame
from app.members.members import MemberFrame
from theme import *
from utils.app_thread import AppThread


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.top_app_bar()
        self.content()
        self.bottom_app_bar()

    def top_app_bar(self):
        top_bar = tk.Frame(
            master=self,
            bg="#5E3B8E",
            height=40
        )
        top_bar.pack(fill=tk.X, side=tk.TOP)
        header_label = tk.Label(
            master=top_bar,
            text="Capstone Project",
            fg="#ffffff",
            bg='#5E3B8E',
            font=('monospace', 16)
        )
        header_label.pack(padx=10, pady=5)

    def content(self):
        frame = tk.Frame(bg=BACKGROUND)
        frame.pack(fill=tk.BOTH, expand=True)  # fillMaxSize() on kotlin

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        light = LightFrame(frame)
        member = MemberFrame(frame)
        door = DoorFrame(frame)

        light.content()
        member.content()
        door.content()

    def bottom_app_bar(self):
        copyright_label = tk.Label(
            master=self,
            text="BSCPE 2024",
            font=('monospace', 10),
            bg='#DCD0FF',
            fg='#333333'
        )
        copyright_label.pack(side=tk.BOTTOM, fill=tk.X)


if __name__ == '__main__':
    app = App()

    app.title('PiHome')
    app.geometry('500x300')

    config = Config(app)
    config.set_fullscreen()
    config.toggle_fullscreen()

    app_thread = AppThread()
    app_thread.start()


    def on_close():
        app_thread.stop()
        app.destroy()


    app.protocol("WM_DELETE_WINDOW", on_close)
    app.mainloop()
