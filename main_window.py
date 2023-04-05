import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QAction, QWidget, QVBoxLayout
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

        # By default the menubar and the main tabs will overlap each other. So we put them in separate widgets and then place thme in a predefined layout
        # However there is a warning that I've applied a layout multiple times.
        # If this warning creates a problem in future, we put the menubar and the main tabs in separate QWidgets with central alignment. 
        self.layout = QVBoxLayout(self)

        # Add menubar
        self.menu_bar()

        # Add widgets
        self.add_widgets()

        # Set the main window layout
        # The central widget is the area of the QMainWindow that is reserved for the main content of the application.
        # By default, a QMainWindow has an empty central widget, so you need to set it explicitly if you want to add content to the main window.
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        # Show the app
        self.show()

    def add_widgets(self):
        """
        Add widgets to the main window.
        """
        # Add main tabs
        self.main_tab_widget = MainTabs(self)
        #self.setCentralWidget(self.main_tab_widget) # centre widget

        self.layout.addWidget(self.main_tab_widget)


    def menu_bar(self):
        """
        Add a menu bar to the main window
        """
        # Add menu bar
        self.menu = QMenuBar(self)
        self.file_menu = self.menu.addMenu("File")
        self.about_menu = self.menu.addMenu("About")
        
        # A simple quit button with a quit action
        self.quit = QAction("Quit", self)
        self.quit.setShortcut("Ctrl+Q")
        self.file_menu.addAction(self.quit) 
        self.layout.addWidget(self.menu)

        # Close the program when quit menu is pressed
        self.quit.triggered.connect(self.close)

        # A simple quit button with a quit action
        self.about = QAction("About", self)
        self.about_menu.addAction(self.about) 
        self.layout.addWidget(self.menu)

        # Close the program when quit menu is clicked
        self.quit.triggered.connect(self.close)

        # Open about dialog box when about is clicked
        self.about.triggered.connect(self.showDialogBox) 

    def showDialogBox(self):
            # Create a new instance of the WelcomeDialog class
            welcome_dialog = WelcomeDialog(self)

            # Show the dialog
            welcome_dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = MyApp()
    sys.exit(app.exec_())