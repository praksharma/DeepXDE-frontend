import tkinter as tk
from tkinter import ttk


from utils.menu import MenuManager
from PageManager import PageManager
from pages.Setup import SetupPage
from pages.Geometry import GeometryPage

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DeepXDE Frontend")
        self.geometry("800x600")

        # Load the image
        icon_image = tk.PhotoImage(file="media/home.png")
        # Set the image as the icon for the window
        self.iconphoto(True, icon_image)
        
        # Menu
        self.menu_manager = MenuManager(self)

        # Navigation Panel
        self.nav_panel = tk.Frame(self)
        self.nav_panel.grid(row=0, column=0, sticky="ew")
        
        # Pages
        self.page_manager = PageManager(self, self.nav_panel)

        # Add pages
        self.page_manager.add_page(SetupPage, "Setup")
        self.page_manager.add_page(GeometryPage, "Geometry")

        # Start with the Setup page
        #self.page_manager.show_page(SetupPage)
        self.page_manager.show_page(SetupPage)



    def quit_app(self):
        self.quit()

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()