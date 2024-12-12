import tkinter as tk


class ServoTest(tk.Tk):
    def __init__(self):
        super().__init__()
        self.action = ServoTestAction()

        self.title('Servo Test')
        self.configure(bg='#333333')
        self.geometry('500x300')
        self.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.content()

    def on_closing(self):
        self.destroy()

    def content(self):
        frame = tk.Frame(
            master=self,
            bg='#333333'
        )
        title_label = tk.Label(
            master=frame,
            text='Servo Test',
            bg='#333333',
            fg='#ffffff',
            font=('monospace', 16)
        )
        button = tk.Button(
            master=frame,
            text='CLICK ME',
            font=('monospace', 16),
            command=self.action.on_click
        )

        title_label.grid(row=0, column=0, pady=5)
        button.grid(row=1, column=0, pady=5)

        frame.pack()

        # REFERENCE
        self.action.button = button


class ServoTestAction:
    def __init__(self):
        self.state = {
            "button": False
        }

    def __toggle(self, name: str):
        button = getattr(self, 'button', None)
        if not button:
            print('Some error')
            return

        if self.state[name]:
            button.config(bg='#ffffff')
            self.state[name] = False
            self.turn_off()
        else:
            button.config(bg='orange')
            self.state[name] = True
            self.turn_on()

    def on_click(self):
        self.__toggle('button')

    def turn_on(self):
        # TODO: Open door [rotate servo]
        print('on')

    def turn_off(self):
        # TODO: Close door [rotate the servo back to its original angle]
        print('off')


if __name__ == '__main__':
    app = ServoTest()

    app.mainloop()
