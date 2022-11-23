from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

#приложение и главное окно
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('игральный кубик')
main_win.resize(600,)

btn1 = QPushButton('1')
btn2 = QPushButton('2')
btn3 = QPushButton('3')
btn4 = QPushButton('4')
btn5 = QPushButton('5')

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line1.addWidget(btn1)
line1.addWidget(btn2)
line2.addWidget(btn3)
line3.addWidget(btn4)
line3.addWidget(btn5)

main_line = QVBoxLayout()
main_line.addLayout(line1)
main_line.addLayout(line2)
main_line.addLayout(line3)

main_win.setLayout(main_line)


main_win.show()
app.exec_()
