import email
from ball_tree import Ball_Tree
from individuo import Individuos
from mongo_db import SGBD
#from vgg_faces import Vgg_Faces
import bcrypt


bd = SGBD()

# Operação e cadastro
nome_adm = 'Usuario_Teste'
email_adm = 'usuario_teste@gmail.com'
senha_adm = 'qwe123'
passwd = senha_adm.encode('UTF-8')
hashpasswd = bcrypt.hashpw(passwd, bcrypt.gensalt(10))

documento_teste = {
    'Nome': nome_adm,
    'email': email_adm,
    'hashpasswd' : hashpasswd
}

bd.adm_colection.insert_one(documento_teste)


# Leitura de hashpasswd no banco de dados
email_adm = 'usuario_teste@gmail.com'
query = {'email':email_adm}
conta = bd.adm_colection.find_one(query)

senha_adm = 'qwe123'
passwd = senha_adm.encode('UTF-8')
matched = bcrypt.checkpw(passwd, conta['hashpasswd'])

print('Conicide:',matched)