from PyQt5 import QtCore, QtGui, QtWidgets
import cv2

from img_procces import find_roi, roi_img_predict


class Test3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(850, 592)
        MainWindow.setGeometry(480, 231, 850, 592)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.final_img = QtWidgets.QLabel(self.centralwidget)
        self.final_img.setGeometry(QtCore.QRect(0, 0, 850, 541))
        self.final_img.setText("")
        self.final_img.setPixmap(QtGui.QPixmap("dependencies/images/start2.png"))
        self.final_img.setScaledContents(True)
        self.final_img.setObjectName("final_img")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 26))
        self.menubar.setObjectName("menubar")
        self.menuLoad_img = QtWidgets.QMenu(self.menubar)
        self.menuLoad_img.setObjectName("menuLoad_img")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionLoad_image = QtWidgets.QAction(MainWindow)
        self.actionLoad_image.setObjectName("actionLoad_image")
        self.menuLoad_img.addAction(self.actionLoad_image)
        self.menubar.addAction(self.menuLoad_img.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.menuLoad_img.triggered.connect(self.load_and_predict)

    def load_and_predict(self):
        imagePath, _ = QtWidgets.QFileDialog.getOpenFileName()

        if imagePath != "":
            path = "." + imagePath[29:]
            img_to_process = cv2.imread(path)

            img = find_roi(img_to_process)

            roi_img_predict(img)

            self.final_img.setPixmap(QtGui.QPixmap("./dependencies/images/predict3.jpg"))
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "test3-gui"))
        self.menuLoad_img.setTitle(_translate("MainWindow", "Load"))
        self.actionLoad_image.setText(_translate("MainWindow", "Load image"))
        self.actionLoad_image.setShortcut(_translate("MainWindow", "Ctrl+L"))
