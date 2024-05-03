import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

class MenuManager:
    def __init__(self, master):
        self.master = master
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)
        self.create_file_menu()
        self.create_help_menu()

    def create_file_menu(self):
        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Quit", accelerator="Ctrl+Q", command=self.master.quit_app)

    def create_help_menu(self):
        help_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="License", command=self.show_license)
        help_menu.add_command(label="About", command=self.show_about_dialog)

    def show_about_dialog(self):
        messagebox.showinfo("About", "DeepXDE Frontend Version 1.0")
    
    def show_license(self):
        try:
            with open("../LICENSE", "r") as file:
                license_content = file.read()
            self.display_license_dialog(license_content)
        except FileNotFoundError:
            messagebox.showerror("Error", "LICENSE file not found.")
    
    def display_license_dialog(self, text):
        """
        Display the license text in a scrolled text dialog box.
        """
        dialog = tk.Toplevel(self.master)
        dialog.title("License")
        dialog.geometry("500x400")
        dialog.transient(self.master)  # Set to be on top of the main window

        text_widget = ScrolledText(dialog, wrap=tk.WORD)
        text_widget.pack(fill=tk.BOTH, expand=True)
        text_widget.insert(tk.END, text)
        text_widget.config(state=tk.DISABLED)  # Make the text read-only

        ok_button = tk.Button(dialog, text="OK", command=dialog.destroy)
        ok_button.pack(pady=10)