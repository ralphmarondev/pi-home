import tkinter as tk

from theme import *


# UI
class LightFrame:
    def __init__(self, frame: tk.Frame):
        self.frame = frame
        self.action = LightFrameAction()

    def light_content(self):
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
        self.action.light_button1 = light_button1
        self.action.light_button2 = light_button2
        self.action.light_button3 = light_button3


# UI States
class LightFrameAction:
    def __init__(self):
        self.action = LightRpiAction()
        self.states = {
            "light1": False,
            "light2": False,
            "light3": False
        }

    def __toggle_light(self, light_name):
        button = getattr(self, f'light_button{light_name[-1]}', None)
        if not button:
            print('Some error :>> so_cute_error :p')
            return

        if self.states[light_name]:
            button.config(bg=FOREGROUND)  # reset color to original
            self.states[light_name] = False
            print(f'{light_name.capitalize()} is turned OFF')
        else:
            button.config(bg='orange')  # change color
            self.states[light_name] = True
            print(f'{light_name.capitalize()} is turned ON')

        self.action.action_on_rpi(light_name)

    def light1_click(self):
        print('Light 1 is clicked')
        self.__toggle_light("light1")

    def light2_click(self):
        print('Light 2 is clicked')
        self.__toggle_light("light2")

    def light3_click(self):
        print('Light 3 is clicked')
        self.__toggle_light("light3")


# RPI states
class LightRpiAction:
    def __init__(self):
        pass

    def action_on_rpi(self, light_name):
        print(f'Configure rpi pin for: {light_name}')
        print()
