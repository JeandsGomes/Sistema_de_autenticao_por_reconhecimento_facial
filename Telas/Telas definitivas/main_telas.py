import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QImage

from ball_tree import Ball_Tree
from individuo import Individuos
from mongo_db import SGBD
from vgg_faces import Vgg_Faces
from encode_object import CustomEncoder
import bcrypt

#import cv2, imutils
import time
import numpy as np
import numpy as np
import cv2

#faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Importndo as telas
from cadastro_administrador_1_1 import cadastro_adm
from login_administrador_1_1 import login_adm
from menu_inicial_1_0 import menu_inicial
from Cadastro_Individuo_Dados_1_1 import cadastro_individuo_Dados
from Cadastro_Individuo_imagens_1_1 import cadastro_individuo_Imagens
from Reconhecimento_Facial_1_1 import reconhecimento_facial_individuo
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

        self._bd = SGBD()
        self._descritor = Vgg_Faces()
        self._ball_tree = Ball_Tree()
        self._descritor.load_model()
        self._encoder = CustomEncoder()
        self._indviduo = Individuos()
        self._nome_ind = ''
        self._email_ind = ''

        #Botões
        #Tela de login
        self.tela_login_adm.login_pushButton_logar.clicked.connect(self.button_login)
        self.tela_login_adm.login_pushButton_entrar_cadastro.clicked.connect(self.abrir_cadastro_adm)

        #Tela de cadastro
        self.tela_cadastro_adm.cadastro_pushButton_cadastrar.clicked.connect(self.botao_cadastro_adm)
        self.tela_cadastro_adm.cadastro_pushButton_entrar_login.clicked.connect(self.abrir_login_adm)

        #Tela menu_inicil
        self.tela_menu_inicial.cadastro_pushButton.clicked.connect(self.abrir_cadastra_idv_dados)
        self.tela_menu_inicial.reconhecimento_pushButton.clicked.connect(self.reconhecimento_facial)
        self.tela_menu_inicial.Editar_pushButton.clicked.connect(self.editar_individuo)
        self.tela_menu_inicial.sair_pushButton.clicked.connect(self.abrir_login_adm)

        #Tela cadastrar individuos dados
        self.tela_cadastro_idv_dados.cadstrar_idv_dados_pushButton_cadastrar.clicked.connect(self.button_cadastra_indv_dados)
        self.tela_cadastro_idv_dados.cadastrar_idv_pushButton_voltar_menu_inicial.clicked.connect(self.abrir_menu_inicial)

        #Tela cadastro individuos fotos
        # Os outros botoes foram implementados nas suas respectivas telas
        self.tela_cadastro_idv_fotos.cadastrar_pushButton_imagens.clicked.connect(self.cad_ind_imagens)
        self.tela_cadastro_idv_fotos.voltar.clicked.connect(self.button_sair_cad_ind_ima)

        #Tela Reconhecimento Facial de Individuo
        self.tela_rec_facial.rec_facial_pushButton_voltar.clicked.connect(self.voltando_do_rec_facial)

        #Tela Editar Individuo
        #self.tela_edita_individuo.editar_pushButton_buscar.clicked.connect()
        #self.tela_edita_individuo.edita_pushButton_editar.clicked.connect()
        #self.tela_edita_individuo.edita_pushButton_remover.clicked.connect()
        self.tela_edita_individuo.edita_pushButton_voltar.clicked.connect(self.voltando_do_editar_individuo)

    #Funcio
    def insere_uma_administrador(self,email_adm = 'usuario_teste@gmail.com',nome_adm = 'Usuario_Teste',senha_adm = 'qwe123'):
        # Operação e cadastro
        passwd = senha_adm.encode('UTF-8')
        hashpasswd = bcrypt.hashpw(passwd, bcrypt.gensalt(10))

        documento_teste = {
            'Nome': nome_adm,
            'email': email_adm,
            'hashpasswd' : hashpasswd
        }

        self._bd.adm_colection.insert_one(documento_teste)

    def cleaning_registration_adm_fields(self):
        self.tela_cadastro_adm.cadastro_lineEdit_email.setText('')
        self.tela_cadastro_adm.cadastro_lineEdit_nome.setText('')
        self.tela_cadastro_adm.cadastro_lineEdit_senha.setText('')
        self.tela_cadastro_adm.cadastro_lineEdit_conf_senha.setText('')

    def botao_cadastro_adm(self):
        email_adm    = self.tela_cadastro_adm.cadastro_lineEdit_email.text()
        nome_adm     = self.tela_cadastro_adm.cadastro_lineEdit_nome.text()
        senha_adm    = self.tela_cadastro_adm.cadastro_lineEdit_senha.text()
        confir_senha = self.tela_cadastro_adm.cadastro_lineEdit_conf_senha.text()
        if(email_adm != ''and nome_adm != '' and senha_adm != '' and confir_senha != ''):
            adm_teste = self._bd.adm_colection.find_one({'email':email_adm})
            checking_email = adm_teste == None
            if(checking_email):
                checking_password = senha_adm == confir_senha
                if checking_password:
                    self.cleaning_registration_adm_fields()
                    self.insere_uma_administrador(email_adm,nome_adm,senha_adm)
                    QMessageBox.information(None, 'Cadastro do Administrador', 'Cadastro feito com sucesso.')
                else:
                    self.cleaning_registration_adm_fields()
                    QMessageBox.information(None, 'Cadastro do Administrador', 'Confirmação de senha não confere.')
            else:
                self.cleaning_registration_adm_fields()
                QMessageBox.information(None, 'Cadastro do Administrador', 'Esse endereço de email já está em uso por {}.'.format(adm_teste['Nome']))
        else:
            self.cleaning_registration_adm_fields()
            QMessageBox.information(None, 'Cadastro do Administrador', 'Todos os campos devem ser preenchidos.')

    def cleaning_login_adm_fields(self):
        self.tela_login_adm.login_lineEdit_email.setText('')
        self.tela_login_adm.login_lineEdit_senha.setText('')

    def button_login(self):
        email_adm = self.tela_login_adm.login_lineEdit_email.text()
        senha_adm = self.tela_login_adm.login_lineEdit_senha.text()
        adm = self._bd.adm_colection.find_one({'email':email_adm})
        checking_email = adm == None
        if(checking_email):
            self.cleaning_login_adm_fields()
            QMessageBox.information(None, 'Login do Administrador', 'Conta não encontrada.')
        else:
            passwd = senha_adm.encode('UTF-8')
            matched = bcrypt.checkpw(passwd, adm['hashpasswd'])
            self._adm = adm
            if(matched):
                self._id_adm = adm['_id']
                self.cleaning_login_adm_fields()
                QMessageBox.information(None, 'Login do Administrador', 'Bem vindo {}.'.format(self._adm['Nome']))
                self.inicializando_tela__inicial()
                self.tela_menu_inicial.nome_adm.setText('{}'.format(self._adm['Nome']))
            else:
                self.cleaning_login_adm_fields()
                QMessageBox.information(None, 'Login do Administrador', 'Senha ou email errados.')

    def cleaning_login_adm_fields(self):
        self.tela_cadastro_idv_dados.cad_ind_lineEdit_nome.setText('')
        self.tela_cadastro_idv_dados.cad_ind_lineEdit_email.setText('')

    def button_cadastra_indv_dados(self):
        self._nome_ind  = self.tela_cadastro_idv_dados.cad_ind_lineEdit_nome.text()
        self._email_ind = self.tela_cadastro_idv_dados.cad_ind_lineEdit_email.text()
        if(self._nome_ind != '' and self._email_ind != ''):
            indv = self._bd.identity_colection.find_one({'email':self._email_ind})
            if(indv == None):
                QMessageBox.information(None, 'Cadastro do Individuo', 'Dados aceitos.')
                self.abrir_cadastra_idv_fotos()
                self.cleaning_login_adm_fields()
            else:
                QMessageBox.information(None, 'Cadastro do Individuo', 'Esse endereço de email já está em uso por {}.'.format(indv['nome']))
                self.cleaning_login_adm_fields()
        else:
            QMessageBox.information(None, 'Cadastro do Individuo', 'Todos os campos devem ser preenchidos.')
    
    def button_sair_cad_ind_ima(self):
        if(self.tela_cadastro_idv_fotos.flag_captura != 0):
            self.tela_cadastro_idv_fotos.loadImage()
        self.abrir_menu_inicial()

    def insert_to_colection_indentity(self,id_adm,nome,email,img,features):
        test_document = {
            'adm_id': id_adm,
            'nome': nome,
            'email': email,
            'img': img,
            'features': features
        }

        self._bd.identity_colection.insert_one(test_document)

    def insert_to_historic(self,id_ind,data,hora):
        test_document = {
            'ind_id': id_ind,
            'data': data,
            'hora': hora
        }

        self._bd.historic_colection.insert_one(test_document)

    def cad_ind_imagens(self):

        # Amarzenando as imagens
        #--------------------------------------------------------------------------------------------------------------------------------------
        if(self.tela_cadastro_idv_fotos.cont_aramzena_image >= 2):
            # storing first image
            img_right_encode = self._encoder.default(self.tela_cadastro_idv_fotos.armazenando_image_1)
            img = self._indviduo.preprocessamento_img(self.tela_cadastro_idv_fotos.armazenando_image_1)
            features_rifht_encode = self._encoder.default(self._descritor.extracao_de_caracteristicas_1_foto(img))
            self.insert_to_colection_indentity(self._id_adm,self._nome_ind,self._email_ind,img_right_encode,features_rifht_encode)

            # storing second image
            img_right_encode = self._encoder.default(self.tela_cadastro_idv_fotos.armazenando_image_2)
            img = self._indviduo.preprocessamento_img(self.tela_cadastro_idv_fotos.armazenando_image_2)
            features_rifht_encode = self._encoder.default(self._descritor.extracao_de_caracteristicas_1_foto(img))
            self.insert_to_colection_indentity(self._id_adm,self._nome_ind,self._email_ind,img_right_encode,features_rifht_encode)
            
            if(self.tela_cadastro_idv_fotos.cont_aramzena_image == 3):
                # storing third image
                img_right_encode = self._encoder.default(self.tela_cadastro_idv_fotos.armazenando_image_3)
                img = self._indviduo.preprocessamento_img(self.tela_cadastro_idv_fotos.armazenando_image_3)
                features_rifht_encode = self._encoder.default(self._descritor.extracao_de_caracteristicas_1_foto(img))
                self.insert_to_colection_indentity(self._id_adm,self._nome_ind,self._email_ind,img_right_encode,features_rifht_encode)

        # Carregando nova arvor de ball tree
        #--------------------------------------------------------------------------------------------------------------------------------------
            query = {'adm_id':self._id_adm}
            base_treino = []
            for identity in self._bd.identity_colection.find(query):
                print('AQUI >>>>',identity['features'])
                base_treino.append(np.array(identity['features']))
            self._ball_tree.criar_modelo(base_treino,self._id_adm)

        # Limpando lineEdits e voltando para o menu inicial
        #--------------------------------------------------------------------------------------------------------------------------------------
            QMessageBox.information(None, 'Cadastro do Individuo', 'Individuo Cadastrado.')
            self.tela_cadastro_idv_fotos.loadImage()
            self.abrir_menu_inicial()

        else:
            QMessageBox.information(None, 'Cadastro do Individuo', 'É nescessario tirar almenos 2 fotos.')

    # Inicialização da tela de Reconhecimento facial
    def reconhecimento_facial(self):
        self.abrir_rec_facial_idv()
        self._ball_tree.carregar_modelo(self._id_adm)
        self.tela_rec_facial.load_metodos(self._indviduo.preprocessamento_img,self._descritor.extracao_de_caracteristicas_1_foto,self._ball_tree.identificar_individuo,self._encoder.default,self._bd.identity_colection)
        self.tela_rec_facial.loadImage()

    def lead_historic_table_first_menu(self):
        row = 0
        historico = []
        for data in self._bd._historic_colection.find():
            query = {'_id': data['ind_id']}
            individuo = self._bd.identity_colection.find_one(query)
            if(str(self._id_adm) == str(individuo['adm_id'])):
                data['nome'] = individuo['nome']
                data['email'] = individuo['email']
                historico.append(data)

        self.tela_menu_inicial.indiv_cadastrados_tableWidget.setRowCount(len(historico))
        for data_row in historico:
            self._bd.identity_colection.find_one()
            self.tela_menu_inicial.indiv_cadastrados_tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data_row['_id'])))
            self.tela_menu_inicial.indiv_cadastrados_tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data_row['nome']))
            self.tela_menu_inicial.indiv_cadastrados_tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(data_row['email']))
            self.tela_menu_inicial.indiv_cadastrados_tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(data_row['data']))
            self.tela_menu_inicial.indiv_cadastrados_tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(data_row['hora']))
            row += 1

    def voltando_do_rec_facial(self):
        self.abrir_menu_inicial()
        self.tela_rec_facial.loadImage()
        for data_dict in self.tela_rec_facial.historic:
            print('Entrou aqui')
            query = {'email': data_dict['Email']}
            indv = self._bd.identity_colection.find_one(query)
            self.insert_to_historic(indv['_id'],data_dict['Data'],data_dict['Hora'])
        self.tela_rec_facial.historic = []
        self.tela_rec_facial.load_historic_table()
        self.tela_rec_facial.nome = ''
        self.tela_rec_facial.rec_facial_label_id.setText('...')
        self.tela_rec_facial.rec_facial_label_nome.setText('...')
        self.tela_rec_facial.rec_facial_label_email.setText('...')
        self.lead_historic_table_first_menu()

    def editar_individuo(self):
        self.tela_edita_individuo.load_metodos(self._bd.identity_colection)
        self.abrir_editar_idv()

    def voltando_do_editar_individuo(self):
        self.lead_historic_table_first_menu()
        self.abrir_menu_inicial()

    def inicializando_tela__inicial(self):
        self.lead_historic_table_first_menu()
        self.abrir_menu_inicial()

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
