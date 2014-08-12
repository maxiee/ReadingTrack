from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Form(QWidget):
    def __init__(self, parent = None):
        super(Form, self).__init__(parent)

        # UI Widget
        self.presentation_combo = QComboBox()
        self.presentation_combo.addItem("Reading")
        self.presentation_combo.addItem("Reded")

        self.new_button = QPushButton("New")
        self.new_button.clicked.connect(self.new_pressed)

        # UI Layout
        top_one = QHBoxLayout()
        top_one.addWidget(self.presentation_combo)
        top_one.addStretch()
        top_one.addWidget(self.new_button)

        # Set Layout
        self.setLayout(top_one)

        # Set Title
        self.setWindowTitle("Reading Track")

    def new_pressed(self):
        pass

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Form()
    window.show()

    sys.exit(app.exec_())
