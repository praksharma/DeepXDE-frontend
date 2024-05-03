import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class SetupPage(tk.Frame):
    def __init__(self, master):
        self.pad_height = 10

        super().__init__(master)
        top_frame = tk.Frame(self) # new frame
        top_frame.grid(row=0, column=0, sticky="ew")
        ttk.Label(top_frame, text="Setup Page").grid(row=0, column=0, pady=self.pad_height)

        self.dimension_dropdown()
        self.setup_working_dir()
    
    def dimension_dropdown(self):
        # FRAME ROW :1
        dimension_dropdown_frame = tk.Frame(self) # new frame
        dimension_dropdown_frame.grid(row=1, column=0, sticky="ew")

        ttk.Label(dimension_dropdown_frame, text="Dimension:").grid(row=0, column=0, sticky="e")

        # Adjust width of column 1 to create a gap between the label and the combobox
        dimension_dropdown_frame.columnconfigure(1, weight=1)  # By default, columns expand to fit the widest widget in that column.

        self.dimension_var = tk.StringVar(self)
        self.dimension_var.set("1D")  # Default value
        dimension_dropdown = ttk.Combobox(dimension_dropdown_frame, textvariable=self.dimension_var, values=["1D", "2D", "3D"])
        dimension_dropdown.grid(row=0, column=3, sticky="w")




    def setup_working_dir(self):
        # FRAME ROW: 2
        working_dir_frame = tk.Frame(self) # new frame
        working_dir_frame.grid(row=2, column=0, sticky="ew")

        ttk.Label(working_dir_frame, text="Setup Working Directory: ").grid(row=0, column=0, pady=self.pad_height, sticky="e")

        self.working_dir_var = tk.StringVar(self)
        self.working_dir_entry = ttk.Entry(working_dir_frame, textvariable=self.working_dir_var)
        self.working_dir_entry.grid(row=0, column=2)#, columnspan=2)

        working_dir_frame.columnconfigure(1, weight=1)  # Adjust column 1 to expand to fill the space
        working_dir_frame.columnconfigure(4, weight=1)

        browse_button = ttk.Button(working_dir_frame, text="Browse", command=self.browse_directory)
        browse_button.grid(row=0, column=5, padx=5)

    def browse_directory(self):
        """
        Opens a file dialog to browse and select a directory,
        then sets the selected directory path in the entry widget.
        """
        selected_dir = filedialog.askdirectory()
        if selected_dir:
            self.working_dir_var.set(selected_dir)
