import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('kalkulator.ui', self)
        self.Bolish.clicked.connect(self.convert_to_float)
        self.Kopaytirish.clicked.connect(self.convert_to_float_1)
        self.Qoshish.clicked.connect(self.convert_to_float_2)
        self.Ayrish.clicked.connect(self.convert_to_float_3)

    def convert_to_float(self):
        try:
            value = int(self.textEdit.toPlainText())
            value2 = int(self.textEdit_2.toPlainText())
            result = value / value2
            self.Natija.setText(f"{result}")
        except ValueError:
            self.Natija.setText("Noto'g'ri")

    def convert_to_float_1(self):
        try:
            value = int(self.textEdit.toPlainText())
            value2 = int(self.textEdit_2.toPlainText())
            result = value * value2
            self.Natija.setText(f"{result}")
        except ValueError:
            self.Natija.setText("Noto'g'ri")

    def convert_to_float_2(self):
        try:
            value = int(self.textEdit.toPlainText())
            value2 = int(self.textEdit_2.toPlainText())
            result = value + value2
            self.Natija.setText(f"{result}")
        except ValueError:
            self.Natija.setText("Noto'g'ri")

    def convert_to_float_3(self):
        try:
            value = int(self.textEdit.toPlainText())
            value2 = int(self.textEdit_2.toPlainText())
            result = value - value2
            self.Natija.setText(f"{result}")
        except ValueError:
            self.Natija.setText("Noto'g'ri")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
