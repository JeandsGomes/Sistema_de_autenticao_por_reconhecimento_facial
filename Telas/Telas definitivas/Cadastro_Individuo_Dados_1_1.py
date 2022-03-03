# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Cadastro_Individuo_Dados_1.0.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class cadastro_individuo_Dados(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 547)
        MainWindow.setMinimumSize(QtCore.QSize(370, 547))
        MainWindow.setMaximumSize(QtCore.QSize(370, 547))
        MainWindow.setStyleSheet("background-color: rgb(242, 242, 242)\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(250, 0))
        self.frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(349, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_7 = QtWidgets.QLabel(self.frame_8)
        self.label_7.setMinimumSize(QtCore.QSize(185, 0))
        self.label_7.setMaximumSize(QtCore.QSize(108, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        spacerItem1 = QtWidgets.QSpacerItem(348, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 98))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_10)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setMinimumSize(QtCore.QSize(142, 0))
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
        self.horizontalLayout_6.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.cad_ind_lineEdit_nome = QtWidgets.QLineEdit(self.frame_10)
        self.cad_ind_lineEdit_nome.setMinimumSize(QtCore.QSize(0, 50))
        self.cad_ind_lineEdit_nome.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cad_ind_lineEdit_nome.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 2px;")
        self.cad_ind_lineEdit_nome.setInputMask("")
        self.cad_ind_lineEdit_nome.setText("")
        self.cad_ind_lineEdit_nome.setObjectName("cad_ind_lineEdit_nome")
        self.verticalLayout_4.addWidget(self.cad_ind_lineEdit_nome)
        self.cad_ind_lineEdit_email = QtWidgets.QLineEdit(self.frame_10)
        self.cad_ind_lineEdit_email.setMinimumSize(QtCore.QSize(0, 50))
        self.cad_ind_lineEdit_email.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cad_ind_lineEdit_email.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 2px;")
        self.cad_ind_lineEdit_email.setInputMask("")
        self.cad_ind_lineEdit_email.setText("")
        self.cad_ind_lineEdit_email.setObjectName("cad_ind_lineEdit_email")
        self.verticalLayout_4.addWidget(self.cad_ind_lineEdit_email)
        self.cadstrar_idv_dados_pushButton_cadastrar = QtWidgets.QPushButton(self.frame_10)
        self.cadstrar_idv_dados_pushButton_cadastrar.setMinimumSize(QtCore.QSize(0, 50))
        self.cadstrar_idv_dados_pushButton_cadastrar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cadstrar_idv_dados_pushButton_cadastrar.setFont(font)
        self.cadstrar_idv_dados_pushButton_cadastrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cadstrar_idv_dados_pushButton_cadastrar.setStyleSheet("QPushButton{\n"
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
        self.cadstrar_idv_dados_pushButton_cadastrar.setObjectName("cadstrar_idv_dados_pushButton_cadastrar")
        self.verticalLayout_4.addWidget(self.cadstrar_idv_dados_pushButton_cadastrar)
        self.verticalLayout.addWidget(self.frame_10)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cadastrar_idv_pushButton_voltar_menu_inicial = QtWidgets.QPushButton(self.frame_5)
        self.cadastrar_idv_pushButton_voltar_menu_inicial.setMaximumSize(QtCore.QSize(300, 16777215))
        self.cadastrar_idv_pushButton_voltar_menu_inicial.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cadastrar_idv_pushButton_voltar_menu_inicial.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"    \n"
"    color: rgb(0,127,255);\n"
"}\n"
"\n"
"\n"
"")
        self.cadastrar_idv_pushButton_voltar_menu_inicial.setObjectName("cadastrar_idv_pushButton_voltar_menu_inicial")
        self.horizontalLayout_4.addWidget(self.cadastrar_idv_pushButton_voltar_menu_inicial)
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "♠ Cadastrar Individuo ♠"))
        self.label_3.setText(_translate("MainWindow", "Informe os dados"))
        self.cad_ind_lineEdit_nome.setPlaceholderText(_translate("MainWindow", "    nome"))
        self.cad_ind_lineEdit_email.setPlaceholderText(_translate("MainWindow", "    email"))
        self.cadstrar_idv_dados_pushButton_cadastrar.setText(_translate("MainWindow", "Cadastrar Dados"))
        self.label_6.setText(_translate("MainWindow", "_______________________________________________"))
        self.cadastrar_idv_pushButton_voltar_menu_inicial.setText(_translate("MainWindow", "← VOLTAR"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = cadastro_individuo_Dados()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())