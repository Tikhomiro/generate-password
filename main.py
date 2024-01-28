import re 
import secrets 
import string 
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
 
 
def clicked_on(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1): 
 
    # Define the possible characters for the password 
    letters = string.ascii_letters 
    digits = string.digits 
    symbols = string.punctuation 
 
    # Combine all characters 
    all_characters = letters + digits + symbols 
 
    while True: 
        password = '' 
        # Generate password 
        for _ in range(length): 
            password += secrets.choice(all_characters) 
         
        constraints = [ 
            (nums, r'\d'), 
            (special_chars, fr'[{symbols}]'), 
            (uppercase, r'[A-Z]'), 
            (lowercase, r'[a-z]') 
        ] 
 
        # Check constraints         
        if all( 
            constraint <= len(re.findall(pattern, password)) 
            for constraint, pattern in constraints 
        ): 
            break 
     
    return password 
 
def main():
    #app
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(286, 241)
    MainWindow.setStyleSheet("background: rgb(159, 159, 159);")
    centralwidget = QtWidgets.QWidget(MainWindow)
    centralwidget.setObjectName("centralwidget")
    #button
    dawnlouds = QtWidgets.QPushButton(centralwidget)
    dawnlouds.setGeometry(QtCore.QRect(80, 40, 121, 23))
    dawnlouds.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid #fff;")
    dawnlouds.setObjectName("dawnlouds")
    #generat_password
    password_label = QtWidgets.QLabel(centralwidget)
    password_label.setGeometry(QtCore.QRect(80, 110, 150, 51))
    password_label.setStyleSheet("background: rgb(255, 255, 255)\n"
"color: red;\n" "border: 5px solid #fff;")
    def generate_password():
        password = clicked_on()
        return password_label.setText(password)

    dawnlouds.clicked.connect(generate_password)

    MainWindow.setCentralWidget(centralwidget)
    statusbar = QtWidgets.QStatusBar(MainWindow)
    statusbar.setObjectName("statusbar")
    MainWindow.setStatusBar(statusbar)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    dawnlouds.setText(_translate("MainWindow", "Генерировать"))
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__": 
    main()