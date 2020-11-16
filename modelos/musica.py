import conexoes.conexao_mongo_musica as conn_mongo
import conexoes.conexao_postgresql as conn_plsql


class Musica:

    def __init__(self, nome, autor, genero):
        self.nome = nome
        self.autor = autor
        self.genero = genero

    def save_mongo(self):
        conn_mongo.save(self.__dict__)

    def save_psql(self):
        conn_plsql.save(self)
