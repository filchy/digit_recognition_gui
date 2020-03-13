from PyQt5 import QtCore, QtGui, QtWidgets

from img_procces import multi_img_predict
from test2_app import Test2_app


class Test2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(994, 725)
        MainWindow.setGeometry(930, 231, 994, 725)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.main_image = QtWidgets.QLabel(self.centralwidget)
        self.main_image.setGeometry(QtCore.QRect(0, 60, 991, 611))
        self.main_image.setText("")
        self.main_image.setPixmap(QtGui.QPixmap("dependencies/images/start1.png"))
        self.main_image.setScaledContents(True)

        self.main_image.setObjectName("main_image")
        self.predict_button = QtWidgets.QPushButton(self.centralwidget)
        self.predict_button.setGeometry(QtCore.QRect(-10, -10, 1011, 71))
        self.predict_button.setObjectName("predict_button")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 994, 26))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.predict_button.clicked.connect(self.predict_action)

        self.ui = Test2_app()
        self.ui.setFixedSize(994, 658)
        self.ui.show()

    def predict_action(self):
        multi_img_predict()
        self.main_image.setPixmap(QtGui.QPixmap("dependencies/images/predict2.png")) 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "test2-gui"))
        self.predict_button.setText(_translate("MainWindow", "PREDICT"))
