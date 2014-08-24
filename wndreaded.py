#!/usr/bin/env python
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import constants
import database
import dlgnew
import time

class ReadedWindow(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)

        # UI Widget
        self.new_button = QPushButton("New")
        self.new_button.clicked.connect(self.new_pressed)

        self.books_list = QListWidget()
        self.books_list.currentRowChanged[int].connect(self.book_list_item_selected)

        self.title_label = QLabel("Title:")
        self.add_date_label = QLabel("Add date:")
        self.page_count_label = QLabel("Page count:")
        self.finish_date_label = QLabel("Finished date:")
        self.rank_label = QLabel("Rank:")
        self.review_label = QLabel("Review:")

        # Init Layout
        main_layout = QVBoxLayout()

        top_one = QHBoxLayout()
        top_one.addStretch()
        top_one.addWidget(self.new_button)

        top_two = QVBoxLayout()
        top_two.addWidget(self.title_label)
        top_two.addWidget(self.add_date_label)
        top_two.addWidget(self.finish_date_label)
        top_two.addWidget(self.page_count_label)
        top_two.addWidget(self.rank_label)
        top_two.addWidget(self.review_label)
        self.top_two_group = QGroupBox("Books Finished Read")
        self.top_two_group.setLayout(top_two)

        # Add sub layouts and widgets to main_layout
        main_layout.addLayout(top_one)
        main_layout.addWidget(self.books_list)
        main_layout.addWidget(self.top_two_group)

        # Set Layout
        self.setLayout(main_layout)

        # Set Title
        self.setWindowTitle("Reading Track")

        # Init database
        self.my_db = database.Database()

        # init
        self.init_booklist(constants.READED)

    def init_booklist(self, finished):
        self.books = self.my_db.get_books(finished)
        self.books_list.clear()
        for book in self.books:
            self.books_list.addItem(book[1])
        self.books_list.setFixedHeight(50)

    def get_status_message(self):
        return "Now you have read " + \
                str(self.my_db.get_count()) + \
                " books!"

    def new_pressed(self):
        new_dlg = dlgnew.NewDialog()
        if new_dlg.exec_() == QDialog.Accepted:
            print("New dialog OK!")
            #print("New title is:" + new_dlg.title)
            #print("It has :" + new_dlg.pages)
            self.my_db.insert_a_book(new_dlg.title, new_dlg.pages)
            self.init_booklist(constants.READING)
        else:
            print("New dialog Cancel!")

    def book_list_item_selected(self, index):
        book = self.books[index]
        self.title_label.setText("Title: " + book[1])
        self.add_date_label.setText("Add date: " + time.ctime(book[2]))
        self.finish_date_label.setText("Finished date: " + time.ctime(book[4]))
        self.page_count_label.setText("Page count: " + str(book[3]))
        self.rank_label.setText("Rank: " + str(book[6]))
        self.review_label.setText("Review: " + book[7])

