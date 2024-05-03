import tkinter as tk

class SetupPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Setup Page").pack()