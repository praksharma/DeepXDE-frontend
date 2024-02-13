from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout , QLabel, QDialog, QPushButton, QTextBrowser
from tabs.Tab_0_Setup import Setup
from tabs.Tab_1_Geometry import Geometry

class MainTabs(QWidget):
    """
    Add contents to the main tabs widget.
    """
    def __init__(self, parent):
        super(QWidget, self).__init__()

        # Setup the MainTabs layout
        self.layout()

        # Initialize main tab screen
        self.main_tabs()

        # Add widgets (main tab screen to the empty window)
        self.add_widgets()
        
        # Add contents from each tab
        # Passing relevant tabs to each class
        self.setup = Setup(self.tab0)

        self.geometry = Geometry(self.tab1)


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

class WelcomeDialog(QDialog):
    """
    A dialog box for the welcome message at the startup.
    TODO: Add icons for email etc.
    """
    def __init__(self, parent):
        super(QWidget, self).__init__()

        # setup the title and dimensions
        self.setWindowTitle("About")
        self.setGeometry(100, 100, 300, 200)

        # Create a vertical layout to add stuff
        self.layout = QVBoxLayout(self)
        
        # Create an about text
        self.label = QLabel("Thanks for using the software.",self)
        self.layout.addWidget(self.label)

        # Create a textbox read-only for some basic info
        # Define your hyperlink using HTML
        self.github_hyperlink = '<a href="https://github.com/praksharma/DeepXDE-frontend">GitHub</a>'
        self.agpl_license_hyperlink = '<a href="https://www.gnu.org/licenses/agpl-3.0.en.html">AGPL license</a>'

        self.message = f"This is a frontend implementation of DeepXDE, licensed under the {self.agpl_license_hyperlink}.<br>You are allowed to use, modify and redistribute the software as per the terms of the AGPL license.<br>The source code is available on {self.github_hyperlink}."
        self.message_text_edit = QTextBrowser(self)
        self.message_text_edit.setReadOnly(True) # set to read only
        self.message_text_edit.setHtml(self.message)        
        self.message_text_edit.setOpenExternalLinks(True)

        # Create a close button
        self.button = QPushButton("Close", self)
        # Close the QDialog using the builtin close() method
        self.button.clicked.connect(self.close) 
        
        # Add the message textbox to the layout
        self.layout.addWidget(self.message_text_edit)

        # Add the widgets to the layout
        self.layout.addWidget(self.button)

        # Set the layout for the dialog box
        self.setLayout(self.layout)
