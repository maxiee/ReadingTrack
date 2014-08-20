#!/usr/bin/env python
from PyQt5.QtWidgets import *

class FinishDialog(QDialog):
    def __init__(self, parent = None):
        super(FinishDialog, self).__init__(parent)

        # UI widget
        rank_label = QLabel("Rank:")
        self.rank_combo = QComboBox()
        self.rank_combo.addItems(["1", "2", "3", "4", "5"])
        review_label = QLabel("Review:")
        self.review_edit = QTextEdit()
        finish_button = QPushButton("Finish")
        cancel_button = QPushButton("Cancel")

        # UI Layout
        layout = QGridLayout()
        layout.addWidget(rank_label, 0, 0)
        layout.addWidget(self.rank_combo, 0, 1)
        layout.addWidget(review_label, 1, 0)
        layout.addWidget(self.review_edit, 1, 1, 3, 3)
        layout.addWidget(finish_button, 4, 3)
        layout.addWidget(cancel_button, 4, 2)

        # Set Layout
        self.setLayout(layout)

        # Set title
        self.setWindowTitle("Rank the book")
