from home import Home
import tkinter as tk

def main():
    print('Hello there, Ralph Maron Eda is here!')
    root = tk.Tk()
    root.title('Pi-Home')
    root.geometry('500x300')
    root.configure(bg='#333333')

    home = Home(root)
    home.say_hello()

    root.mainloop()


if __name__ == '__main__':
    main()
