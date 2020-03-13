from PyQt5 import QtCore, QtGui, QtWidgets

from test1 import Test1
from test2 import Test2
from test3 import Test3


class StartGUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(333, 157)
        MainWindow.setGeometry(700, 36, 333, 157)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.test1_button = QtWidgets.QPushButton(self.centralwidget)
        self.test1_button.setGeometry(QtCore.QRect(56, 15, 101, 51))
        self.test1_button.setObjectName("test1_button")

        self.test2_button = QtWidgets.QPushButton(self.centralwidget)
        self.test2_button.setGeometry(QtCore.QRect(166, 15, 101, 51))
        self.test2_button.setObjectName("test2_button")

        self.test3_button = QtWidgets.QPushButton(self.centralwidget)
        self.test3_button.setGeometry(QtCore.QRect(115, 70, 101, 51))
        self.test3_button.setObjectName("test3_button")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 333, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.test1_button.clicked.connect(self.open_test1)
        self.test2_button.clicked.connect(self.open_test2)
        self.test3_button.clicked.connect(self.open_test3)

    def open_test1(self):
        self.window = QtWidgets.QMainWindow()
        self.ai = Test1()
        self.ai.setupUi(self.window)
        self.window.show()

    def open_test2(self):
        self.window = QtWidgets.QMainWindow()
        self.ai = Test2()
        self.ai.setupUi(self.window)
        self.window.show()

    def open_test3(self):
        self.window = QtWidgets.QMainWindow()
        self.ai = Test3()
        self.ai.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "start-gui"))
        self.test1_button.setText(_translate("MainWindow", "Test 1"))
        self.test2_button.setText(_translate("MainWindow", "Test 2"))
        self.test3_button.setText(_translate("MainWindow", "Test 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = StartGUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
