from PyQt5.QtWidgets import QLabel
import configparser


def gen_conf_file(workdir):
    """
    The code creates an ini file to store confgurations.
    the default workdir is $HOME/DeepXDE_simulations/
    """
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'workdir': workdir}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def empty_label(self, row , col, rowSpan, colSpan, height):
    """
    Add an empty label to put suitable gaps in the grid layout.

    Args:
        row (int): row number
        col (int): column number
        rowSpan (int): number of row span
        colSpan (int): number of col span
        height (int): height of the QLabel
    """
    # Add an empty QLabel with suitable height to increase the gap
    self.empty_label = QLabel()
    self.empty_label.setFixedHeight(height) # set the height of the empty label as per your requirement
    self.grid.addWidget(self.empty_label, row, col, rowSpan, colSpan)

