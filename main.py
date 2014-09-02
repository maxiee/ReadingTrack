#!/usr/bin/env python
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import wndonreading
import wndhaveread
import wndonreadingone
import constants

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        
        on_reading_action = QAction("On Reading", self)
        on_reading_action.triggered.connect(self.on_reading_mode_selected)
        have_read_action = QAction("Have Read", self)
        have_read_action.triggered.connect(self.have_read_mode_selected)
        
        self.statusBar().showMessage("Hello!")

        mode_menu = self.menuBar().addMenu("mode")
        mode_menu.addAction(on_reading_action)
        mode_menu.addAction(have_read_action)

        #TODO: add a flag variable to indicate current window.
        #      prevent load the same window again.
        # Set Title
        self.on_reading_mode_selected()

    def on_reading_mode_selected(self):
        # Set Title
        self.setWindowTitle("Books on Reading")
        self.main_window = wndonreading.OnReadingWindow(self)
        self.main_window.begin_read_signal[int].connect(self.switch_window)
        self.statusBar().showMessage(self.main_window.get_status_message())
        self.setCentralWidget(self.main_window)
    
    def on_reading_one_mode_selected(self, book_selected_id):
        # Set Title
        self.setWindowTitle("正在阅读一本书")
        print("CCCCCCC" + str(book_selected_id))
        self.main_window = wndonreadingone.WndOnReadingOne(self)
        self.main_window.book_id = book_selected_id
        self.main_window.init_book_title()
        self.setCentralWidget(self.main_window)

    def have_read_mode_selected(self):
        # Set Title
        self.setWindowTitle("Books have Read")
        self.main_window = wndhaveread.HaveReadWindow(self)
        self.statusBar().showMessage(self.main_window.get_status_message())
        self.setCentralWidget(self.main_window)

    def switch_window(self, index):
        print("Ouch! WTF!!!!")
        if index == 0:
            book_selected_id = self.main_window.book_selected_id
            if constants.DEBUG:
                print("Book selected ID is: " + str(book_selected_id))
            self.on_reading_one_mode_selected(book_selected_id)
            

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
