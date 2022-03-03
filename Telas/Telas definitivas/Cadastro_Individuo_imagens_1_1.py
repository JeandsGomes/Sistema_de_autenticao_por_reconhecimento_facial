# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Cadastro_Individuo_imagens1.0.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from PyQt5.QtGui import QImage
import imutils
import cv2
import time
import numpy as np
faceCascade = cv2.CascadeClassifier('../../modelos_e_XLM/haarcascade_frontalface_default.xml')
import numpy as np

class cadastro_individuo_Imagens(object):
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
        self.label_5.setMinimumSize(QtCore.QSize(185, 0))
        self.label_5.setMaximumSize(QtCore.QSize(108, 16777215))
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
        self.display_camera.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
        self.voltar = QtWidgets.QPushButton(self.frame_5)
        self.voltar.setMinimumSize(QtCore.QSize(60, 20))
        self.voltar.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.voltar.setFont(font)
        self.voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.voltar.setStyleSheet("QPushButton{\n"
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
        self.voltar.setObjectName("voltar")
        self.horizontalLayout_3.addWidget(self.voltar)
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
        self.cad_img_pushButton_start_camera = QtWidgets.QPushButton(self.frame)
        self.cad_img_pushButton_start_camera.setMinimumSize(QtCore.QSize(0, 50))
        self.cad_img_pushButton_start_camera.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cad_img_pushButton_start_camera.setFont(font)
        self.cad_img_pushButton_start_camera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cad_img_pushButton_start_camera.setStyleSheet("QPushButton{\n"
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
        self.cad_img_pushButton_start_camera.setObjectName("cad_img_pushButton_start_camera")
        self.verticalLayout.addWidget(self.cad_img_pushButton_start_camera)
        self.cad_img_pushButton_captura = QtWidgets.QPushButton(self.frame)
        self.cad_img_pushButton_captura.setMinimumSize(QtCore.QSize(0, 50))
        self.cad_img_pushButton_captura.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cad_img_pushButton_captura.setFont(font)
        self.cad_img_pushButton_captura.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cad_img_pushButton_captura.setStyleSheet("QPushButton{\n"
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
        self.cad_img_pushButton_captura.setObjectName("cad_img_pushButton_captura")
        self.verticalLayout.addWidget(self.cad_img_pushButton_captura)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayout = QtWidgets.QFormLayout(self.frame_3)
        self.formLayout.setObjectName("formLayout")
        self.image_1 = QtWidgets.QLabel(self.frame_3)
        self.image_1.setMinimumSize(QtCore.QSize(91, 86))
        self.image_1.setMaximumSize(QtCore.QSize(70, 70))
        self.image_1.setText("")
        self.image_1.setPixmap(QtGui.QPixmap("../../imagens/Frame 19 (1).png"))
        self.image_1.setObjectName("image_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.image_1)
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_10)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(121, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.flag_foto_1 = QtWidgets.QLabel(self.frame_10)
        self.flag_foto_1.setMinimumSize(QtCore.QSize(24, 26))
        self.flag_foto_1.setMaximumSize(QtCore.QSize(22, 29))
        self.flag_foto_1.setText("")
        self.flag_foto_1.setPixmap(QtGui.QPixmap("../../imagens/Group 144.png"))
        self.flag_foto_1.setObjectName("flag_foto_1")
        self.horizontalLayout_2.addWidget(self.flag_foto_1)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.frame_10)
        self.Image_2 = QtWidgets.QLabel(self.frame_3)
        self.Image_2.setMinimumSize(QtCore.QSize(91, 86))
        self.Image_2.setMaximumSize(QtCore.QSize(70, 70))
        self.Image_2.setText("")
        self.Image_2.setPixmap(QtGui.QPixmap("../../imagens/Frame 19 (1).png"))
        self.Image_2.setObjectName("Image_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Image_2)
        self.frame_12 = QtWidgets.QFrame(self.frame_3)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.frame_12)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setMaximumSize(QtCore.QSize(121, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.flag_foto_2 = QtWidgets.QLabel(self.frame_12)
        self.flag_foto_2.setMinimumSize(QtCore.QSize(24, 26))
        self.flag_foto_2.setMaximumSize(QtCore.QSize(22, 29))
        self.flag_foto_2.setText("")
        self.flag_foto_2.setPixmap(QtGui.QPixmap("../../imagens/Group 144.png"))
        self.flag_foto_2.setObjectName("flag_foto_2")
        self.horizontalLayout_7.addWidget(self.flag_foto_2)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.frame_12)
        self.Image_3 = QtWidgets.QLabel(self.frame_3)
        self.Image_3.setMinimumSize(QtCore.QSize(91, 86))
        self.Image_3.setMaximumSize(QtCore.QSize(70, 70))
        self.Image_3.setText("")
        self.Image_3.setPixmap(QtGui.QPixmap("../../imagens/Frame 19 (1).png"))
        self.Image_3.setObjectName("Image_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Image_3)
        self.frame_13 = QtWidgets.QFrame(self.frame_3)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_13)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setMaximumSize(QtCore.QSize(121, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.flag_foto_3 = QtWidgets.QLabel(self.frame_13)
        self.flag_foto_3.setMinimumSize(QtCore.QSize(24, 26))
        self.flag_foto_3.setMaximumSize(QtCore.QSize(22, 29))
        self.flag_foto_3.setText("")
        self.flag_foto_3.setPixmap(QtGui.QPixmap("../../imagens/Group 144.png"))
        self.flag_foto_3.setObjectName("flag_foto_3")
        self.horizontalLayout_4.addWidget(self.flag_foto_3)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.frame_13)
        self.verticalLayout.addWidget(self.frame_3)
        self.cadastrar_pushButton_imagens = QtWidgets.QPushButton(self.frame)
        self.cadastrar_pushButton_imagens.setMinimumSize(QtCore.QSize(0, 50))
        self.cadastrar_pushButton_imagens.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cadastrar_pushButton_imagens.setFont(font)
        self.cadastrar_pushButton_imagens.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cadastrar_pushButton_imagens.setStyleSheet("QPushButton{\n"
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
        self.cadastrar_pushButton_imagens.setObjectName("cadastrar_pushButton_imagens")
        self.verticalLayout.addWidget(self.cadastrar_pushButton_imagens)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.frame_7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Adicionar codigo aqui
        #self.filename = 'Snapssho '+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png' # Localização da foto que sera salva
        self.tmp = None # Onde sera armazenado a imagem do dysplay
        self.fps=0
        self.started = False

        self.armazenando_image_1 = None #1° Imagens capturadas do rosto
        self.armazenando_image_2 = None #2° Imagens capturadas do rosto
        self.armazenando_image_3= None #3° Imagens capturadas do rosto
        self.captura = None
        self.flag_captura = 0

        self.cont_aramzena_image = 0 #Contador de onde vai ficar a imagem


        self.cad_img_pushButton_start_camera.clicked.connect(self.loadImage)
        self.cad_img_pushButton_captura.clicked.connect(self.captura_face)


    def loadImage(self):
        """
            Esta função inicializara a camera Inicializar a camera.
            :return:
        """
        if self.started:
            self.started = False
            self.cad_img_pushButton_start_camera.setText('Ligar a Camera')
            self.armazenando_image_1 = None  # 1° Imagens capturadas do rosto
            self.armazenando_image_2 = None  # 2° Imagens capturadas do rosto
            self.armazenando_image_3 = None  # 3° Imagens capturadas do rosto
            self.setPhoto_imagem(cv2.imread("../../imagens/Frame 19 (1).png"), 0)
            self.setPhoto_imagem(cv2.imread("../../imagens/Frame 19 (1).png"), 1)
            self.setPhoto_imagem(cv2.imread("../../imagens/Frame 19 (1).png"), 2)
            image_flag = cv2.imread("../../imagens/Group 144.png")
            self.setPhoto(self.flag_foto_1,image_flag,h=27,w=24)
            self.setPhoto(self.flag_foto_2,image_flag,h=27,w=24)
            self.setPhoto(self.flag_foto_3,image_flag,h=27,w=24)
            self.flag_captura = 0
            self.cont_aramzena_image = 0
        else:
            self.flag_captura = 1
            self.started = True
            self.cad_img_pushButton_start_camera.setText('Desligar a Camera')



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

    def captura_face(self):
        try:
            if(self.cont_aramzena_image <= 4):
                self.setPhoto_imagem(self.captura, self.cont_aramzena_image)
                self.cont_aramzena_image += 1
        except:
            pass

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
        self.label_5.setText(_translate("MainWindow", "♠ Cadastrar Individuo ♠"))
        self.voltar.setText(_translate("MainWindow", "<< Voltar"))
        self.cad_img_pushButton_start_camera.setText(_translate("MainWindow", "Ligar a Camera"))
        self.cad_img_pushButton_captura.setText(_translate("MainWindow", "Capturar a imagem"))
        self.label_4.setText(_translate("MainWindow", "Imagem Fontal"))
        self.label_6.setText(_translate("MainWindow", "Olhar Esquerda"))
        self.label_7.setText(_translate("MainWindow", "Olhar Direita"))
        self.cadastrar_pushButton_imagens.setText(_translate("MainWindow", "Cadastrar Individuo"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = cadastro_individuo_Imagens()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

