#!/usr/bin/env python
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import bookmodel
import database
import dlgnew
import time

class Form(QWidget):
    def __init__(self, parent = None):
        super(Form, self).__init__(parent)

        # UI Widget
        self.presentation_combo = QComboBox()
        self.presentation_combo.addItem("Reading")
        self.presentation_combo.addItem("Finish Read")

        self.new_button = QPushButton("New")
        self.new_button.clicked.connect(self.new_pressed)

        self.books_list = QListWidget()
        self.books_list.currentRowChanged[int].connect(self.book_list_item_selected)

        self.title_label = QLabel("Title:")
        self.add_date_label = QLabel("Add date:")
        self.page_count_label = QLabel("Page count:")

        self.giveup_button = QPushButton("Give Up")
        self.finish_button = QPushButton("Finish")

        self.status_info = QLabel()


        # UI Layout
        main_layout = QVBoxLayout()

        top_one = QHBoxLayout()
        top_one.addWidget(self.presentation_combo)
        top_one.addStretch()
        top_one.addWidget(self.new_button)

        top_two = QVBoxLayout()
        top_two.addWidget(self.title_label)
        top_two.addWidget(self.add_date_label)
        top_two.addWidget(self.page_count_label)
        top_two_group = QGroupBox("Book on reading")
        top_two_group.setLayout(top_two)

        top_three = QHBoxLayout()
        top_three.addWidget(self.giveup_button)
        top_three.addStretch()
        top_three.addWidget(self.finish_button)


        # Add sub layouts and widgets to main_layout
        main_layout.addLayout(top_one)
        main_layout.addWidget(self.books_list)
        main_layout.addWidget(top_two_group)
        main_layout.addLayout(top_three)
        main_layout.addWidget(self.status_info)

        # Set Layout
        self.setLayout(main_layout)

        # Set Title
        self.setWindowTitle("Reading Track")

        # Init database
        self.my_db = database.Database()

        # init
        self.init_booklist()
        self.init_status()

    def init_booklist(self):
        self.books = self.my_db.get_books(0)
        self.books_list.clear()
        for book in self.books:
            self.books_list.addItem(book[0])
        self.books_list.setFixedHeight(50)

    def init_status(self):
        self.status_info.setText("Now you have " + 
                str(self.my_db.get_count()) + 
                " books on reading...")

    def new_pressed(self):
        new_dlg = dlgnew.NewDialog()
        if new_dlg.exec_() == QDialog.Accepted:
            print("New dialog OK!")
            #print("New title is:" + new_dlg.title)
            #print("It has :" + new_dlg.pages)
            self.my_db.insert_a_book(new_dlg.title, new_dlg.pages)
            self.init_booklist()
        else:
            print("New dialog Cancel!")

    def book_list_item_selected(self, index):
        book = self.books[index]
        self.title_label.setText("Title: " + book[0])
        self.add_date_label.setText("Add date: " + time.ctime(book[1]))
        self.page_count_label.setText("Page count: " + str(book[2]))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Form()
    window.show()

    sys.exit(app.exec_())
