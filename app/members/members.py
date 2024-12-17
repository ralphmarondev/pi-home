import tkinter as tk

from app.theme import *


class MemberFrame:
    def __init__(self, frame: tk.Frame):
        self.frame = frame
        self.members = [
            'Ralph Maron Eda',
            'Nympha Lebantino',
            'Elisha Macalanda',
            'Jhaymark Basa',
            'Mark John Germinal',
            'Glenn Kylle Fronda',
            'Kurt Estorquia',
            'Ivan Rosini',
            'Triesha Mae Olunan',
            'Joanna Saballero',
            'Shanlei Cabbab',
            'Jezlyn Cabbab',
            'Neal Mabborang',
            'Jack Cabigayan',
            'Hannah Joyce Carag',
            'Ariel Annunciacon',
            'Joseph Aguinaldo',
            'Rhea Oloraza',
            'Pauline Dumlao',
            'Angel Apay',
            'Jamaica Quizzaga',
            'Jaylord Agub',
            'Marylitte Capistrano'
        ]

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

        for index, member in enumerate(self.members[:2]):
            member_label = tk.Label(
                master=frame_members,
                text=member,
                bg=BACKGROUND,
                fg=FOREGROUND,
                font=FONT
            )
            member_label.grid(row=index + 1, column=0, pady=5)

        see_all_button = tk.Button(
            master=frame_members,
            text="See All",
            command=self.show_all_members,
            bg="#D8BFD8",
            fg="black"
        )
        see_all_button.grid(row=len(self.members) + 1, column=0, pady=5)

    def show_all_members(self):
        small_window = tk.Toplevel(self.frame)
        small_window.title("All Members")
        small_window.resizable(False, False)

        # Ensure the main window has been rendered
        self.frame.update_idletasks()

        # Get the position
        x = self.frame.winfo_rootx()
        y = self.frame.winfo_rooty()

        # Get the dimension
        frame_width = self.frame.winfo_width()
        frame_height = self.frame.winfo_height()

        window_width = 250
        window_height = 200

        # Calculate the position to center the window
        position_top = y + int((frame_height - window_height) / 2)
        position_left = x + int((frame_width - window_width) / 2)
        small_window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

        tk.Label(small_window, text="Team Members", font=("monospace", 12, "bold")).pack(pady=5)

        canvas = tk.Canvas(small_window)
        scrollbar = tk.Scrollbar(small_window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        member_frame = tk.Frame(canvas)
        for index, member in enumerate(self.members):
            tk.Label(member_frame, text=member, font=("monospace", 10)).pack(anchor="w", padx=10)

        canvas.create_window((0, 0), window=member_frame, anchor="nw")

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        member_frame.update_idletasks()  # Ensure that the frame is fully packed before updating scroll region
        canvas.config(scrollregion=canvas.bbox("all"))

        tk.Button(small_window, text="Close", command=small_window.destroy).pack(pady=10)
