#!/usr/bin/env python
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import constants
import database
import time

class WndOnReadingOne(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
    
        # UI Widgets
        title_label = QLabel("书名:")
        self.title = QLabel("")

        current_reading_time = QLabel("当前阅读时间:")
        self.reading_time_hours = QLabel("00")
        reading_colon_1 = QLabel(":")
        self.reading_time_minutes = QLabel("00")
        reading_colon_2 = QLabel(":")
        self.reading_time_seconds = QLabel("00")

        book_finished_button = QPushButton("读完啦!")
        book_unfinished_button = QPushButton("读到这")

        # Init Layout
        main_layout = QVBoxLayout()

        top_one = QHBoxLayout()
        top_one.addWidget(title_label)
        top_one.addWidget(self.title)
        top_one.addStretch()

        top_two = QHBoxLayout()
        top_two.addWidget(current_reading_time)
        top_two.addStretch()

        top_three = QHBoxLayout()
        top_three.addStretch()
        top_three.addWidget(self.reading_time_hours)
        top_three.addWidget(reading_colon_1)
        top_three.addWidget(self.reading_time_minutes)
        top_three.addWidget(reading_colon_2)
        top_three.addWidget(self.reading_time_seconds)
        top_three.addStretch()

        top_four = QHBoxLayout()
        top_four.addStretch()
        top_four.addWidget(book_finished_button)
        top_four.addStretch()
        top_four.addWidget(book_unfinished_button)
        top_four.addStretch()

        main_layout.addLayout(top_one)
        main_layout.addLayout(top_two)
        main_layout.addLayout(top_three)
        main_layout.addLayout(top_four)

        # Set Layout
        self.setLayout(main_layout)
