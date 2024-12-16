import tkinter as tk

from app.theme import *


class DoorFrame:
    def __init__(self, frame: tk.Frame):
        self.frame = frame
        self.action = DoorFrameAction()

    def content(self):
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
            font=FONT,
            command=self.action.door1_click
        )
        door_button2 = tk.Button(
            master=frame_doors,
            text="Door 2",
            bg=FOREGROUND,
            fg=BACKGROUND,
            font=FONT,
            command=self.action.door2_click
        )
        door_button3 = tk.Button(
            master=frame_doors,
            text="Door 3",
            bg=FOREGROUND,
            fg=BACKGROUND,
            font=FONT,
            command=self.action.door3_click
        )

        door_button1.grid(row=1, column=0, pady=5)
        door_button2.grid(row=2, column=0, pady=5)
        door_button3.grid(row=3, column=0, pady=5)

        # References
        self.action.door1 = door_button1
        self.action.door2 = door_button2
        self.action.door3 = door_button3


class DoorFrameAction:
    def __init__(self):
        self.state = {
            "door1": False,
            "door2": False,
            "door3": False
        }
        self.door1_pin = 0
        self.door2_pin = 2
        self.door3_pin = 4

    def __toggle(self, name: str):
        door = getattr(self, f'door{name[-1]}', None)
        if not door:
            print('Some error')
            return

        if self.state[name]:
            door.config(bg=FOREGROUND)
            self.state[name] = False
            self.close_door(name)
        else:
            door.config(bg='orange')
            self.state[name] = True
            self.open_door(name)

    def open_door(self, name: str):
        print(f'Opening door: {name}')

    def close_door(self, name: str):
        print(f'Closing door: {name}')

    def door1_click(self):
        self.__toggle('door1')

    def door2_click(self):
        self.__toggle('door2')

    def door3_click(self):
        self.__toggle('door3')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Door')
    root.geometry('500x300')
    root.configure(bg='#333333')

    frame = tk.Frame(
        master=root,
        bg='#333333'
    )
    door = DoorFrame(frame)
    door.content()

    frame.pack()
    root.mainloop()
