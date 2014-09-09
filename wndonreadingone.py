#!/usr/bin/env python
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import constants
import database
import time
from threading import Timer

class WndOnReadingOne(QWidget):
    book_id = -1
    # Init database
    my_db = database.Database()
    timer_update_signal = pyqtSignal()
    read_here_signal = pyqtSignal([int])

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
        book_unfinished_button.clicked.connect(self.unfinished_pressed)

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

        # 初始化定时器
        self.timer = Timer(1, self.timer_update)
        self.second = 0
        self.timer_update_signal.connect(self.update_widgets)
        self.timer.start()

    def init_book_title(self):
        self.title.setText(self.my_db.get_book(self.book_id))
        print(self.my_db.get_book(self.book_id))

    def timer_update(self):
        self.timer_update_signal.emit()
        self.timer = Timer(1, self.timer_update)
        self.timer.start()
        self.second += 1

    def update_widgets(self):
        #print("ouch!")
        self.reading_time_seconds.setText(str(int(self.second)))
        self.reading_time_minutes.setText(str(int(self.second/60)))
        self.reading_time_hours.setText(str(int(self.second/3600)))

    def unfinished_pressed(self):
        read_time = self.my_db.get_read_time(self.book_id)
        print(read_time)
        read_time += self.second
        self.timer.cancel()
        self.my_db.update_read_time(read_time, self.book_id)
        self.read_here_signal.emit(1)
