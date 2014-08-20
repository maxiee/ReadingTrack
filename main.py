#!/usr/bin/env python
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import wndonreading

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        
        self.main_widget = wndonreading.OnReadingWindow(self)
        self.setCentralWidget(self.main_widget)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
