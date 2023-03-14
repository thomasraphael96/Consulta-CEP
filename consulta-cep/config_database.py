import sqlite3
import time

seconds = 2

# classe de endereços
class Endereco(object):

    def __init__(self):
        self.cep = None
        self.logradouro = None
        self.bairro = None
        self.localidade = None
        self.uf = None
        self.ddd = None

# método para criar a tabela "enderecos" caso ela não exista
    def criar_tabela(self):
        conn = sqlite3.connect("via_cep.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tb_endereco (
            cep text, logradouro text, bairro text, cidade text,
            uf text, ddd text
            )
            """
        )

        conn.commit()

# método para inserir os dados na tabela "enderecos" do banco de dados "via_cep"
    def inserir_dados(self):
        
        self.criar_tabela()

        conn = sqlite3.connect("via_cep.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO enderecos VALUES('%s','%s','%s','%s','%s','%s')
            """
            %(self.cep, self.logradouro, self.bairro, self.localidade, self.uf, self.ddd)
        )

        conn.commit()

        time.sleep(seconds)

        print("Informações de endereço salvas no banco de dados")
