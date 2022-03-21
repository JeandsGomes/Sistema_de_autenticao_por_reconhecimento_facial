from sklearn.neighbors import BallTree
import numpy as np
import pickle
import os


class Ball_Tree():
    def __init__(self,tree = None):
        self._tree = tree
        
    @property
    def tree(self):
        return self._tree

    @tree.setter
    def tree(self,new_tree):
        self._tree = new_tree

    # Cria uma arvore nova a partir da base de trenho
    def criar_modelo(self,base_de_treino,id_adm):
        novo_treino = np.array(base_de_treino)
        tree = BallTree(novo_treino, leaf_size=2)
        self._tree = tree
        pickle.dump(self._tree,open('../../../{}.sav'.format(str(id_adm)),'wb'))
        return tree
        
    # Realiza a identificação de 1 imagem usando o tree carregada
    def identificar_individuo(self,individuo,model = None):

        if model == None:
            model = self._tree

        novo_individuo = [np.array(individuo)]
        dist, ind = model.query(novo_individuo, k=10)
        return [ind[0],dist[0]]

    # Carrega o modelo salvo usando id do adm como chave
    def carregar_modelo(self,id_adm):
        if('{}.sav'.format(str(id_adm)) in os.listdir('../../../')):
            self._tree = pickle.load(open('../../../{}.sav'.format(id_adm),'rb'))
