#!/usr/bin/env python
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import constants
import database
import time

class WndStatistics(QWidget):
    my_db = database.Database()

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        
        # Label: 已读书籍本数
        books = self.my_db.get_books(constants.MODE_HAVE_READ)
        have_read_label = QLabel("已读书籍"+str(len(books))+"本。")

        # 计算已读累计阅读时间
        time = 0
        for book in books:
            time += book[8]

        # Label: 在读书籍本数
        books = self.my_db.get_books(constants.MODE_READING)
        on_reading_label = QLabel("在读书籍"+str(len(books))+"本。")

        # 计算在读累计阅读时间，加到time里
        for book in books:
            time += book[8]

        # Label: 累计阅读时间
        total_time_label = QLabel(
                "累计阅读时间" + str(int(time/3600)) + "小时" + 
                str(int(time/60%6)) + "分钟。")
        # Init Layout
        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addWidget(have_read_label)
        main_layout.addStretch()
        main_layout.addWidget(on_reading_label)
        main_layout.addStretch()
        main_layout.addWidget(total_time_label)
        main_layout.addStretch()

        # Set Layout
        self.setLayout(main_layout)
