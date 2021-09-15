from PyQt5 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('basic.ui', self)
        self.status.setText('Pass')


def Application():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec_()


if __name__ == "__main__":
    Application()
