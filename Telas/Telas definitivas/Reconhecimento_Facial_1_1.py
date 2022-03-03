# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Reconhecimento_Facial_1.0.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import QCoreApplication

from PyQt5.QtGui import QImage
import imutils
import cv2
import time
import numpy as np
faceCascade = cv2.CascadeClassifier('../../modelos_e_XLM/haarcascade_frontalface_default.xml')
import numpy as np
from sklearn.neighbors import BallTree

from datetime import datetime

class reconhecimento_facial_individuo(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(878, 545)
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
        self.label_5.setMinimumSize(QtCore.QSize(210, 0))
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
        self.horizontalLayout.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame_7)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.display_camera = QtWidgets.QLabel(self.frame_2)
        self.display_camera.setMinimumSize(QtCore.QSize(502, 300))
        self.display_camera.setText("")
        self.display_camera.setPixmap(QtGui.QPixmap("../../imagens/Frame 1.png"))
        self.display_camera.setObjectName("display_camera")
        self.verticalLayout_3.addWidget(self.display_camera)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rec_facial_pushButton_voltar = QtWidgets.QPushButton(self.frame_5)
        self.rec_facial_pushButton_voltar.setMinimumSize(QtCore.QSize(60, 20))
        self.rec_facial_pushButton_voltar.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rec_facial_pushButton_voltar.setFont(font)
        self.rec_facial_pushButton_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rec_facial_pushButton_voltar.setStyleSheet("QPushButton{\n"
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
        self.rec_facial_pushButton_voltar.setObjectName("rec_facial_pushButton_voltar")
        self.horizontalLayout_3.addWidget(self.rec_facial_pushButton_voltar)
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
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 98))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.individuo_identificado = QtWidgets.QLabel(self.frame_10)
        self.individuo_identificado.setMinimumSize(QtCore.QSize(91, 86))
        self.individuo_identificado.setMaximumSize(QtCore.QSize(70, 70))
        self.individuo_identificado.setText("")
        self.individuo_identificado.setPixmap(QtGui.QPixmap("../../imagens/Frame 19 (1).png"))
        self.individuo_identificado.setObjectName("individuo_identificado")
        self.horizontalLayout_4.addWidget(self.individuo_identificado)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout.addWidget(self.frame_10)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 75))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(20, 40, 53, 13))
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setMaximumSize(QtCore.QSize(100, 16777215))
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
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 53, 13))
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setMaximumSize(QtCore.QSize(100, 16777215))
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
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(20, 0, 53, 13))
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
        self.rec_facial_label_id = QtWidgets.QLabel(self.frame_4)
        self.rec_facial_label_id.setGeometry(QtCore.QRect(90, 0, 201, 16))
        self.rec_facial_label_id.setMinimumSize(QtCore.QSize(0, 0))
        self.rec_facial_label_id.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rec_facial_label_id.setFont(font)
        self.rec_facial_label_id.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.rec_facial_label_id.setObjectName("rec_facial_label_id")
        self.rec_facial_label_nome = QtWidgets.QLabel(self.frame_4)
        self.rec_facial_label_nome.setGeometry(QtCore.QRect(90, 20, 211, 16))
        self.rec_facial_label_nome.setMinimumSize(QtCore.QSize(0, 0))
        self.rec_facial_label_nome.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rec_facial_label_nome.setFont(font)
        self.rec_facial_label_nome.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.rec_facial_label_nome.setObjectName("rec_facial_label_nome")
        self.rec_facial_label_email = QtWidgets.QLabel(self.frame_4)
        self.rec_facial_label_email.setGeometry(QtCore.QRect(90, 40, 211, 16))
        self.rec_facial_label_email.setMinimumSize(QtCore.QSize(0, 0))
        self.rec_facial_label_email.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rec_facial_label_email.setFont(font)
        self.rec_facial_label_email.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.rec_facial_label_email.setObjectName("rec_facial_label_email")
        self.verticalLayout.addWidget(self.frame_4)
        self.rec_facial_tableWidget_mini_historico = QtWidgets.QTableWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rec_facial_tableWidget_mini_historico.sizePolicy().hasHeightForWidth())
        self.rec_facial_tableWidget_mini_historico.setSizePolicy(sizePolicy)
        self.rec_facial_tableWidget_mini_historico.setMinimumSize(QtCore.QSize(290, 200))
        self.rec_facial_tableWidget_mini_historico.setMaximumSize(QtCore.QSize(302, 199))
        self.rec_facial_tableWidget_mini_historico.setObjectName("rec_facial_tableWidget_mini_historico")
        self.rec_facial_tableWidget_mini_historico.setColumnCount(3)
        self.rec_facial_tableWidget_mini_historico.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.rec_facial_tableWidget_mini_historico.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.rec_facial_tableWidget_mini_historico.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.rec_facial_tableWidget_mini_historico.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.rec_facial_tableWidget_mini_historico)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.frame_7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Adicionar codigo aqui
        self.tmp = None # Onde sera armazenado a imagem do dysplay
        self.fps=0
        self.started = False

        self.armazenando_image = None #1° Imagens capturadas do rosto
        self.captura = None

        #self.rec_facial_tableWidget_mini_historico.setColumnWidth(0,400)
        #self.rec_facial_tableWidget_mini_historico.setColumnWidth(1,100)
        #self.rec_facial_tableWidget_mini_historico.setColumnWidth(2,100)

        self._nome = ''
        self._historic = []
        self._cont_frame = 0


    # Carregar metodos nescessarios para realizar a identificação de um individuo
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,new_nome):
        self._nome = new_nome

    def load_metodos(self,metodo_pre_processamento,metodo_extracao_caract,metodo_identificador,encode,colecao_identidades):
        self.metodo_pre_processamento = metodo_pre_processamento
        self.metodo_extracao_caract = metodo_extracao_caract
        self.metodo_identificador = metodo_identificador
        self.encode = encode
        self.colecao_identidades = colecao_identidades

    def identificar_individuo(self,img_individuo):
        img = self.metodo_pre_processamento(img_individuo)
        features_ind = self.metodo_extracao_caract(img)
        #print('>>>>TAMANHO>>>>',features_ind.shape)
        #features_ind_encode = self.encode(features_ind)
        index = self.metodo_identificador(features_ind)
        cont = 0
        print('AQUI >>>>>>',index[1][0])
        if(index[1][0] <= 50):
            for individuo in self.colecao_identidades.find():
                cont += 1
                if(cont == index[0][0]):
                    return individuo
        return None

    def store_data_in_historic(self,email):
        objeto_data_time = datetime.now()
        data_hora_now = objeto_data_time.strftime('%d/%m/%Y %H:%M')
        result= data_hora_now.split()
        dict = {'Email':email,'Data':result[0],'Hora':result[1]}
        print(dict)
        self._historic.append(dict)
        
    def load_historic_table(self):
        
        row = 0
        self.rec_facial_tableWidget_mini_historico.setRowCount(len(self._historic))
        for data_row in self._historic:
            self.rec_facial_tableWidget_mini_historico.setItem(row, 0, QtWidgets.QTableWidgetItem(data_row['Email']))
            self.rec_facial_tableWidget_mini_historico.setItem(row, 1, QtWidgets.QTableWidgetItem(data_row['Data']))
            self.rec_facial_tableWidget_mini_historico.setItem(row, 2, QtWidgets.QTableWidgetItem(data_row['Hora']))
            row += 1
        
    @property
    def historic(self):
        return self._historic

    @historic.setter
    def historic(self,new_historic):
        self._historic = new_historic

    def loadImage(self):
        """
            Esta função inicializara a camera Inicializar a camera.
            :return:
        """
        if self.started:
            self.started = False
            self.armazenando_image = None  # 1° Imagens capturadas do rosto
            image_ind = cv2.imread("../../imagens/Frame 19 (1).png")
            self.setPhoto(self.individuo_identificado,image_ind,h=90,w=90)
            self.flag_captura = 0
        else:
            self.flag_captura = 1
            self.started = True



        cam = True #Possui WebCam
        if cam:
            vid = cv2.VideoCapture(0)

        cnt = 0
        frames_to_count=20
        st = 0
        fps = 0

        while(vid.isOpened()):
            img, self.image = vid.read()
            self.image = imutils.resize(self.image, width=502, height=300)

            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.15,
                    minNeighbors=7,
                    minSize=(80, 80),
                    flags=cv2.CASCADE_SCALE_IMAGE)

            maior_dimencao = 0
            x_p = None
            for (x,y,w,h) in faces:
                if(maior_dimencao <= 2**((x-x+w) * (y-y+h))):
                        x_p = x
                        y_p = y
                        w_p = w
                        h_p = h
                        maior_dimencao = 2**((x-x+w) * (y-y+h))
                        #print('-- CAPTURA --',type(captura))
                        #print('-- IMAGEM --', type(self.image))        
            if x_p != None:

                self.captura = self.image[y_p:y_p + h_p, x_p:x_p + w_p]
                cv2.rectangle(self.image, (x_p, y_p), (x_p + w_p, y_p + h_p), (20, 255, 57), 5)
                #print('>>>>>AQUI>>>>>',self.captura)


                self._cont_frame += 1
                if(self._cont_frame == 15):
                    info=self.identificar_individuo(self.captura)
                    print('1.TRUE >>>>>>>> info != None', info != None)
                    self._cont_frame = 0
                    if(info != None):
                        print('2.TRUE >>>>>>>> self._nome == nada ',self._nome == '')
                        print('3.TRUE >>>>>>>> self._nome != info[nome]',self._nome != info['nome'])
                        if((self._nome == '' or self._nome != info['nome'])):
                            self.rec_facial_label_id.setText(str(info['_id']))
                            self.rec_facial_label_nome.setText(info['nome'])
                            self.rec_facial_label_email.setText(info['email'])
                            self.setPhoto(self.individuo_identificado,np.array(info['img'],np.uint8),h=90,w=90)
                            self._nome = info['nome']
                            #print('!!!!!!ENTROU AQUI!!!!!!')
                            self.store_data_in_historic(info['email'])
                            self.load_historic_table()


                    #cv2.circle(self.image,(x_p, y_p),10,(255, 0, 0), 3)
                    #cv2.circle(self.image,(w_p+x, h_p+y),10, (0, 0, 255), 3)

                    #Armazenar as imagens dos rostos detectados
                    #Armazenar as imagens dos rostos detectados


            if cnt == frames_to_count:
                try:  # To avoid divide by 0 we put it in try except
                    print(frames_to_count / (time.time() - st), 'FPS')
                    self.fps = round(frames_to_count / (time.time() - st))

                    st = time.time()
                    cnt = 0
                except:
                    pass
            cnt+=1

            self.update()

            key = cv2.waitKey(1) & 0xFF
            if self.started == False:
                    self.image = cv2.imread("../../imagens/Frame 1.png")
                    #self.update()
                    self.setPhoto(self.display_camera,self.image)
                    break #Loop break

    def setPhoto(self,display,image,h=300, w=502):
            
        """
            Essa função vair utilizar a imagem passadapor parametro realizar o
            preprocessamento ajustando seu diametro e inserindo no display da
            da interface.
            :param image:
            :return:
        """
        self.tmp = image
        image = imutils.resize(image, height=h, width=w)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        display.setPixmap(QtGui.QPixmap.fromImage(image))

    def setPhoto_imagem(self,image,flag):
        """
            Essa função vair utilizar a imagem passadapor parametro realizar o
            preprocessamento ajustando seu diametro e inserindo no display da
            da interface.
            :param image:
            :return:
        """
        #self.tmp = image
        image_copy = image
        image = imutils.resize(image, height=90, width=90)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        image_flag = cv2.imread("../../imagens/Group 143.png")
        #cv2.imwrite('teste_2.png', image)

        if flag == 0:
            self.armazenando_image_1 = image_copy
            self.image_1.setPixmap(QtGui.QPixmap.fromImage(image))
            self.setPhoto(self.flag_foto_1,image_flag,h=27,w=24)
            #QMessageBox.information(None, 'Foto Captuirada', 'Captura da 1 foto!')
        if flag == 1:
            self.armazenando_image_2 = image_copy
            self.Image_2.setPixmap(QtGui.QPixmap.fromImage(image))
            self.setPhoto(self.flag_foto_2,image_flag,h=27,w=24)
            #QMessageBox.information(None, 'Foto Captuirada', 'Captura da 2 foto!')
        if flag == 2:
            self.armazenando_image_3 = image_copy
            self.Image_3.setPixmap(QtGui.QPixmap.fromImage(image))
            self.setPhoto(self.flag_foto_3,image_flag,h=27,w=24)
            #QMessageBox.information(None, 'Foto Captuirada', 'Captura da 3 foto!')


    def update(self):
        """

            :return:
        """
        img = self.image
        #text = 'FPS: '+str(self.fps)
        #img = ps.putBText(img,text,text_offset_x=20,text_offset_y=30,vspace=20,hspace=10, font_scale=1.0,background_RGB=(10,20,222),text_RGB=(255,255,255))
        #text = str(time.strftime("%H:%M %p"))
        #img = ps.putBText(img, text, text_offset_x=self.image.shape[1] - 180, text_offset_y=30, vspace=20, hspace=10,
                          #font_scale=1.0, background_RGB=(228, 20, 222), text_RGB=(255, 255, 255))

        self.setPhoto(self.display_camera,img)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Identificação do Individuo"))
        self.rec_facial_pushButton_voltar.setText(_translate("MainWindow", "<< Voltar"))
        self.label_3.setText(_translate("MainWindow", "Individuo"))
        self.label_7.setText(_translate("MainWindow", "Email:"))
        self.label_6.setText(_translate("MainWindow", "Nome:"))
        self.label_4.setText(_translate("MainWindow", "ID:"))
        self.rec_facial_label_id.setText(_translate("MainWindow", "..."))
        self.rec_facial_label_nome.setText(_translate("MainWindow", "..."))
        self.rec_facial_label_email.setText(_translate("MainWindow", "..."))
        item = self.rec_facial_tableWidget_mini_historico.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.rec_facial_tableWidget_mini_historico.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Data"))
        item = self.rec_facial_tableWidget_mini_historico.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Hora"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = reconhecimento_facial_individuo()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())