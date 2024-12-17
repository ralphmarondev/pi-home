import tkinter as tk

from app.light.light_action import *
from app.theme import *


class LightFrame:
    def __init__(self, frame: tk.Frame):
        self.frame = frame
        self.action = LightAction()

    def content(self):
        frame_lights = tk.Frame(master=self.frame, bg=BACKGROUND)
        frame_lights.grid(row=0, column=0, sticky="nsew")
        frame_lights.columnconfigure(0, weight=1)

        lights_label = tk.Label(
            master=frame_lights,
            text='Lights',
            bg=BACKGROUND,
            fg=FOREGROUND,
            font=FONT
        )
        lights_label.grid(row=0, column=0, pady=10)

        light_button1 = tk.Button(
            master=frame_lights,
            text="Light 1",
            bg=FOREGROUND,
            fg=BACKGROUND,
            font=FONT,
            command=self.action.light1_click
        )
        light_button2 = tk.Button(
            master=frame_lights,
            text="Light 2",
            bg=FOREGROUND,
            fg=BACKGROUND,
            font=FONT,
            command=self.action.light2_click
        )
        light_button3 = tk.Button(
            master=frame_lights,
            text="Light 3",
            bg=FOREGROUND,
            fg=BACKGROUND,
            font=FONT,
            command=self.action.light3_click
        )

        light_button1.grid(row=1, column=0, pady=5)
        light_button2.grid(row=2, column=0, pady=5)
        light_button3.grid(row=3, column=0, pady=5)

        # Store button references in the action object
        self.action.light1 = light_button1
        self.action.light2 = light_button2
        self.action.light3 = light_button3

    def start_thread(self):
        self.action.start()
