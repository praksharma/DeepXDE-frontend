import tkinter as tk
from tkinter import ttk

class PageManager:
    def __init__(self, master, nav_panel):
        self.master = master
        self.nav_panel = nav_panel  # This is the frame where navigation buttons will be placed
        self.pages = {}
        self.current_page = None

    def add_page(self, page_cls, title):
        # Create an instance of the page class
        page = page_cls(self.master)
        self.pages[page_cls] = page
        page.grid(row=1, column=0, sticky="nsew")  # Place it below the navigation panel, "nsew" ensures that the page expands to fill the given space

        # Create a navigation button for the page
        button = tk.Button(self.nav_panel, text=title, command=lambda: self.show_page(page_cls))
        # TODO: Set this to row col and pady for more space
        button.pack(side="left")  # Using pack for simplicity in horizontal button arrangement

    def show_page(self, page_cls):
        """
        Show the page corresponding to the given page class.
        """
        page = self.pages.get(page_cls)
        if page:
            if self.current_page:
                self.current_page.grid_remove()
            page.grid()
            self.current_page = page
            # Raise the current page to the top of the stacking order
            page.tkraise()
        else:
            print("Requested page not found. Please add the page first.")
