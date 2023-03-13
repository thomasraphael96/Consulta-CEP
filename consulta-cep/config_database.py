import sqlite3

# classe de endereços
class Endereco(object):

    def __init__(self):
        self.cep = None
        self.logradouro = None
        self.complemento = None
        self.bairro = None
        self.localidade = None
        self.uf = None
        self.ddd = None
        self.ibge = None
        self.gia = None

# método para criar a tabela "enderecos" caso ela não exista
    def cria_tabela(self):
        conn = sqlite3.connect("via_cep.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS enderecos (
            cep text, logradouro text, complemento text, bairro text, localidade text,
            uf text, ddd text, ibge text, gia text
            )
            """
        )

        conn.commit()

# método para inserir os dados na tabela "enderecos" do banco de dados "via_cep"
    def salvar(self):
        
        self.cria_tabela()

        conn = sqlite3.connect("via_cep.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO enderecos VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')
            """
            %(self.cep, self.logradouro, self.complemento, self.bairro, self.localidade, self.uf, self.ddd, self.ibge, self.gia)
        )

        conn.commit()

        print("Informações de endereço salvas no banco de dados")
