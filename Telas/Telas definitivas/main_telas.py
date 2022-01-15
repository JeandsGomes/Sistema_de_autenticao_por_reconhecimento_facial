import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QImage
#import cv2, imutils
import time
import numpy as np
import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Importndo as telas
from cadastro_administrador_1_0 import cadastro_adm
from login_administrador_1_0 import login_adm
from menu_inicial_1_0 import menu_inicial
from Cadastro_Individuo_Dados_1_0 import cadastro_individuo_Dados
from Cadastro_Individuo_imagens import cadastro_individuo_Imagens
from Reconhecimento_Facial import reconhecimento_facial_individuo
from Editar_individuo_1_0 import editar_individuo

class Ui_Main(QtWidgets.QWidget):
    '''
    O objeto Ui_Main possibilita ter acesso a todas as telas varias telas.
    '''

    def setupUi(self,Main):

        Main.setObjectName('Main')
        Main.resize(640,480)#tamnaho da tela

        self.QtStack=QtWidgets.QStackedLayout()#cria pilha


        #quantidde de telas
        self.stack0 = QMainWindow()
        self.stack1 = QMainWindow()
        self.stack2 = QMainWindow()
        self.stack3 = QMainWindow()
        self.stack4 = QMainWindow()
        self.stack5 = QMainWindow()
        self.stack6 = QMainWindow()

        #Crindo os objetos par as telas
        self.tela_login_adm = login_adm()
        self.tela_login_adm.setupUi(self.stack0)

        self.tela_cadastro_adm = cadastro_adm()
        self.tela_cadastro_adm.setupUi(self.stack1)

        self.tela_menu_inicial = menu_inicial()
        self.tela_menu_inicial.setupUi(self.stack2)

        self.tela_cadastro_idv_dados = cadastro_individuo_Dados()
        self.tela_cadastro_idv_dados.setupUi(self.stack3)

        self.tela_cadastro_idv_fotos = cadastro_individuo_Imagens()
        self.tela_cadastro_idv_fotos.setupUi(self.stack4)

        self.tela_rec_facial = reconhecimento_facial_individuo()
        self.tela_rec_facial.setupUi(self.stack5)

        self.tela_edita_individuo = editar_individuo()
        self.tela_edita_individuo.setupUi(self.stack6)

        #add ao QtStack
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)


class Main(QMainWindow,Ui_Main):
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        #Botões
        #Tela de login
        self.tela_login_adm.login_pushButton_logar.clicked.connect(self.abrir_menu_inicial)
        self.tela_login_adm.login_pushButton_entrar_cadastro.clicked.connect(self.abrir_cadastro_adm)

        #Tela de cadastro
        #self.tela_cadastro_adm.cadastro_pushButton_cadastrar.clicked.connect()
        self.tela_cadastro_adm.cadastro_pushButton_entrar_login.clicked.connect(self.abrir_login_adm)

        #Tela menu_inicil
        self.tela_menu_inicial.cadastro_pushButton.clicked.connect(self.abrir_cadastra_idv_dados)
        self.tela_menu_inicial.reconhecimento_pushButton.clicked.connect(self.abrir_rec_facial_idv)
        self.tela_menu_inicial.Editar_pushButton.clicked.connect(self.abrir_editar_idv)
        self.tela_menu_inicial.sair_pushButton.clicked.connect(self.abrir_login_adm)

        #Tela cadastrar individuos dados
        self.tela_cadastro_idv_dados.cadstrar_idv_dados_pushButton_cadastrar.clicked.connect(self.abrir_cadastra_idv_fotos)
        self.tela_cadastro_idv_dados.cadastrar_idv_pushButton_voltar_menu_inicial.clicked.connect(self.abrir_menu_inicial)

        #Tela cadastro individuos fotos
        #self.tela_cadastro_idv_fotos.star_camera_pushButton.clicked.connect()
        #self.tela_cadastro_idv_fotos.cadastrar_pushButton_imagens.clicked.connect()
        self.tela_cadastro_idv_fotos.voltar.clicked.connect(self.abrir_menu_inicial)

        #Tela Reconhecimento Facial de Individuo
        self.tela_rec_facial.rec_facial_pushButton_voltar.clicked.connect(self.abrir_menu_inicial)

        #Tela Editar Individuo
        #self.tela_edita_individuo.editar_pushButton_buscar.clicked.connect()
        #self.tela_edita_individuo.edita_pushButton_editar.clicked.connect()
        #self.tela_edita_individuo.edita_pushButton_remover.clicked.connect()
        self.tela_edita_individuo.edita_pushButton_voltar.clicked.connect(self.abrir_menu_inicial)

    #Abrindo as telas
    def abrir_cadastro_adm(self):
        self.QtStack.setCurrentIndex(1)

    def abrir_login_adm(self):
        self.QtStack.setCurrentIndex(0)

    def abrir_menu_inicial(self):
        self.QtStack.setCurrentIndex(2)

    def abrir_cadastra_idv_dados(self):
        self.QtStack.setCurrentIndex(3)

    def abrir_cadastra_idv_fotos(self):
        self.QtStack.setCurrentIndex(4)

    def abrir_rec_facial_idv(self):
        self.QtStack.setCurrentIndex(5)

    def abrir_editar_idv(self):
        self.QtStack.setCurrentIndex(6)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main=Main()
    sys.exit(app.exec_())
