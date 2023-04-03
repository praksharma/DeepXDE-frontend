import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_tabs import MainTabs

class MyApp(QMainWindow):
    """
    The base class showing the main window. Initialises an empty window with some basic information such the title and the size of the window.

    ...

    Attributes
    ----------
    NONE

    Methods
    -------
    add_widgets()

    Add widgets in the empty window
    """
   
    def __init__(self):
        super().__init__()  # initialise super class

        # window title
        self.setWindowTitle("DeepXDE Frontend")

        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 600

        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # Add widgets
        self.add_widgets()

        # Show the app
        self.show()

    def add_widgets(self):
        """
        Add widgets to the main window.
        """
        self.main_tab_widget = MainTabs(self)
        self.setCentralWidget(self.main_tab_widget) # centre widget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = MyApp()
    sys.exit(app.exec_())