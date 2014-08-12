from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import bookmodel
import time

class Form(QWidget):
    def __init__(self, parent = None):
        super(Form, self).__init__(parent)

        # Test: Suppose we have 3 books
        books = [
                bookmodel.Book("Book 1", time.time(), 0, 350, 0, False),
                bookmodel.Book("Book 2", time.time(), 0, 400, 0, False),
                bookmodel.Book("Book 3", time.time(), 0, 450, 0, False)]

        # UI Widget
        self.presentation_combo = QComboBox()
        self.presentation_combo.addItem("Reading")
        self.presentation_combo.addItem("Finish Read")

        self.new_button = QPushButton("New")
        self.new_button.clicked.connect(self.new_pressed)

        self.books_list = QListWidget()
        for book in books:
            self.books_list.addItem(book.title)
        self.books_list.setFixedHeight(50)

        self.title_label = QLabel("Title:")
        self.add_date_label = QLabel("Add date:")
        self.page_count_label = QLabel("Page count:")
        self.page_current_label = QLabel("Current read:")
        self.read_times_label = QLabel("Read_times:")

        self.giveup_button = QPushButton("Give Up")

        self.finish_button = QPushButton("Finish")

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
        top_two.addWidget(self.page_current_label)
        top_two.addWidget(self.read_times_label)
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

        # Set Layout
        self.setLayout(main_layout)

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
