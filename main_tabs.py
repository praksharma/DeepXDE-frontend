from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout #, QLabel
from tabs.Tab_0_Setup import Setup

class MainTabs(QWidget):
    """
    Add contents to the main tabs widget.

    """
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        # Setup the MainTabs layout
        self.layout()

        # Initialize main tab screen
        self.main_tabs()

        # Add widgets (main tab screen to the empty window)
        self.add_widgets()
        
        # Add contents in each tab
        self.setup = Setup(self.tab0) # here self.tab0 is passed as self to Setup class


    def layout(self):
        """
        A vertical layout has been added to the MainTabs widget. Anything we add will be added vertically.
        """
        self.layout = QVBoxLayout(self)

    def main_tabs(self):
        """
        Add any tabs that you want to display in the main screen.
        """

        self.tab = QTabWidget(self)

        # Setup the directory
        self.tab0 = QWidget(self)
        self.tab.addTab(self.tab0, "Setup")

        # Setup the geometry
        self.tab1 = QWidget(self)
        self.tab.addTab(self.tab1, "Geometry")

        # Setup the PDE and the constraints
        self.tab2 = QWidget(self)
        self.tab.addTab(self.tab2, "Problem")

        # Setup the PINN architecture
        self.tab3 = QWidget(self)
        self.tab.addTab(self.tab3, "Compile")

        # Training setup
        self.tab4 = QWidget(self)
        self.tab.addTab(self.tab4, "Training")

        # Print results 
        self.tab5 = QWidget(self)
        self.tab.addTab(self.tab5, "Results")

        # Codes for debugging
        # Add some contents to the first tab
        # if we use self here than the pyqt5 will get confused whether we are referring to overall Tab's layout or the layout inside this specific tab
        # self.tab1.layout = QVBoxLayout()
        # self.l = QLabel()
        # self.l.setText("This is the first tab")
        # self.tab1.layout.addWidget(self.l)
        # self.tab1.setLayout(self.tab1.layout)

    def add_widgets(self):
        """
        Add widgets to the layout.
        """

        self.layout.addWidget(self.tab)
        self.setLayout(self.layout)