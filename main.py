#!/usr/bin/env python
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import wndonreading
import wndhaveread

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
        self.setWindowTitle("Books On Reading")
        self.main_window = wndonreading.OnReadingWindow(self)
        self.statusBar().showMessage(self.main_window.get_status_message())
        self.setCentralWidget(self.main_window)

    def on_reading_mode_selected(self):
        # Set Title
        self.setWindowTitle("Books on Reading")
        self.main_window = wndonreading.OnReadingWindow(self)
        self.statusBar().showMessage(self.main_window.get_status_message())
        self.setCentralWidget(self.main_window)

    def have_read_mode_selected(self):
        # Set Title
        self.setWindowTitle("Books have Read")
        self.main_window = wndhaveread.HaveReadWindow(self)
        self.statusBar().showMessage(self.main_window.get_status_message())
        self.setCentralWidget(self.main_window)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
