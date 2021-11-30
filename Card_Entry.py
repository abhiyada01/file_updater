import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import time

card = "HE315451-20.22#D82110385720678"

card_data = card.split('#')
po_num = card_data[1][-11:-4]
part_num = card_data[0].split('-')[0]
ver = card_data[0].split('-')[1]
# print(part_num,",",ver,'-',po_num)

class Application(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.label1 = QLabel('Barcode')
        self.label1.setStyleSheet("border: 1px solid black;") # setting up border
        self.label1.setFont(QFont('Arial', 18))# setting font and size
        # self.label1.setFixedWidth(5)
        self.label1.setFixedHeight(40)
        self.line1 = QLineEdit()
        self.line1.setFont(QFont("Timers",15))
        self.line1.setStyleSheet("QLineEdit { background-color: white }")
        self.line1.setAlignment(Qt.AlignCenter)
        self.line1.setDisabled(True)
        # self.line1.textChanged.connect(self.barcode_event)
        # self.line1.setFixedWidth(3)
        self.line1.setFixedHeight(40)
        hbox1 = QVBoxLayout()
        hbox2 = QVBoxLayout()
        hbox1.addWidget(self.label1)
        hbox2.addWidget(self.line1)



        self.ser_label = QLabel('Serial Number')
        self.ser_label.setStyleSheet("border: 1px solid black;") # setting up border
        self.ser_label.setFont(QFont('Arial', 18))# setting font and size
        self.ser_label.setFixedHeight(40)
        self.ser_line = QLineEdit()
        self.ser_line.setFont(QFont("Timers",20))
        self.ser_line.setFixedHeight(40)
        self.ser_line.setStyleSheet("QLineEdit { background-color: white }")
        self.ser_line.setAlignment(Qt.AlignCenter)
        self.ser_line.setDisabled(True)

        hbox1.addWidget(self.ser_label)
        hbox2.addWidget(self.ser_line)
        
        

        self.label2 = QLabel('PO Number')
        self.label2.setStyleSheet("border: 1px solid black;") # setting up border
        self.label2.setFont(QFont('Arial', 20))# setting font and size
        self.label2.setFixedHeight(40)
        self.line2 = QLineEdit()
        self.line2.setFont(QFont("Timers",30))
        self.line2.setStyleSheet("QLineEdit { background-color: white }")
        self.line2.setAlignment(Qt.AlignVCenter)
        self.line2.setDisabled(True)
        self.line2.setFixedHeight(40)
        hbox1.addWidget(self.label2)
        hbox2.addWidget(self.line2)

        self.label3 = QLabel('Operator')
        self.label3.setStyleSheet("border: 1px solid black;") # setting up border
        self.label3.setFont(QFont('Arial', 20))# setting font and size
        self.label3.setFixedHeight(40)
        self.line3= QLineEdit()
        self.line3.textChanged.connect(self.disableButton)
        self.line3.setFont(QFont("Timers",30))
        self.line3.setFixedHeight(40)
        self.line3.setStyleSheet("QLineEdit { background-color: white }")
        # self.line3.setDisabled(True)
        
        hbox1.addWidget(self.label3)
        hbox2.addWidget(self.line3)

        self.label4 = QLabel('Date')
        self.label4.setStyleSheet("border: 1px solid black;") # setting up border
        self.label4.setFont(QFont('Arial', 20))# setting font and size
        self.label4.setFixedHeight(40)
        self.line4 = QLineEdit()
        self.line4.setFont(QFont("Timers",30))
        self.line4.setFixedHeight(40)
        self.line4.setStyleSheet("QLineEdit { background-color: white }")
        self.line4.setDisabled(True)
        hbox1.addWidget(self.label4)
        hbox2.addWidget(self.line4)

        self.label5 = QLabel('Shift')
        self.label5.setStyleSheet("border: 1px solid black;") # setting up border
        self.label5.setFont(QFont('Arial', 20))# setting font and size
        self.label5.setFixedHeight(40)
        self.line5 = QLineEdit()
        self.line5.setFont(QFont("Timers",30))
        self.line5.setFixedHeight(40)
        self.line5.setStyleSheet("QLineEdit { background-color: white }")
        self.line5.setDisabled(True)
        hbox1.addWidget(self.label5)
        hbox2.addWidget(self.line5)


        self.label6 = QLabel('Status')
        self.label6.setStyleSheet("border: 1px solid black;") # setting up border
        self.label6.setFont(QFont('Arial', 20))# setting font and size
        self.label6.setFixedHeight(40)
        self.line6 = QLineEdit()
        self.line6.setFont(QFont("Timers",30))
        self.line6.setFixedHeight(40)
        self.line6.setStyleSheet("QLineEdit { background-color: white }")

        hbox1.addWidget(self.label6)
        hbox2.addWidget(self.line6)


        self.label7 = QLabel('Fault')
        self.label7.setStyleSheet("border: 1px solid black;") # setting up border
        self.label7.setFont(QFont('Arial', 20))# setting font and size
        self.label7.setFixedHeight(40)
        self.line7 = QLineEdit()
        self.line7.setFont(QFont("Timers",30))
        self.line7.setFixedHeight(40)
        self.line7.setStyleSheet("QLineEdit { background-color: white }")
        hbox1.addWidget(self.label7)
        hbox2.addWidget(self.line7)
        

        self.rad = QPushButton("UPDATE")
        self.rad.clicked.connect(self.upadate_data)
        self.rad.setChecked(True)  #to select the button by default.
        self.rad.setFont(QFont("Timers",20))
        self.rad.setStyleSheet("QLineEdit { background-color: white }")
        self.exi = QPushButton("Exit")
        self.exi.setFont(QFont("Timers",30))
        self.exi.setStyleSheet("QLineEdit { background-color: white }")
        self.exi.clicked.connect(self.closeEvent)
        self.exi.setChecked(False)
        hbox1.addWidget(self.exi)
        hbox2.addWidget(self.rad)
        hbox1.addStretch(1)
        hbox2.addStretch(1)

        vb = QHBoxLayout()
        vb.addStretch(1)
        
        vb.addLayout(hbox1)
        vb.addLayout(hbox2)
        self.setLayout(vb)

    def upadate_data(self):
        self.get_time()

    
    def disableButton(self):
        if len(self.line3.text()) > 0:
            # self.btnButton.setDisable(True)
            self.line1.setDisabled(False)

    def check_operator(self):
        op = self.line3.text()
        if len(op) is 0:
            self.error_message("First enter operator name")
        else:
            print(op)
            

    def get_time(self):
        t = time.gmtime([secs])
        print(t)


    def get_shift(self):
        cur_shift = ''
        t = 0
        if 6 > t < 14:
            cur_shift = 'A'
        elif 14 < t < 22:
            cur_shift = 'B'
        else:
            cur_shift = 'C'



    def error_message(self, mess):
        print('2')
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(mess)
        msg.setInformativeText('More information')
        msg.setWindowTitle("Error")
        msg.exec_()
        



    def closeEvent(self, event):
        self.close()
        
        


def main():

    app = QApplication(sys.argv)
    w = Application()
    wi,ht = 600,500
    w.setWindowTitle('Data Entry')
    w.show()
    w.setFixedWidth(wi)
    w.setFixedHeight(ht)
    sys.exit(app.exec_())
    os.exit()


if __name__ == '__main__':
    main()
