from keras.applications.imagenet_utils import preprocess_input
import numpy as np
import cv2

class Individuos():
    
    def __init__(self):
        self._individuos = dict() # Logal onde vou aramzenar os dados 
    
    @property
    def individuos(self):
        return self._individuos

    @individuos.setter
    def individuos(self,new_individuos):
        self._individuos = new_individuos
    
    def carregar_foto(self,image_path):
        img = cv2.imread(image_path)
        #print(img)

        #recorte da face
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + '/haarcascade_frontalface_default.xml')


        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        gray = img
        #filtro Gaussiano
        smooth = cv2.GaussianBlur(gray,((gray.shape[0]//7)|1,(gray.shape[1]//7)|1),0)# D
        gray = cv2.divide(gray, smooth, scale=255)# D

        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            img = img[y:y+h,x:x+w]
            break


        img=cv2.resize(img,(224, 224))

        #plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        #plt.show()


        img = np.array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)

        return img

    def preprocessamento_img(self,img):
        img_processing=cv2.resize(img,(224, 224))
        img_processing = np.array(img_processing)
        img_processing = np.expand_dims(img_processing, axis=0)
        img_processing = preprocess_input(img_processing)
        return img_processing
    
    def adicionar_individuo(self,identificador,img,caracteristicas):
        self._individuos[identificador] = [img,caracteristicas]
        