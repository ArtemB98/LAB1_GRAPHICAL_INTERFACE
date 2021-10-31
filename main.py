import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QFont


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('LAB_1')
        self.setGeometry(600, 800, 400, 400)

        self.btn = QPushButton(self)
        self.btn.move(10, 10)
        self.btn.setText("Выполнить ЛР №1!")
        self.btn.adjustSize()
        self.btn.clicked.connect(self.add_text)

        self.msg = QLabel(self)
        self.msg.move(10, 50)
        self.msg.setFont(QFont('Arial', 12))

    def add_text(self):
        self.msg.setText("Лабораторная работа выполнена!")
        self.msg.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())