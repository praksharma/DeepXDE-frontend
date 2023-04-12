from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QComboBox,  QPushButton
import os
import configparser
from helpers import empty_label, gen_conf_file, problem_conf_file

# Remember
# self.setup = Setup(self.tab0) 
# here self.tab1 is passed as self to the Setup class

class Geometry(QWidget):
    def __init__(self,parent) -> None:
        super(QWidget, self).__init__(parent)

        pass