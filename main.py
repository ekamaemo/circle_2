import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPointF


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 800, 600)
        self.button = QPushButton(self)
        self.button.setText("НАЖМИ")
        self.button.setGeometry(310, 500, 93, 28)
        self.initUI()

    def initUI(self):
        self.paint = False
        self.button.clicked.connect(self.run)

    def run(self):
        self.paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.paint = False
        self.square = False
        self.triangle = False
        self.circle = False

    def draw_flag(self, qp):
        color = QColor(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        qp.setBrush(color)
        a = random.randint(20, 780)
        b = random.randint(20, 580)
        r = random.randint(20, min(800 - a, 600 - b))
        p = QPointF(a, b)
        color = QColor()
        qp.drawEllipse(p, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())