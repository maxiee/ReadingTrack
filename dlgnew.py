#!/usr/bin/env python
from PyQt5.QtWidgets import *

class NewDialog(QDialog):
    def __init__(self, parent = None):
        super(NewDialog, self).__init__(parent)

        # UI widget
        title_label = QLabel("Book title:")
        self.title_edit = QLineEdit()
        pages_label = QLabel("Total pages")
        self.pages_edit = QLineEdit()
        ok_button = QPushButton("Ok")
        ok_button.clicked.connect(self.ok_pressed)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.cancel_pressed)

        # UI layout
        layout = QGridLayout()
        layout.addWidget(title_label, 0, 0)
        layout.addWidget(self.title_edit, 0, 1, 1, 2)
        layout.addWidget(pages_label, 1, 0)
        layout.addWidget(self.pages_edit, 1, 1, 1, 2)
        layout.addWidget(ok_button, 2, 0)
        layout.addWidget(cancel_button, 2, 2)

        # Set layout
        self.setLayout(layout)

        # Set title
        self.setWindowTitle("New Reading Task")

        # variables
        self.title = ""
        self.pages = ""

    def ok_pressed(self):
        self.title = self.title_edit.text()
        self.pages = self.pages_edit.text()
        if self.title == "" or self.pages == "":
            QMessageBox.warning(self, "Empty field", 
                    "Please enter a title and its pages!")
            return
        self.accept()

    def cancel_pressed(self):
        self.reject()
