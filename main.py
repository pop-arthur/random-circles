from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
import sys


SCREEN_SIZE = (800, 500)


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi("UI.ui", self)
        self.resize(*SCREEN_SIZE)


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
