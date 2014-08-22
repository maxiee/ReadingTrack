#!/usr/bin/env python
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import wndonreading
import wndreaded

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        
        on_reading_action = QAction("On Reading", self)
        on_reading_action.triggered.connect(self.on_reading_mode_selected)
        readed_action = QAction("Readed", self)
        readed_action.triggered.connect(self.readed_mode_selected)
        
        self.setStatusBar(QStatusBar())

        mode_menu = self.menuBar().addMenu("mode")
        mode_menu.addAction(on_reading_action)
        mode_menu.addAction(readed_action)

        #TODO: add a flag variable to indicate current window.
        #      prevent load the same window again.
        self.main_window = wndonreading.OnReadingWindow(self)
        self.main_window.status[str].connect(self.statusBar().showMessage)
        self.setCentralWidget(self.main_window)

    def on_reading_mode_selected(self):
        self.main_window = wndonreading.OnReadingWindow(self)
        self.setCentralWidget(self.main_window)

    def readed_mode_selected(self):
        self.main_window = wndreaded.ReadedWindow(self)
        self.setCentralWidget(self.main_window)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
