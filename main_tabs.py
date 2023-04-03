from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QLabel

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

        # Add widgets
        self.add_widgets()
        


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

        self.tab1 = QWidget(self)
        self.tab.addTab(self.tab1, "Geometry")

        self.tab2 = QWidget(self)
        self.tab.addTab(self.tab2, "Constraints")

        self.tab3 = QWidget(self)
        self.tab.addTab(self.tab3, "Compile")

        self.tab4 = QWidget(self)
        self.tab.addTab(self.tab4, "Training")

        self.tab5 = QWidget(self)
        self.tab.addTab(self.tab5, "Results")

        # Add some contents to the first tab
        # if we use self here than the pyqt5 will get confused whether we are referring to overall Tab's layout or the layout inside this specific tab
        self.tab1.layout = QVBoxLayout()
        self.l = QLabel()
        self.l.setText("This is the first tab")
        self.tab1.layout.addWidget(self.l)
        self.tab1.setLayout(self.tab1.layout)

    def add_widgets(self):
        """
        Add widgets to the layout.
        """

        self.layout.addWidget(self.tab)
        self.setLayout(self.layout)