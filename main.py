#!/usr/bin/env python
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import bookmodel
import database
import dlgnew
import dlgfinish
import time
import constants

class Form(QWidget):
    def __init__(self, parent = None):
        super(Form, self).__init__(parent)

        # UI Widget
        self.presentation_combo = QComboBox()
        self.presentation_combo.addItem("Reading")
        self.presentation_combo.addItem("Finish Read")
        self.presentation_combo.currentIndexChanged[int].connect(self.presentation_combo_pressed)

        self.new_button = QPushButton("New")
        self.new_button.clicked.connect(self.new_pressed)

        self.books_list = QListWidget()
        self.books_list.currentRowChanged[int].connect(self.book_list_item_selected)

        self.title_label = QLabel("Title:")
        self.add_date_label = QLabel("Add date:")
        self.page_count_label = QLabel("Page count:")

        self.giveup_button = QPushButton("Give Up")
        self.giveup_button.clicked.connect(self.give_up_pressed)
        self.finish_button = QPushButton("Finish")
        self.finish_button.clicked.connect(self.finish_pressed)

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

        # Represent current is on reading or finish read
        self.current_page = constants.READING

        # Init database
        self.my_db = database.Database()

        # init
        self.init_booklist(constants.READING)
        self.init_status()

    def init_booklist(self, finished):
        self.books = self.my_db.get_books(finished)
        self.books_list.clear()
        for book in self.books:
            self.books_list.addItem(book[1])
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

    def presentation_combo_pressed(self, index):
        if index == self.current_page:
            return
        self.current_page = index
        if index == constants.READING:
            self.init_booklist(constants.READING)
            return
        if index == constants.READED:
            self.init_booklist(constants.READED)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Form()
    window.show()

    sys.exit(app.exec_())
