import pymongo

class SGBD():
    def __init__(self):
        connection_url = "mongodb://localhost:27017"
        self.client = pymongo.MongoClient(connection_url)
        database_name = "Reconhecimento_Facial"
        self._DataBase = self.client[database_name]
        
        adm_colction_name = "Manager"
        self._adm_colection = self._DataBase[adm_colction_name]

        identity_colction_name = "Identity"
        self._identity_colection = self._DataBase[identity_colction_name]

        historic_colction_name = "Historic"
        self._historic_colection = self._DataBase[historic_colction_name]


        self.administrador = {}

    @property
    def DataBase(self):
        return self._DataBase
    
    @DataBase.setter
    def DataBase(self,new_DataBase):
        self._DataBase = new_DataBase
        
    @property
    def adm_colection(self):
        return self._adm_colection
    
    @adm_colection.setter
    def adm_colection(self,new_adm_colection):
        self._adm_colection = new_adm_colection

    @property
    def identity_colection(self):
        return self._identity_colection

    @identity_colection.setter
    def identity_colection(self,new_identity_colection):
        self._identity_colection = new_identity_colection

    @property
    def historic_colection(self):
        return self._historic_colection

    @historic_colection.setter
    def historic_colection(self,new_historic_colection):
        self._historic_colection = new_historic_colection

    def close_bd(self):
        self.client.close()
    