import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QAction, QWidget, QVBoxLayout
from PyQt5 import QtGui
from main_tabs import MainTabs, WelcomeDialog
from helpers import gen_conf_file

class MyApp(QMainWindow):
    """
    The base class showing the main window. Initialises an empty window with some basic information such the title and the size of the window.
    ...

    Methods
    -------
    add_widgets()

    Add widgets in the empty window
    """
   
    def __init__(self):
        super().__init__()  # initialise super class

        # Set frontend icon
        self.setWindowIcon(QtGui.QIcon('home.png'))

        # set default workdir to home
        self.workdir = '$HOME/DeepXDE_simulations/'
        gen_conf_file(self.workdir)
         
        # window title
        self.setWindowTitle("DeepXDE Frontend")

        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 600

        self.setGeometry(self.left, self.top, self.width, self.height)

        """
        By default the menubar and the main tabs will overlap each other. So we put them in separate widgets and then place thme in a predefined layout
        However there is a warning that I've applied a layout multiple times.
        If this warning creates a problem in future, we put the menubar and the main tabs in separate QWidgets with central alignment. 
        Okay, there are spacing issues and a warning which might create problem later on.
        Thus, I am using two seperate QWidgets to get rid of them.
        """

        # Add menubar
        self.menu_bar()

        # Add widgets
        self.add_widgets()

        # Show the app
        self.show()

    def add_widgets(self):
        """
        Add widgets to the main window.
        """
        # Add main tabs
        self.main_tab_widget = MainTabs(self)

        # Create a container for the tabs widget
        self.tabs_container = QWidget(self)
        self.tabs_layout = QVBoxLayout(self.tabs_container)
        self.tabs_layout.addWidget(self.main_tab_widget)

        # Set the central widget to the tabs container
        """
        Set the main window layout
        The central widget is the area of the QMainWindow that is reserved for the main content of the application.
        By default, a QMainWindow has an empty central widget, so you need to set it explicitly if you want to add content to the main window.
        """
        self.setCentralWidget(self.tabs_container)


    def menu_bar(self):
        """
        Add a menu bar to the main window
        Note: a menu doesn't need setCentralWidget method as it is done by default.
        """
        # Add menu bar
        self.menu = QMenuBar(self)
        self.file_menu = self.menu.addMenu("File")
        self.about_menu = self.menu.addMenu("About")
        
        # A simple quit button with a quit action
        self.quit = QAction("Quit", self)
        self.quit.setShortcut("Ctrl+Q")
        self.file_menu.addAction(self.quit) 

        # Close the program when quit menu is pressed
        self.quit.triggered.connect(self.close)

        # A simple quit button with a quit action
        self.about = QAction("About", self)
        self.about_menu.addAction(self.about) 

        # Close the program when quit menu is clicked
        self.quit.triggered.connect(self.close)

        # Open about dialog box when about is clicked
        self.about.triggered.connect(self.showDialogBox)

        # Create a container for the menu bar
        self.menu_container = QWidget(self)
        self.menu_layout = QVBoxLayout(self.menu_container)
        self.menu_layout.setContentsMargins(0, 0, 0, 0)
        self.menu_layout.addWidget(self.menu)

        # Add the menu container to the main window
        self.setMenuBar(self.menu)

    def showDialogBox(self):
            # Create a new instance of the WelcomeDialog class
            welcome_dialog = WelcomeDialog(self)

            # Show the dialog
            welcome_dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = MyApp()
    sys.exit(app.exec_())