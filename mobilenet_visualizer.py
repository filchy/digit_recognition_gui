from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt


class mobilenet_layers(object):
    def setupUi(self, MainWindow, activations):
        self.activations = activations

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(631, 495)
        MainWindow.setGeometry(800, 331, 631, 495)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(50, 10, 91, 31))
        self.pushButton1.setObjectName("pushButton1")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(50, 50, 91, 31))
        self.pushButton2.setObjectName("pushButton2")

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(50, 90, 91, 31))
        self.pushButton3.setObjectName("pushButton3")

        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(50, 130, 91, 31))
        self.pushButton4.setObjectName("pushButton4")

        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(50, 170, 91, 31))
        self.pushButton5.setObjectName("pushButton5")

        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton6.setGeometry(QtCore.QRect(50, 210, 91, 31))
        self.pushButton6.setObjectName("pushButton6")

        self.pushButton7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton7.setGeometry(QtCore.QRect(50, 250, 91, 31))
        self.pushButton7.setObjectName("pushButton7")

        self.pushButton8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton8.setGeometry(QtCore.QRect(50, 290, 91, 31))
        self.pushButton8.setObjectName("pushButton8")

        self.pushButton9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton9.setGeometry(QtCore.QRect(50, 330, 91, 31))
        self.pushButton9.setObjectName("pushButton9")

        self.pushButton10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton10.setGeometry(QtCore.QRect(50, 370, 91, 31))
        self.pushButton10.setObjectName("pushButton10")

        self.pushButton11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton11.setGeometry(QtCore.QRect(50, 410, 91, 31))
        self.pushButton11.setObjectName("pushButton11")

        self.pushButton12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton12.setGeometry(QtCore.QRect(160, 10, 91, 31))
        self.pushButton12.setObjectName("pushButton12")

        self.pushButton13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton13.setGeometry(QtCore.QRect(160, 50, 91, 31))
        self.pushButton13.setObjectName("pushButton13")

        self.pushButton14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton14.setGeometry(QtCore.QRect(160, 90, 91, 31))
        self.pushButton14.setObjectName("pushButton14")

        self.pushButton15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton15.setGeometry(QtCore.QRect(160, 130, 91, 31))
        self.pushButton15.setObjectName("pushButton15")

        self.pushButton16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton16.setGeometry(QtCore.QRect(160, 170, 91, 31))
        self.pushButton16.setObjectName("pushButton16")

        self.pushButton17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton17.setGeometry(QtCore.QRect(160, 210, 91, 31))
        self.pushButton17.setObjectName("pushButton17")

        self.pushButton18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton18.setGeometry(QtCore.QRect(160, 250, 91, 31))
        self.pushButton18.setObjectName("pushButton18")

        self.pushButton19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton19.setGeometry(QtCore.QRect(160, 290, 91, 31))
        self.pushButton19.setObjectName("pushButton19")

        self.pushButton20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton20.setGeometry(QtCore.QRect(160, 330, 91, 31))
        self.pushButton20.setObjectName("pushButton20")

        self.pushButton21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton21.setGeometry(QtCore.QRect(160, 370, 91, 31))
        self.pushButton21.setObjectName("pushButton21")

        self.pushButton22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton22.setGeometry(QtCore.QRect(160, 410, 91, 31))
        self.pushButton22.setObjectName("pushButton22")

        self.pushButton23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton23.setGeometry(QtCore.QRect(270, 10, 91, 31))
        self.pushButton23.setObjectName("pushButton23")

        self.pushButton24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton24.setGeometry(QtCore.QRect(270, 50, 91, 31))
        self.pushButton24.setObjectName("pushButton24")

        self.pushButton25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton25.setGeometry(QtCore.QRect(270, 90, 91, 31))
        self.pushButton25.setObjectName("pushButton25")

        self.pushButton26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton26.setGeometry(QtCore.QRect(270, 130, 91, 31))
        self.pushButton26.setObjectName("pushButton26")

        self.pushButton27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton27.setGeometry(QtCore.QRect(270, 170, 91, 31))
        self.pushButton27.setObjectName("pushButton27")

        self.pushButton28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton28.setGeometry(QtCore.QRect(270, 210, 91, 31))
        self.pushButton28.setObjectName("pushButton28")

        self.pushButton29 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton29.setGeometry(QtCore.QRect(270, 250, 91, 31))
        self.pushButton29.setObjectName("pushButton29")

        self.pushButton30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton30.setGeometry(QtCore.QRect(270, 290, 91, 31))
        self.pushButton30.setObjectName("pushButton30")

        self.pushButton31 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton31.setGeometry(QtCore.QRect(270, 330, 91, 31))
        self.pushButton31.setObjectName("pushButton31")

        self.pushButton32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton32.setGeometry(QtCore.QRect(270, 370, 91, 31))
        self.pushButton32.setObjectName("pushButton32")

        self.pushButton33 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton33.setGeometry(QtCore.QRect(270, 410, 91, 31))
        self.pushButton33.setObjectName("pushButton33")

        self.pushButton34 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton34.setGeometry(QtCore.QRect(380, 10, 91, 31))
        self.pushButton34.setObjectName("pushButton34")

        self.pushButton35 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton35.setGeometry(QtCore.QRect(380, 50, 91, 31))
        self.pushButton35.setObjectName("pushButton35")

        self.pushButton36 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton36.setGeometry(QtCore.QRect(380, 90, 91, 31))
        self.pushButton36.setObjectName("pushButton36")

        self.pushButton37 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton37.setGeometry(QtCore.QRect(380, 130, 91, 31))
        self.pushButton37.setObjectName("pushButton37")

        self.pushButton38 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton38.setGeometry(QtCore.QRect(380, 170, 91, 31))
        self.pushButton38.setObjectName("pushButton38")

        self.pushButton39 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton39.setGeometry(QtCore.QRect(380, 210, 91, 31))
        self.pushButton39.setObjectName("pushButton39")

        self.pushButton40 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton40.setGeometry(QtCore.QRect(380, 250, 91, 31))
        self.pushButton40.setObjectName("pushButton40")

        self.pushButton41 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton41.setGeometry(QtCore.QRect(380, 290, 91, 31))
        self.pushButton41.setObjectName("pushButton41")

        self.pushButton42 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton42.setGeometry(QtCore.QRect(380, 330, 91, 31))
        self.pushButton42.setObjectName("pushButton42")

        self.pushButton43 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton43.setGeometry(QtCore.QRect(380, 370, 91, 31))
        self.pushButton43.setObjectName("pushButton43")

        self.pushButton44 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton44.setGeometry(QtCore.QRect(380, 410, 91, 31))
        self.pushButton44.setObjectName("pushButton44")

        self.pushButton45 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton45.setGeometry(QtCore.QRect(490, 10, 91, 31))
        self.pushButton45.setObjectName("pushButton45")

        self.pushButton46 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton46.setGeometry(QtCore.QRect(490, 50, 91, 31))
        self.pushButton46.setObjectName("pushButton46")

        self.pushButton47 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton47.setGeometry(QtCore.QRect(490, 90, 91, 31))
        self.pushButton47.setObjectName("pushButton47")

        self.pushButton48 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton48.setGeometry(QtCore.QRect(490, 130, 91, 31))
        self.pushButton48.setObjectName("pushButton48")

        self.pushButton49 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton49.setGeometry(QtCore.QRect(490, 170, 91, 31))
        self.pushButton49.setObjectName("pushButton49")

        self.pushButton50 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton50.setGeometry(QtCore.QRect(490, 210, 91, 31))
        self.pushButton50.setObjectName("pushButton50")

        self.pushButton51 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton51.setGeometry(QtCore.QRect(490, 250, 91, 31))
        self.pushButton51.setObjectName("pushButton51")

        self.pushButton52 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton52.setGeometry(QtCore.QRect(490, 290, 91, 31))
        self.pushButton52.setObjectName("pushButton52")

        self.pushButton53 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton53.setGeometry(QtCore.QRect(490, 330, 91, 31))
        self.pushButton53.setObjectName("pushButton53")

        self.pushButton54 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton54.setGeometry(QtCore.QRect(490, 370, 91, 31))
        self.pushButton54.setObjectName("pushButton54")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton1.clicked.connect(lambda x:self.click(1))
        self.pushButton2.clicked.connect(lambda x:self.click(2))
        self.pushButton3.clicked.connect(lambda x:self.click(3))
        self.pushButton4.clicked.connect(lambda x:self.click(4))
        self.pushButton5.clicked.connect(lambda x:self.click(5))
        self.pushButton6.clicked.connect(lambda x:self.click(6))
        self.pushButton7.clicked.connect(lambda x:self.click(7))
        self.pushButton8.clicked.connect(lambda x:self.click(8))
        self.pushButton9.clicked.connect(lambda x:self.click(9))
        self.pushButton10.clicked.connect(lambda x:self.click(10))
        self.pushButton11.clicked.connect(lambda x:self.click(11))
        self.pushButton12.clicked.connect(lambda x:self.click(12))
        self.pushButton13.clicked.connect(lambda x:self.click(13))
        self.pushButton14.clicked.connect(lambda x:self.click(14))
        self.pushButton15.clicked.connect(lambda x:self.click(15))
        self.pushButton16.clicked.connect(lambda x:self.click(16))
        self.pushButton17.clicked.connect(lambda x:self.click(17))
        self.pushButton18.clicked.connect(lambda x:self.click(18))
        self.pushButton19.clicked.connect(lambda x:self.click(19))
        self.pushButton20.clicked.connect(lambda x:self.click(20))
        self.pushButton21.clicked.connect(lambda x:self.click(21))
        self.pushButton22.clicked.connect(lambda x:self.click(22))
        self.pushButton23.clicked.connect(lambda x:self.click(23))
        self.pushButton24.clicked.connect(lambda x:self.click(24))
        self.pushButton25.clicked.connect(lambda x:self.click(25))
        self.pushButton26.clicked.connect(lambda x:self.click(26))
        self.pushButton27.clicked.connect(lambda x:self.click(27))
        self.pushButton28.clicked.connect(lambda x:self.click(28))
        self.pushButton29.clicked.connect(lambda x:self.click(29))
        self.pushButton30.clicked.connect(lambda x:self.click(30))
        self.pushButton31.clicked.connect(lambda x:self.click(31))
        self.pushButton32.clicked.connect(lambda x:self.click(32))
        self.pushButton33.clicked.connect(lambda x:self.click(33))
        self.pushButton34.clicked.connect(lambda x:self.click(34))
        self.pushButton35.clicked.connect(lambda x:self.click(35))
        self.pushButton36.clicked.connect(lambda x:self.click(36))
        self.pushButton37.clicked.connect(lambda x:self.click(37))
        self.pushButton38.clicked.connect(lambda x:self.click(38))
        self.pushButton39.clicked.connect(lambda x:self.click(39))
        self.pushButton40.clicked.connect(lambda x:self.click(40))
        self.pushButton41.clicked.connect(lambda x:self.click(41))
        self.pushButton42.clicked.connect(lambda x:self.click(42))
        self.pushButton43.clicked.connect(lambda x:self.click(43))
        self.pushButton44.clicked.connect(lambda x:self.click(44))
        self.pushButton45.clicked.connect(lambda x:self.click(45))
        self.pushButton46.clicked.connect(lambda x:self.click(46))
        self.pushButton47.clicked.connect(lambda x:self.click(47))
        self.pushButton48.clicked.connect(lambda x:self.click(48))
        self.pushButton49.clicked.connect(lambda x:self.click(49))
        self.pushButton50.clicked.connect(lambda x:self.click(50))
        self.pushButton51.clicked.connect(lambda x:self.click(51))
        self.pushButton52.clicked.connect(lambda x:self.click(52))
        self.pushButton53.clicked.connect(lambda x:self.click(53))
        self.pushButton54.clicked.connect(lambda x:self.click(54))

    def click(self, i):
        if self.activations is not None:
            activation = self.activations[i]
            activation_index = 0
            row_size, col_size = 3, 3
            
            fig, ax = plt.subplots(row_size, col_size, figsize=(row_size*1.8,col_size*1.8))

            for row in range(0,row_size):
                for col in range(0,col_size):
                    ax[row][col].imshow(activation[0, :, :, activation_index], cmap='gray')
                    activation_index += 1
            plt.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "mobilenet_layers"))
        self.pushButton1.setText(_translate("MainWindow", "Layer 1"))
        self.pushButton2.setText(_translate("MainWindow", "Layer 2"))
        self.pushButton3.setText(_translate("MainWindow", "Layer 3"))
        self.pushButton4.setText(_translate("MainWindow", "Layer 4"))
        self.pushButton5.setText(_translate("MainWindow", "Layer 5"))
        self.pushButton6.setText(_translate("MainWindow", "Layer 6"))
        self.pushButton7.setText(_translate("MainWindow", "Layer 7"))
        self.pushButton8.setText(_translate("MainWindow", "Layer 8"))
        self.pushButton9.setText(_translate("MainWindow", "Layer 9"))
        self.pushButton10.setText(_translate("MainWindow", "Layer 10"))
        self.pushButton11.setText(_translate("MainWindow", "Layer 11"))
        self.pushButton12.setText(_translate("MainWindow", "Layer 12"))
        self.pushButton13.setText(_translate("MainWindow", "Layer 13"))
        self.pushButton14.setText(_translate("MainWindow", "Layer 14"))
        self.pushButton15.setText(_translate("MainWindow", "Layer 15"))
        self.pushButton16.setText(_translate("MainWindow", "Layer 16"))
        self.pushButton17.setText(_translate("MainWindow", "Layer 17"))
        self.pushButton19.setText(_translate("MainWindow", "Layer 19"))
        self.pushButton18.setText(_translate("MainWindow", "Layer 18"))
        self.pushButton20.setText(_translate("MainWindow", "Layer 20"))
        self.pushButton21.setText(_translate("MainWindow", "Layer 21"))
        self.pushButton22.setText(_translate("MainWindow", "Layer 22"))
        self.pushButton23.setText(_translate("MainWindow", "Layer 23"))
        self.pushButton24.setText(_translate("MainWindow", "Layer 24"))
        self.pushButton25.setText(_translate("MainWindow", "Layer 25"))
        self.pushButton26.setText(_translate("MainWindow", "Layer 26"))
        self.pushButton27.setText(_translate("MainWindow", "Layer 27"))
        self.pushButton28.setText(_translate("MainWindow", "Layer 28"))
        self.pushButton29.setText(_translate("MainWindow", "Layer 29"))
        self.pushButton30.setText(_translate("MainWindow", "Layer 30"))
        self.pushButton31.setText(_translate("MainWindow", "Layer 31"))
        self.pushButton32.setText(_translate("MainWindow", "Layer 32"))
        self.pushButton33.setText(_translate("MainWindow", "Layer 33"))
        self.pushButton34.setText(_translate("MainWindow", "Layer 34"))
        self.pushButton35.setText(_translate("MainWindow", "Layer 35"))
        self.pushButton36.setText(_translate("MainWindow", "Layer 36"))
        self.pushButton37.setText(_translate("MainWindow", "Layer 37"))
        self.pushButton38.setText(_translate("MainWindow", "Layer 38"))
        self.pushButton39.setText(_translate("MainWindow", "Layer 39"))
        self.pushButton40.setText(_translate("MainWindow", "Layer 40"))
        self.pushButton41.setText(_translate("MainWindow", "Layer 41"))
        self.pushButton42.setText(_translate("MainWindow", "Layer 42"))
        self.pushButton43.setText(_translate("MainWindow", "Layer 43"))
        self.pushButton44.setText(_translate("MainWindow", "Layer 44"))
        self.pushButton45.setText(_translate("MainWindow", "Layer 45"))
        self.pushButton46.setText(_translate("MainWindow", "Layer 46"))
        self.pushButton47.setText(_translate("MainWindow", "Layer 47"))
        self.pushButton48.setText(_translate("MainWindow", "Layer 48"))
        self.pushButton49.setText(_translate("MainWindow", "Layer 49"))
        self.pushButton50.setText(_translate("MainWindow", "Layer 50"))
        self.pushButton51.setText(_translate("MainWindow", "Layer 51"))
        self.pushButton52.setText(_translate("MainWindow", "Layer 52"))
        self.pushButton53.setText(_translate("MainWindow", "Layer 53"))
        self.pushButton54.setText(_translate("MainWindow", "Layer 54"))
