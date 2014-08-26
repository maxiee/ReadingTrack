#!/usr/bin/env python
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import constants
import database
import time
import dlgnew

class OnReadingWindow(QWidget):
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

        self.giveup_button = QPushButton("Give Up")
        self.giveup_button.clicked.connect(self.give_up_pressed)
        self.finish_button = QPushButton("Finish")
        self.finish_button.clicked.connect(self.finish_pressed)

        # Init Layout
        main_layout = QVBoxLayout()

        top_one = QHBoxLayout()
        top_one.addStretch()
        top_one.addWidget(self.new_button)

        top_two = QVBoxLayout()
        top_two.addWidget(self.title_label)
        top_two.addWidget(self.add_date_label)
        top_two.addWidget(self.page_count_label)
        self.top_two_group = QGroupBox("Books on reading")
        self.top_two_group.setLayout(top_two)

        self.top_four = QHBoxLayout()
        self.top_four.addWidget(self.giveup_button)
        self.top_four.addStretch()
        self.top_four.addWidget(self.finish_button)
        self.top_four_widget = QWidget()
        self.top_four_widget.setLayout(self.top_four)

        # Add sub layouts and widgets to main_layout
        main_layout.addLayout(top_one)
        main_layout.addWidget(self.books_list)
        main_layout.addWidget(self.top_two_group)
        main_layout.addWidget(self.top_four_widget)

        # Set Layout
        self.setLayout(main_layout)

        # Set Title
        self.setWindowTitle("Reading Track")

        # Init database
        self.my_db = database.Database()

        # init
        self.init_booklist(constants.READING)

    def init_booklist(self, finished):
        self.books = self.my_db.get_books(finished)
        self.books_list.clear()
        for book in self.books:
            self.books_list.addItem(book[1])
        self.books_list.setFixedHeight(80)

    def get_status_message(self):
        return "Now you have " + \
                str(self.my_db.get_count()) + \
                " books on reading..."

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
        self.page_count_label.setText("Page count: " + str(book[3]))

    def give_up_pressed(self):
        current_selected = self.books_list.currentRow()
        self.my_db.remove_a_book(current_selected)
        self.init_booklist(constants.READING)

    def finish_pressed(self):
        finish_dialog = dlgfinish.FinishDialog()
        if finish_dialog.exec_() == QDialog.Accepted:
            current_selected = self.books_list.currentRow()
            if constants.DEBUG:
                #print("rank:" + str(finish_dialog.rank))
                #print("review:" + finish_dialog.review)
                print("[DEBUG]Current selected is " + str(current_selected))
            self.my_db.finished_read(
                    current_selected,
                    finish_dialog.rank,
                    finish_dialog.review)
            self.init_booklist(constants.READING)
