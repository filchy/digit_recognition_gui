from PyQt5 import QtCore, QtGui, QtWidgets

from paint_gui import Painting
from multipredictor_gui import MultiPainting


class StartGUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(333, 157)
        MainWindow.setGeometry(700, 36, 333, 157)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.painting_button = QtWidgets.QPushButton(self.centralwidget)
        self.painting_button.setGeometry(QtCore.QRect(50, 40, 101, 51))
        self.painting_button.setObjectName("painting_button")

        self.multipredictor_button = QtWidgets.QPushButton(self.centralwidget)
        self.multipredictor_button.setGeometry(QtCore.QRect(180, 40, 101, 51))
        self.multipredictor_button.setObjectName("multipredictor_button")

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

        self.painting_button.clicked.connect(self.open_paint)
        self.multipredictor_button.clicked.connect(self.open_multi)

    def open_paint(self):
        self.window = QtWidgets.QMainWindow()
        self.ai = Painting()
        self.ai.setupUi(self.window)
        self.window.show()

    def open_multi(self):
        self.window = QtWidgets.QMainWindow()
        self.ai = MultiPainting()
        self.ai.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "start-gui"))
        self.painting_button.setText(_translate("MainWindow", "Painitng"))
        self.multipredictor_button.setText(_translate("MainWindow", "Multi-painting"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = StartGUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
