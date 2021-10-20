from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # Nomi
        self.setWindowTitle("Calculator")

        # geometrik tuzulishi
        self.setGeometry(150, 150, 360, 360)

        # methoddi chaqirish
        self.UiComponents()


        # hamma narsani korsatish
        self.show()

        # widget methodi
    def UiComponents(self):

        # label tuzish
        self.label = QLabel(self)

        # label hajmini berish
        self.label.setGeometry(5, 5, 350, 70)

        # labelga multi line tuzish
        self.label.setWordWrap(True)

        # label korinish styli
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid black;"
                                 "background : white;"
                                 "}")

        # labelga alignment tuzish
        self.label.setAlignment(Qt.AlignRight)

        # raqamlani hajmi
        self.label.setFont(QFont('Arial', 15))

        # ekranga raqam qoshish
        # va push button
        push1 = QPushButton("1", self)

        # geometrik tuzulishi
        push1.setGeometry(5, 150, 80, 40)

        # push button
        push2 = QPushButton("2", self)

        # geometrik tuzulishi
        push2.setGeometry(95, 150, 80, 40)

        # push button
        push3 = QPushButton("3", self)

        # geometrik tuzulishi
        push3.setGeometry(185, 150, 80, 40)

        # push button
        push4 = QPushButton("4", self)

        # geometrik tuzulishi
        push4.setGeometry(5, 200, 80, 40)

        # push button
        push5 = QPushButton("5", self)

        # geometrik tuzulishi
        push5.setGeometry(95, 200, 80, 40)

        # push button
        push6 = QPushButton("6", self)

        # geometrik tuzulishi
        push6.setGeometry(185, 200, 80, 40)

        # push button
        push7 = QPushButton("7", self)

        # geometrik tuzulishi
        push7.setGeometry(5, 250, 80, 40)

        # push button
        push8 = QPushButton("8", self)

        # geometrik tuzulishi
        push8.setGeometry(95, 250, 80, 40)

        # push button
        push9 = QPushButton("9", self)

        # geometrik tuzulishi
        push9.setGeometry(185, 250, 80, 40)

        # push button
        push0 = QPushButton("0", self)

        # geometrik tuzulishi
        push0.setGeometry(5, 300, 80, 40)

        # = push button qoshish
        # push button
        push_equal = QPushButton("=", self)

        # geometrik tuzulishi
        push_equal.setGeometry(275, 300, 80, 40)

        # barobar ni rangi, grafigi
        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.red)
        push_equal.setGraphicsEffect(c_effect)

        # push button
        push_plus = QPushButton("+", self)

        # geometrik tuzulishi
        push_plus.setGeometry(275, 250, 80, 40)

        # push button
        push_minus = QPushButton("-", self)

        # geometrik tuzulishi
        push_minus.setGeometry(275, 200, 80, 40)

        # push button
        push_mul = QPushButton("*", self)

        # geometrik tuzulishi
        push_mul.setGeometry(275, 150, 80, 40)

        # push button
        push_div = QPushButton("/", self)

        # geometrik tuzulishi
        push_div.setGeometry(185, 300, 80, 40)

        # push button
        push_point = QPushButton(".", self)

        # geometrik tuzulishi
        push_point.setGeometry(95, 300, 80, 40)

        # tozalash button
        push_clear = QPushButton("Clear", self)
        push_clear.setGeometry(5, 100, 80, 40)

        #  ( button
        push_qovs = QPushButton("(", self)
        push_qovs.setGeometry(95, 100, 80, 40)

        # ) button
        push_qovs2 = QPushButton(")", self)
        push_qovs2.setGeometry(185, 100, 80, 40)

        # 1 ta belgini ochirish
        push_del = QPushButton("Del", self)
        push_del.setGeometry(275, 100, 80, 40)

        # har bir button funksiyasini ulash
        push_minus.clicked.connect(self.action_minus)
        push_equal.clicked.connect(self.action_equal)
        push0.clicked.connect(self.action0)
        push1.clicked.connect(self.action1)
        push2.clicked.connect(self.action2)
        push3.clicked.connect(self.action3)
        push4.clicked.connect(self.action4)
        push5.clicked.connect(self.action5)
        push6.clicked.connect(self.action6)
        push7.clicked.connect(self.action7)
        push8.clicked.connect(self.action8)
        push9.clicked.connect(self.action9)
        push_div.clicked.connect(self.action_div)
        push_mul.clicked.connect(self.action_mul)
        push_plus.clicked.connect(self.action_plus)
        push_point.clicked.connect(self.action_point)
        push_clear.clicked.connect(self.action_clear)
        push_del.clicked.connect(self.action_del)
        push_qovs.clicked.connect(self.action_qovus)
        push_qovs2.clicked.connect(self.action_qovus2)


    def action_equal(self):

        # label texti olish
        equation = self.label.text()

        try:
            # javobini olish
            ans = eval(equation)

            # javobini korsatish
            self.label.setText(str(ans))

        except:
            # notori bosa daang
            self.label.setText("Wrong Input")

    def action_plus(self):
        # label textga qoshish
        text = self.label.text()
        self.label.setText(text + " + ")

    def action_minus(self):
        # label textga qoshish
        text = self.label.text()
        self.label.setText(text + " - ")

    def action_div(self):
        # label textga qoshish
        text = self.label.text()
        self.label.setText(text + " / ")

    def action_mul(self):
        # label textga qoshish
        text = self.label.text()
        self.label.setText(text + " * ")

    def action_point(self):
        # label textga qoshish
        text = self.label.text()
        self.label.setText(text + ".")

    def action0(self):
        # label textga qoshish
        text = self.label.text()
        self.label.setText(text + "0")

    def action1(self):
        # label textga qoshish
        text = self.label.text()
        self.label.setText(text + "1")

    def action2(self):
        # label textga qoshish
        text = self.label.text()
        self.label.setText(text + "2")

    def action3(self):
        # label textga qoshish
        text = self.label.text()
        self.label.setText(text + "3")

    def action4(self):
        # label textga qoshish
        text = self.label.text()
        self.label.setText(text + "4")

    def action5(self):
        # label textga qoshish
        text = self.label.text()
        self.label.setText(text + "5")

    def action6(self):
        # label textga qoshish
        text = self.label.text()
        self.label.setText(text + "6")

    def action7(self):
        # label textga qoshish
        text = self.label.text()
        self.label.setText(text + "7")

    def action8(self):
        # label textga qoshish
        text = self.label.text()
        self.label.setText(text + "8")

    def action9(self):
        # label textga qoshish
        text = self.label.text()
        self.label.setText(text + "9")

    def action_clear(self):
        # label text ni tozalash
        self.label.setText("")

    def action_qovus(self):
        # label textga qoshish
        text = self.label.text()
        self.label.setText(text + "(")

    def action_qovus2(self):
        # label textga qoshish
        text = self.label.text()
        self.label.setText(text + ")")

    def action_del(self):
        # oxiridan 1 tasini ochirish
        text = self.label.text()
        print(text[:len(text) - 1])
        self.label.setText(text[:len(text) - 1])


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

