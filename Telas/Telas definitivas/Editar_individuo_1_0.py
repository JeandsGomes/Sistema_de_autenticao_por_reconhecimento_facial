# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Editar_individuo_1.0.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class editar_individuo(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(878, 540)
        MainWindow.setStyleSheet("background-color: rgb(242, 242, 242)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(349, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        self.label_5.setMinimumSize(QtCore.QSize(125, 0))
        self.label_5.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(348, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame_7)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(502, 300))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edita_pushButton_voltar = QtWidgets.QPushButton(self.frame_5)
        self.edita_pushButton_voltar.setMinimumSize(QtCore.QSize(60, 20))
        self.edita_pushButton_voltar.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.edita_pushButton_voltar.setFont(font)
        self.edita_pushButton_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edita_pushButton_voltar.setStyleSheet("QPushButton{\n"
"    border-radius: 10px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(0, 0, 0);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(42, 42, 42);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.edita_pushButton_voltar.setObjectName("edita_pushButton_voltar")
        self.horizontalLayout_3.addWidget(self.edita_pushButton_voltar)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.frame_7)
        self.frame.setMinimumSize(QtCore.QSize(300, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addWidget(self.frame_3)
        self.login_lineEdit_cpf_3 = QtWidgets.QLineEdit(self.frame)
        self.login_lineEdit_cpf_3.setMinimumSize(QtCore.QSize(0, 50))
        self.login_lineEdit_cpf_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.login_lineEdit_cpf_3.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 2px;")
        self.login_lineEdit_cpf_3.setInputMask("")
        self.login_lineEdit_cpf_3.setText("")
        self.login_lineEdit_cpf_3.setObjectName("login_lineEdit_cpf_3")
        self.verticalLayout.addWidget(self.login_lineEdit_cpf_3)
        self.editar_pushButton_buscar = QtWidgets.QPushButton(self.frame)
        self.editar_pushButton_buscar.setMinimumSize(QtCore.QSize(0, 50))
        self.editar_pushButton_buscar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.editar_pushButton_buscar.setFont(font)
        self.editar_pushButton_buscar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editar_pushButton_buscar.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(0, 0, 0);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(42, 42, 42);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.editar_pushButton_buscar.setObjectName("editar_pushButton_buscar")
        self.verticalLayout.addWidget(self.editar_pushButton_buscar)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout.addWidget(self.frame_4)
        self.login_lineEdit_cpf_5 = QtWidgets.QLineEdit(self.frame)
        self.login_lineEdit_cpf_5.setMinimumSize(QtCore.QSize(0, 50))
        self.login_lineEdit_cpf_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.login_lineEdit_cpf_5.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 2px;")
        self.login_lineEdit_cpf_5.setInputMask("")
        self.login_lineEdit_cpf_5.setText("")
        self.login_lineEdit_cpf_5.setObjectName("login_lineEdit_cpf_5")
        self.verticalLayout.addWidget(self.login_lineEdit_cpf_5)
        self.login_lineEdit_cpf_4 = QtWidgets.QLineEdit(self.frame)
        self.login_lineEdit_cpf_4.setMinimumSize(QtCore.QSize(0, 50))
        self.login_lineEdit_cpf_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.login_lineEdit_cpf_4.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 2px;")
        self.login_lineEdit_cpf_4.setInputMask("")
        self.login_lineEdit_cpf_4.setText("")
        self.login_lineEdit_cpf_4.setObjectName("login_lineEdit_cpf_4")
        self.verticalLayout.addWidget(self.login_lineEdit_cpf_4)
        self.edita_pushButton_editar = QtWidgets.QPushButton(self.frame)
        self.edita_pushButton_editar.setMinimumSize(QtCore.QSize(0, 50))
        self.edita_pushButton_editar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.edita_pushButton_editar.setFont(font)
        self.edita_pushButton_editar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edita_pushButton_editar.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(0, 0, 0);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(42, 42, 42);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.edita_pushButton_editar.setObjectName("edita_pushButton_editar")
        self.verticalLayout.addWidget(self.edita_pushButton_editar)
        self.edita_pushButton_remover = QtWidgets.QPushButton(self.frame)
        self.edita_pushButton_remover.setMinimumSize(QtCore.QSize(0, 50))
        self.edita_pushButton_remover.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.edita_pushButton_remover.setFont(font)
        self.edita_pushButton_remover.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edita_pushButton_remover.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(0, 0, 0);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(42, 42, 42);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.edita_pushButton_remover.setObjectName("edita_pushButton_remover")
        self.verticalLayout.addWidget(self.edita_pushButton_remover)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.frame_7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Editar Cadastro"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Data"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Hora"))
        self.edita_pushButton_voltar.setText(_translate("MainWindow", "<< Voltar"))
        self.label_3.setText(_translate("MainWindow", "Buscar"))
        self.login_lineEdit_cpf_3.setPlaceholderText(_translate("MainWindow", "    email"))
        self.editar_pushButton_buscar.setText(_translate("MainWindow", "buscar"))
        self.label_4.setText(_translate("MainWindow", "Editar"))
        self.login_lineEdit_cpf_5.setPlaceholderText(_translate("MainWindow", "    nome"))
        self.login_lineEdit_cpf_4.setPlaceholderText(_translate("MainWindow", "    email"))
        self.edita_pushButton_editar.setText(_translate("MainWindow", "editar"))
        self.edita_pushButton_remover.setText(_translate("MainWindow", "remover"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = editar_individuo()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

