import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

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

        # A maximised screen
        self.showMaximized()
        
        # Show the app
        self.show()

    def add_widgets(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = MyApp()
    sys.exit(app.exec_())