# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Jashua\OneDrive\Escritorio\AVANCE1\Interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(956, 657)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(32, 33,79);\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_superior = QtWidgets.QFrame(self.frame)
        self.frame_superior.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_superior.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_superior.setStyleSheet("Qframe{\n"
"background-color: rgb(191, 186, 43);}\n"
"\n"
"QpushButton{\n"
"border-radius:18px;\n"
"background-color: rgb(255, 103, 43);}\n"
"\n"
"QpushButton:hover{\n"
"background-color: rgb(0, 85, 255);}")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(803, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bt_minimize = QtWidgets.QPushButton(self.frame_superior)
        self.bt_minimize.setMinimumSize(QtCore.QSize(30, 30))
        self.bt_minimize.setMaximumSize(QtCore.QSize(30, 30))
        self.bt_minimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Jashua\\OneDrive\\Escritorio\\AVANCE1\\IMAGENES/mi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_minimize.setIcon(icon)
        self.bt_minimize.setIconSize(QtCore.QSize(36, 36))
        self.bt_minimize.setObjectName("bt_minimize")
        self.horizontalLayout.addWidget(self.bt_minimize)
        self.bt_normal = QtWidgets.QPushButton(self.frame_superior)
        self.bt_normal.setMinimumSize(QtCore.QSize(30, 30))
        self.bt_normal.setMaximumSize(QtCore.QSize(30, 30))
        self.bt_normal.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Jashua\\OneDrive\\Escritorio\\AVANCE1\\IMAGENES/ma.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_normal.setIcon(icon1)
        self.bt_normal.setIconSize(QtCore.QSize(36, 36))
        self.bt_normal.setObjectName("bt_normal")
        self.horizontalLayout.addWidget(self.bt_normal)
        self.bt_maximize = QtWidgets.QPushButton(self.frame_superior)
        self.bt_maximize.setMinimumSize(QtCore.QSize(30, 30))
        self.bt_maximize.setMaximumSize(QtCore.QSize(30, 30))
        self.bt_maximize.setText("")
        self.bt_maximize.setIcon(icon1)
        self.bt_maximize.setIconSize(QtCore.QSize(36, 36))
        self.bt_maximize.setObjectName("bt_maximize")
        self.horizontalLayout.addWidget(self.bt_maximize)
        self.bt_close = QtWidgets.QPushButton(self.frame_superior)
        self.bt_close.setMinimumSize(QtCore.QSize(30, 30))
        self.bt_close.setMaximumSize(QtCore.QSize(30, 30))
        self.bt_close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\Jashua\\OneDrive\\Escritorio\\AVANCE1\\IMAGENES/x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_close.setIcon(icon2)
        self.bt_close.setIconSize(QtCore.QSize(36, 36))
        self.bt_close.setObjectName("bt_close")
        self.horizontalLayout.addWidget(self.bt_close)
        self.verticalLayout_2.addWidget(self.frame_superior)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 30, 401, 61))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 26pt \"Bauhaus 93\";")
        self.label.setObjectName("label")
        self.cb_list_ports = QtWidgets.QComboBox(self.frame_2)
        self.cb_list_ports.setGeometry(QtCore.QRect(300, 140, 150, 22))
        self.cb_list_ports.setStyleSheet("QComboBox{\n"
"    border: 3px solid rgb(255,255,255);\n"
"    border-radius: 5px;\n"
"    min-width: 6em;\n"
"    color: rgb(255,255,255);\n"
"    font: 87 10pt    \"Arial Black\" ;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width:3px;\n"
"    border-left-color: rgb(255,255,255);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"    background: #2c2c2c;\n"
"    selection-background-color: #ff0037;\n"
"    color: rgb(255,255,255);\n"
"}")
        self.cb_list_ports.setObjectName("cb_list_ports")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(180, 500, 100, 100))
        self.label_2.setMinimumSize(QtCore.QSize(100, 100))
        self.label_2.setMaximumSize(QtCore.QSize(50, 100))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\Jashua\\OneDrive\\Escritorio\\AVANCE1\\360.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 231, 61))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Comic Sans MS\";")
        self.label_3.setObjectName("label_3")
        self.cb_list_baudrates = QtWidgets.QComboBox(self.frame_2)
        self.cb_list_baudrates.setGeometry(QtCore.QRect(300, 230, 150, 22))
        self.cb_list_baudrates.setStyleSheet("QComboBox{\n"
"    border: 3px solid rgb(255,255,255);\n"
"    border-radius: 5px;\n"
"    min-width: 6em;\n"
"    color: rgb(255,255,255);\n"
"    font: 87 10pt    \"Arial Black\" ;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width:3px;\n"
"    border-left-color: rgb(255,255,255);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"    background: #2c2c2c;\n"
"    selection-background-color: #ff0037;\n"
"    color: rgb(255,255,255);\n"
"}")
        self.cb_list_baudrates.setObjectName("cb_list_baudrates")
        self.bt_connect = QtWidgets.QPushButton(self.frame_2)
        self.bt_connect.setGeometry(QtCore.QRect(150, 310, 171, 41))
        self.bt_connect.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bt_connect.setStyleSheet("font: 10pt \"Vineta BT\";\n"
"background-color: rgb(255, 255, 255);")
        self.bt_connect.setObjectName("bt_connect")
        self.bt_disconnect = QtWidgets.QPushButton(self.frame_2)
        self.bt_disconnect.setGeometry(QtCore.QRect(120, 380, 231, 41))
        self.bt_disconnect.setStyleSheet("font: 10pt \"Vineta BT\";\n"
"background-color: rgb(255, 255, 255);")
        self.bt_disconnect.setObjectName("bt_disconnect")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 231, 61))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Comic Sans MS\";")
        self.label_4.setObjectName("label_4")
        self.bt_update = QtWidgets.QPushButton(self.frame_2)
        self.bt_update.setGeometry(QtCore.QRect(120, 450, 231, 41))
        self.bt_update.setStyleSheet("font: 10pt \"Vineta BT\";\n"
"background-color: rgb(255, 255, 255);")
        self.bt_update.setObjectName("bt_update")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.camara_frame = QtWidgets.QFrame(self.frame_3)
        self.camara_frame.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.camara_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.camara_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.camara_frame.setObjectName("camara_frame")
        self.label_5 = QtWidgets.QLabel(self.camara_frame)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 231, 61))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Comic Sans MS\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.camara_frame)
        self.label_6.setGeometry(QtCore.QRect(40, 90, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 10pt \"Comic Sans MS\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.camara_frame)
        self.label_7.setGeometry(QtCore.QRect(40, 160, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 10pt \"Comic Sans MS\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.camara_frame)
        self.label_8.setGeometry(QtCore.QRect(40, 230, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 10pt \"Comic Sans MS\";")
        self.label_8.setObjectName("label_8")
        self.save_photo = QtWidgets.QPushButton(self.camara_frame)
        self.save_photo.setGeometry(QtCore.QRect(330, 110, 93, 28))
        self.save_photo.setStyleSheet("font: 10pt \"Vineta BT\";\n"
"background-color: rgb(255, 255, 255);")
        self.save_photo.setObjectName("save_photo")
        self.procesing = QtWidgets.QPushButton(self.camara_frame)
        self.procesing.setGeometry(QtCore.QRect(330, 180, 93, 28))
        self.procesing.setStyleSheet("font: 10pt \"Vineta BT\";\n"
"background-color: rgb(255, 255, 255);")
        self.procesing.setObjectName("procesing")
        self.calculate = QtWidgets.QPushButton(self.camara_frame)
        self.calculate.setGeometry(QtCore.QRect(330, 250, 93, 28))
        self.calculate.setStyleSheet("font: 10pt \"Vineta BT\";\n"
"background-color: rgb(255, 255, 255);")
        self.calculate.setObjectName("calculate")
        self.verticalLayout_3.addWidget(self.camara_frame)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "GRUPO 08"))
        self.label_3.setText(_translate("MainWindow", "VELOCIDAD (BAUNDS)"))
        self.bt_connect.setText(_translate("MainWindow", "CONECTAR"))
        self.bt_disconnect.setText(_translate("MainWindow", "DESCONECTAR"))
        self.label_4.setText(_translate("MainWindow", "PUERTO SERIAL"))
        self.bt_update.setText(_translate("MainWindow", "ACTUALIZAR"))
        self.label_5.setText(_translate("MainWindow", "PROCESO:"))
        self.label_6.setText(_translate("MainWindow", "1. GUARDAR FOTO:"))
        self.label_7.setText(_translate("MainWindow", "2. PROCESAR FOTO:"))
        self.label_8.setText(_translate("MainWindow", "3. CALCULAR DISTANCIA:"))
        self.save_photo.setText(_translate("MainWindow", ">>"))
        self.procesing.setText(_translate("MainWindow", ">>"))
        self.calculate.setText(_translate("MainWindow", ">>"))
