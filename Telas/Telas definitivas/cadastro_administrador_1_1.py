# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\cadastro_administrador_1.0.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class cadastro_adm(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 547)
        MainWindow.setMinimumSize(QtCore.QSize(370, 547))
        MainWindow.setMaximumSize(QtCore.QSize(370, 16777215))
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
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cadastro_lineEdit_email = QtWidgets.QLineEdit(self.frame_4)
        self.cadastro_lineEdit_email.setMinimumSize(QtCore.QSize(0, 50))
        self.cadastro_lineEdit_email.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cadastro_lineEdit_email.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 2px;")
        self.cadastro_lineEdit_email.setInputMask("")
        self.cadastro_lineEdit_email.setText("")
        self.cadastro_lineEdit_email.setObjectName("cadastro_lineEdit_email")
        self.verticalLayout_2.addWidget(self.cadastro_lineEdit_email)
        self.cadastro_lineEdit_nome = QtWidgets.QLineEdit(self.frame_4)
        self.cadastro_lineEdit_nome.setMinimumSize(QtCore.QSize(0, 50))
        self.cadastro_lineEdit_nome.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cadastro_lineEdit_nome.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 2px;")
        self.cadastro_lineEdit_nome.setInputMask("")
        self.cadastro_lineEdit_nome.setText("")
        self.cadastro_lineEdit_nome.setObjectName("cadastro_lineEdit_nome")
        self.verticalLayout_2.addWidget(self.cadastro_lineEdit_nome)
        self.cadastro_lineEdit_senha = QtWidgets.QLineEdit(self.frame_4)
        self.cadastro_lineEdit_senha.setMinimumSize(QtCore.QSize(0, 50))
        self.cadastro_lineEdit_senha.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 2px;")
        self.cadastro_lineEdit_senha.setInputMask("")
        self.cadastro_lineEdit_senha.setText("")
        self.cadastro_lineEdit_senha.setObjectName("cadastro_lineEdit_senha")

        # ocultando a senha
        self.cadastro_lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.cadastro_lineEdit_senha)
        self.cadastro_lineEdit_conf_senha = QtWidgets.QLineEdit(self.frame_4)
        self.cadastro_lineEdit_conf_senha.setMinimumSize(QtCore.QSize(0, 50))
        self.cadastro_lineEdit_conf_senha.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cadastro_lineEdit_conf_senha.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 2px;")
        self.cadastro_lineEdit_conf_senha.setInputMask("")
        self.cadastro_lineEdit_conf_senha.setText("")
        self.cadastro_lineEdit_conf_senha.setObjectName("cadastro_lineEdit_conf_senha")

        # ocultando a senha
        self.cadastro_lineEdit_conf_senha.setEchoMode(QtWidgets.QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.cadastro_lineEdit_conf_senha)
        self.cadastro_pushButton_cadastrar = QtWidgets.QPushButton(self.frame_4)
        self.cadastro_pushButton_cadastrar.setMinimumSize(QtCore.QSize(0, 50))
        self.cadastro_pushButton_cadastrar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cadastro_pushButton_cadastrar.setFont(font)
        self.cadastro_pushButton_cadastrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cadastro_pushButton_cadastrar.setStyleSheet("QPushButton{\n"
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
        self.cadastro_pushButton_cadastrar.setObjectName("cadastro_pushButton_cadastrar")
        self.verticalLayout_2.addWidget(self.cadastro_pushButton_cadastrar)
        self.verticalLayout.addWidget(self.frame_4)
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
        self.label_4 = QtWidgets.QLabel(self.frame_2)
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
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cadastro_pushButton_entrar_login = QtWidgets.QPushButton(self.frame_5)
        self.cadastro_pushButton_entrar_login.setMaximumSize(QtCore.QSize(300, 16777215))
        self.cadastro_pushButton_entrar_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cadastro_pushButton_entrar_login.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"    \n"
"    color: rgb(0,127,255);\n"
"}\n"
"\n"
"\n"
"")
        self.cadastro_pushButton_entrar_login.setObjectName("cadastro_pushButton_entrar_login")
        self.horizontalLayout_4.addWidget(self.cadastro_pushButton_entrar_login)
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "♠ Cadastro ♠"))
        self.cadastro_lineEdit_email.setPlaceholderText(_translate("MainWindow", "    email"))
        self.cadastro_lineEdit_nome.setPlaceholderText(_translate("MainWindow", "    nome"))
        self.cadastro_lineEdit_senha.setPlaceholderText(_translate("MainWindow", "    senha"))
        self.cadastro_lineEdit_conf_senha.setPlaceholderText(_translate("MainWindow", "    confirmar senha"))
        self.cadastro_pushButton_cadastrar.setText(_translate("MainWindow", "cadastrar"))
        self.label_6.setText(_translate("MainWindow", "_________________"))
        self.label_4.setText(_translate("MainWindow", "ou"))
        self.label_5.setText(_translate("MainWindow", "_________________"))
        self.cadastro_pushButton_entrar_login.setText(_translate("MainWindow", "Já possui conta ? Entrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = cadastro_adm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())