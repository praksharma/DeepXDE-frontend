from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QComboBox, QLineEdit, QPushButton, QFileDialog, QDialog, QTextEdit
import os
import configparser
from helpers import empty_label, gen_conf_file, problem_conf_file


# Remember
# self.setup = Setup(self.tab0) 
# here self.tab0 is passed as self to the Setup class

class Setup(QWidget):
    def __init__(self,parent) -> None:
        super(QWidget, self).__init__(parent)

        # Preliminary tasks
        # Read the workdir from the config file
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.workdir = os.path.expandvars(self.config['DEFAULT']['workdir'])

        # Project's config filename
        self.project_config = "project.ini"

        # Create a grid layout
        self.grid = QGridLayout(self)
        # spans the heading over all the columns
        self.grid.addWidget(QLabel('<p><span style="font-size:14px">Start with selecting suitable options to setup the model.</span></p>'), 0, 0, 1, 1)
        # how to span over entire row or column : https://stackoverflow.com/a/38332682/14598633 and https://stackoverflow.com/a/14337204/14598633
        # Here is QGridLayout example : https://www.bogotobogo.com/Qt/Qt5_GridLayout.php

        empty_label(self,  1, 0, 1, 1, 10)

        # Asking for dimension of the problem
        self.grid.addWidget(QLabel('Please select the dimension of the problem.'), 2, 0, 1, 1) # 3rd row 1st columns 


        # Create combobox to input dimension of the problem
        self.problem_dimension_comboBox()

        # Add the dimension combobox to the column 
        self.grid.addWidget(self.dimension_ComboBox, 2, 1, 1, 1) # 3rd row 3nd columns for more gap 
        
        empty_label(self,  3, 0, 1, 1, 10)
        
        # Asking for the working directory
        self.grid.addWidget(QLabel('Please browse the working directory.'), 4, 0, 1, 1) # 3rd row 1st columns 

        # Create workdir edit text
        self.workdir_editText()

        empty_label(self,  5, 0, 1, 1, 10)

        # Add the workdir edit text below the label
        self.grid.addWidget(self.workdir_editText, 6, 0, 1, 2)

        # Create pushbutton to browse the filesystem
        self.workdir_pushbutton()

        # Add pushbutton (next to the browsing label) to browse the filesystem
        self.grid.addWidget(self.workdir_browse_button, 4, 1, 1, 1)

        empty_label(self,  7, 0, 1, 1, 10)

        # Create pushbutton to create project directory and project config file
        self.project_directory_pushbutton()

        # Add pushbutton to create the project
        self.grid.addWidget(self.project_dir_button, 8, 0, 1, 1)

        empty_label(self,  9, 0, 1, 1, 10)

        # A pushbutton for module check textbox
        ##### Dynamically adding textedit messes with the layout
        # self.module_check_pushbutton = QPushButton("Check dependencies", self)
        # self.module_check_pushbutton.clicked.connect(self.check_modules)
        # self.grid.addWidget(self.module_check_pushbutton,8,0,1,1)
        
        # #Adding module check message
        self.grid.addWidget(QLabel('Dependency check. If there is an error please download the dependencies.'), 10, 0, 1, 1) # 3rd row 1st columns 
        self.check_modules()
        self.grid.addWidget(self.error_text_edit, 11, 0, 1, 2)



    def problem_dimension_comboBox(self):
        """
        Add Problem dimension combobox
        """
        self.dimension_ComboBox = QComboBox(self)
        self.dimension_ComboBox.addItems(["1 Dimensional (1D)", "2 Dimensional (2D)" , "3 Dimensional (3D)"])



    def workdir_pushbutton(self):
        """
        Add workdir browsing pushbutton
        """
        self.workdir_browse_button = QPushButton('Browse', self)
        self.workdir_browse_button.clicked.connect(self.browse_workdir) # connect to a callback function
    
    def browse_workdir(self):
        """
        Implement the browse_workdir function
        """
        self.dialog = QFileDialog()
        # allow directory selection only
        self.dialog.setFileMode(QFileDialog.DirectoryOnly)
        
        # Put the workdir in the workdir_editText
        if self.dialog.exec_() == QDialog.Accepted:
            self.workdir = self.dialog.selectedFiles()[0] + "/" # selected folder  # add / after the path
            self.workdir_editText.setText(self.workdir)
            # Update the conf file with the browsed directory
            gen_conf_file(self.workdir)

    def workdir_editText(self):
        """
        Add workdir edittext
        """
        self.workdir_editText = QLineEdit(self)
        self.workdir_editText.setText(os.path.expandvars(self.workdir))


    def project_directory_pushbutton(self):
        """
        A pushbutton to trigger the project directory check and config file creation.
        """
        self.project_dir_button = QPushButton('Create Project', self)
        self.project_dir_button.clicked.connect(self.create_project_directory) # connect to a callback function

    def create_project_directory(self):
        """
        A method to create project directory and populate the config files with basic details.
        """
        # Check if the workdir exists otherwise create one.
        #print(f"DEBUG: dimension = {self.dimension_ComboBox.currentIndex()+1}")
        if not os.path.exists(self.workdir):
            print("DEBUG : Workdir doesn't exist")
            # Create the directory
            os.makedirs(self.workdir)
            print("DEBUG : Workdir created")

            # create a config file with the dimension of the problem.
            # problem_conf_file(workdir, project_config, dimension_ComboBox current value)

            problem_conf_file(self.workdir, self.project_config, self.dimension_ComboBox.currentIndex())
            
            print("DEBUG : project.ini created")

        else: # if workdir exists
            print("DEBUG : Workdir already exists")
            # check if project.ini is already there
            if os.path.exists(self.workdir + self.project_config):
                print(f"The file '{self.project_config}' exists.")
                # TODO : Add function to read existing project.ini
                print("DEBUG :  Reading from project.ini is a TODO.\nDEBUG : Please use an empty directory")
            else: #if project.ini doesn't exist
                problem_conf_file(self.workdir, self.project_config, self.dimension_ComboBox.currentIndex())                
                print("DEBUG : project.ini created")




    def check_modules(self):
        """
        Checking for Pytorch, DeepXDE, numpy and matplotlib
        DeepXDE ships matplotlib, numpy, scikit-learn, scikit-optimize and scipy. So no need to check these.
        """
        self.moduleCheckTurnedOn = True
        self.flag = False
        self.error_message = "Checking modules\n"
        try:
            self.error_message = self.error_message + "Searching for DeepXDE...\n"
            import deepxde
            self.error_message = self.error_message + "DeepXDE found : version" + str(deepxde.__version__) + "\n"
        except ImportError:
            self.flag = True
            self.error_message = self.error_message + "Can't find DeepXDE.\n Please install DeepXDE.\n"

        try:
            self.error_message = self.error_message + "Searching for Pytorch...\n"
            import torch
            self.error_message = self.error_message + "Pytorch found : version" +str(torch.__version__) + "\n"
        except:
            self.flag = True
            self.error_message = self.error_message + "Can't find Pytorch.\n Please install Pytorch.\n"

        if self.flag:
            self.error_message = self.error_message + "Make sure you activate a correct Python environment.\n"
        else:
            self.error_message = self.error_message + "All modules have been found...\nYou are good to go :)"

        self.error_text_edit = QTextEdit(self)
        self.error_text_edit.setReadOnly(True) # set to read only
        self.error_text_edit.setText(self.error_message)
        #self.error_text_edit.setMinimumHeight(500)  # Sets the minimum height to 100 pixels
        # self.grid.addWidget(self.error_text_edit, 11, 0, 6, 2)
        # # self.error_text_edit.setFixedSize(400, 200)  # Adjust width and height as needed
        # self.adjustSize()
        # self.updateGeometry()