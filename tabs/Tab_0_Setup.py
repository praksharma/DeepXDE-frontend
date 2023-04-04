from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QComboBox, QLineEdit, QPushButton
import os
import configparser
from helpers import empty_label


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
        self.workdir = self.config['DEFAULT']['workdir']

        #### TODO : Put this is a QMessageBox.
        # # A big heading
        # self.layout = QVBoxLayout()
        # self.l = QLabel()
        # font1 = self.l.font()
        # font1.setPointSize(20)
        # self.l.setFont(font1)


        # self.l.setText("\nWelcome")
        # self.layout.addWidget(self.l)
        # self.setLayout(self.layout)

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
        self.grid.addWidget(self.dimension_ComboBox,2,1 ,1,1) # 3rd row 3nd columns for more gap 
        
        # Add an empty QLabel with suitable height to increase the gap
        self.empty_label = QLabel()
        self.empty_label.setFixedHeight(10) # set the height of the empty label as per your requirement
        self.grid.addWidget(self.empty_label, 3, 0, 1, 1)
        
        # Asking for the working directory
        self.grid.addWidget(QLabel('Please browse the working directory.'), 4, 0, 1, 1) # 3rd row 1st columns 

        # Create workdir edit text
        self.workdir_editText()

        # Add an empty QLabel with suitable height to increase the gap
        self.empty_label = QLabel()
        self.empty_label.setFixedHeight(10) # set the height of the empty label as per your requirement
        self.grid.addWidget(self.empty_label, 5, 0, 1, 1)

        # Add the workdir edit text below the label
        self.grid.addWidget(self.workdir_editText, 6, 0, 1, 2)





    def problem_dimension_comboBox(self):
        """
        Add Problem dimension combobox
        """
        self.dimension_ComboBox = QComboBox(self)
        self.dimension_ComboBox.addItems(["1 Dimensional (1D)", "2 Dimensional (2D)" , "3 Dimensional (3D)"])

    def workdir_editText(self):
        """
        Add workdir edittext
        """
        self.workdir_editText = QLineEdit(self)
        self.workdir_editText.setText(os.path.expandvars(self.workdir))
