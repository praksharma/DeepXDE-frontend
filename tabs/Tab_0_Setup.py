from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QComboBox, QLineEdit
import os

# Remember
# self.setup = Setup(self.tab0) 
# here self.tab0 is passed as self to the Setup class

class Setup(QWidget):
    def __init__(self,parent) -> None:
        super(QWidget, self).__init__(parent)

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

        grid = QGridLayout(self)
        # spans the heading over all the columns
        grid.addWidget(QLabel('<p><span style="font-size:14px">Start with selecting suitable options to setup the model.</span></p>'), 0, 0, 1, 0)
        # how to span over entire row or column : https://stackoverflow.com/a/38332682/14598633
        grid.addWidget(QLabel('\n'), 1, 0) # empty line
        
        # Asking for dimension of the problem
        grid.addWidget(QLabel('Please select the dimension of the problem.'), 2, 0) # 3rd row 1st columns 


        # Create combobox to input dimension of the problem
        self.problem_dimension_comboBox()

        # Add the dimension combobox to the column 
        grid.addWidget(self.dimension_ComboBox,2,2) # 3rd row 3nd columns for more gap 
        
        grid.addWidget(QLabel('\n'), 3, 0) # empty line
        
        # Asking for the working directory
        grid.addWidget(QLabel('Please browse the working directory.'), 4, 0) # 3rd row 1st columns 

        # Create workdir edit text
        self.workdir_editText()

        # Add the workdir edit text below the label
        grid.addWidget(self.e)




    def problem_dimension_comboBox(self):
        self.dimension_ComboBox = QComboBox(self)
        self.dimension_ComboBox.addItems(["1 Dimensional (1D)", "2 Dimensional (2D)" , "3 Dimensional (3D)"])

    def workdir_editText(self):
        self.editText = QLineEdit(self)
        self.editText.setText(os.path.expandvars(self.workdir))
