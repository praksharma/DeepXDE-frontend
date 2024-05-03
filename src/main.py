import tkinter as tk
from tkinter import ttk


from utils.menu import MenuManager

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DeepXDE Frontend")
        self.geometry("800x600")
        self.menu_manager = MenuManager(self)
        #self.main_tab_widget = MainTabs(self)
        #self.main_tab_widget.pack(fill=tk.BOTH, expand=True)

    def quit_app(self):
        self.quit()

        


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()