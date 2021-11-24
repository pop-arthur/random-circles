from random import randint

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
import sys


SCREEN_SIZE = (800, 500)


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi("UI.ui", self)
        self.resize(*SCREEN_SIZE)
        self.pushButton.clicked.connect(self.do_draw)
        self.flag = False

    def do_draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        self.qp.setBrush(QColor(250, 255, 0))
        x, y = randint(0, SCREEN_SIZE[0]), randint(0, SCREEN_SIZE[1])
        r = randint(0, 100)
        self.qp.drawEllipse(x, y, r, r)


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
