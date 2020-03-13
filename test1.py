from PyQt5 import QtCore, QtGui, QtWidgets

from test1_app import Test1_app
from filchy_visualizer import filchy_layers
from vgg16_visualizer import vgg16_layers
from mobilenet_visualizer import mobilenet_layers
from img_procces import img_preprocces, img_prediction


class Test1(object):
    def setupUi(self, MainWindow):
        self.model_name = "filchy"
        self.activations = None

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(896, 559)
        MainWindow.setGeometry(700, 231, 896, 559)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.accuracy_img = QtWidgets.QLabel(self.centralwidget)
        self.accuracy_img.setGeometry(QtCore.QRect(530, 50, 331, 221))
        self.accuracy_img.setText("")
        self.accuracy_img.setPixmap(QtGui.QPixmap("./dependencies/graphs/filchy_accuracy.png"))
        self.accuracy_img.setScaledContents(False)
        self.accuracy_img.setObjectName("accuracy_img")

        self.loss_img = QtWidgets.QLabel(self.centralwidget)
        self.loss_img.setGeometry(QtCore.QRect(530, 310, 331, 221))
        self.loss_img.setText("")
        self.loss_img.setPixmap(QtGui.QPixmap("./dependencies/graphs/filchy_loss.png"))
        self.loss_img.setScaledContents(False)
        self.loss_img.setObjectName("loss_img")

        self.predict_img = QtWidgets.QLabel(self.centralwidget)
        self.predict_img.setGeometry(QtCore.QRect(30, 20, 331, 330))
        self.predict_img.setText("")
        self.predict_img.setPixmap(QtGui.QPixmap("dependencies/images/start1.png"))
        self.predict_img.setScaledContents(False)
        self.predict_img.setObjectName("predict_img")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.model_loss_label = QtWidgets.QLabel(self.centralwidget)
        self.model_loss_label.setGeometry(QtCore.QRect(640, 270, 151, 41))
        self.model_loss_label.setFont(font)
        self.model_loss_label.setObjectName("model_loss_label")
        
        self.model_accuracy_label = QtWidgets.QLabel(self.centralwidget)
        self.model_accuracy_label.setGeometry(QtCore.QRect(620, 10, 151, 41))
        self.model_accuracy_label.setFont(font)
        self.model_accuracy_label.setObjectName("model_accuracy_label")
        
        self.current_model_label1 = QtWidgets.QLabel(self.centralwidget)
        self.current_model_label1.setGeometry(QtCore.QRect(30, 305, 160, 41))
        self.current_model_label1.setFont(font)
        self.current_model_label1.setObjectName("current_model_label1")

        self.current_model_label2 = QtWidgets.QLabel(self.centralwidget)
        self.current_model_label2.setGeometry(QtCore.QRect(100, 305, 160, 41))
        self.current_model_label2.setFont(font)
        self.current_model_label2.setObjectName("current_model_label2")

        self.predicted_img_label = QtWidgets.QLabel(self.centralwidget)
        self.predicted_img_label.setGeometry(QtCore.QRect(30, 10, 160, 41))
        self.predicted_img_label.setFont(font)
        self.predicted_img_label.setObjectName("predicted_img_label")

        self.predicted_number_label1 = QtWidgets.QLabel(self.centralwidget)
        self.predicted_number_label1.setGeometry(QtCore.QRect(320, 170, 160, 41))
        self.predicted_number_label1.setFont(font)
        self.predicted_number_label1.setObjectName("predicted_number_label1")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)

        self.predicted_number_label2 = QtWidgets.QLabel(self.centralwidget)
        self.predicted_number_label2.setGeometry(QtCore.QRect(430, 170, 160, 41))
        self.predicted_number_label2.setFont(font)
        self.predicted_number_label2.setObjectName("predicted_number_label2")

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.filchy_button = QtWidgets.QPushButton(self.centralwidget)
        self.filchy_button.setGeometry(QtCore.QRect(30, 350, 101, 51))
        self.filchy_button.setFont(font)
        self.filchy_button.setObjectName("filchy_button")

        self.vgg16_button = QtWidgets.QPushButton(self.centralwidget)
        self.vgg16_button.setGeometry(QtCore.QRect(30, 410, 101, 51))
        self.vgg16_button.setFont(font)
        self.vgg16_button.setObjectName("vgg16_button")

        self.mobilenet_button = QtWidgets.QPushButton(self.centralwidget)
        self.mobilenet_button.setGeometry(QtCore.QRect(30, 470, 101, 51))
        self.mobilenet_button.setFont(font)
        self.mobilenet_button.setObjectName("mobilenet_button")

        self.predict_button = QtWidgets.QPushButton(self.centralwidget)
        self.predict_button.setGeometry(QtCore.QRect(320, 60, 101, 51))
        self.predict_button.setFont(font)
        self.predict_button.setObjectName("predict_button")

        self.layer_button = QtWidgets.QPushButton(self.centralwidget)
        self.layer_button.setGeometry(QtCore.QRect(320, 120, 101, 51))
        self.layer_button.setFont(font)
        self.layer_button.setObjectName("layer_button")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 896, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.filchy_button.clicked.connect(self.filchy_action)
        self.vgg16_button.clicked.connect(self.cnnsvm_action)
        self.mobilenet_button.clicked.connect(self.mobilenet_action)
        self.predict_button.clicked.connect(self.predict_action)
        self.layer_button.clicked.connect(self.layer_visualize)

        self.ui = Test1_app()
        self.ui.setFixedSize(252, 252)
        self.ui.show()

    def layer_visualize(self):
        if self.model_name == "filchy":
            self.window = QtWidgets.QMainWindow()
            self.ai = filchy_layers()
            self.ai.setupUi(self.window, self.activations)
            self.window.show()

        elif self.model_name == "vgg16":
            self.window = QtWidgets.QMainWindow()
            self.ai = vgg16_layers()
            self.ai.setupUi(self.window, self.activations)
            self.window.show()

        else:
            self.window = QtWidgets.QMainWindow()
            self.ai = mobilenet_layers()
            self.ai.setupUi(self.window, self.activations)
            self.window.show()

    def predict_action(self):
        self.predict_img.setPixmap(QtGui.QPixmap("dependencies/images/predict1.png"))
        img = img_preprocces()
        final_num, self.activations = img_prediction(img, self.model_name)
        self.predicted_number_label2.setText(final_num)

    def filchy_action(self):
        self.model_name = "filchy"
        self.accuracy_img.setPixmap(QtGui.QPixmap("./dependencies/graphs/filchy_accuracy.png"))
        self.loss_img.setPixmap(QtGui.QPixmap("./dependencies/graphs/filchy_loss.png"))
        self.current_model_label2.setText(self.model_name)

    def cnnsvm_action(self):
        self.model_name = "vgg16"
        self.accuracy_img.setPixmap(QtGui.QPixmap("./dependencies/graphs/vgg16_accuracy.png"))
        self.loss_img.setPixmap(QtGui.QPixmap("./dependencies/graphs/vgg16_loss.png"))
        self.current_model_label2.setText(self.model_name)

    def mobilenet_action(self):
        self.model_name = "mobilenet"
        self.accuracy_img.setPixmap(QtGui.QPixmap("./dependencies/graphs/mobilenet_accuracy.png"))
        self.loss_img.setPixmap(QtGui.QPixmap("./dependencies/graphs/mobilenet_loss.png"))
        self.current_model_label2.setText(self.model_name)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "test1-gui"))
        self.model_loss_label.setText(_translate("MainWindow", "Model loss"))
        self.model_accuracy_label.setText(_translate("MainWindow", "Model accuracy"))
        self.current_model_label1.setText(_translate("MainWindow", "Model:"))
        self.current_model_label2.setText(_translate("MainWindow", "filchy"))
        self.predicted_img_label.setText(_translate("MainWindow", "Predicted image"))
        self.predicted_number_label1.setText(_translate("MainWindow", "NUMBER: "))
        self.predicted_number_label2.setText(_translate("MainWindow", "-"))
        self.filchy_button.setText(_translate("MainWindow", "FilChy model"))
        self.vgg16_button.setText(_translate("MainWindow", "VGG16"))
        self.mobilenet_button.setText(_translate("MainWindow", "MobileNet"))
        self.predict_button.setText(_translate("MainWindow", "Predict"))
        self.layer_button.setText(_translate("MainWindow", "Show layers"))
