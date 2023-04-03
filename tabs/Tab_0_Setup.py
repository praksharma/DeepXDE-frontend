from PyQt5.QtWidgets import QWidget, QFormLayout, QVBoxLayout, QLabel

# Remember
# self.setup = Setup(self.tab0) # here self.tab0 is passed as self to Setup class
class Setup(QWidget):
    def __init__(self,parent) -> None:
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout()
        self.l = QLabel()
        self.l.setText("This is the first tab")
        self.layout.addWidget(self.l)
        self.setLayout(self.layout)