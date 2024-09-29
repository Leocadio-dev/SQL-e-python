import sqlite3 as sqlite

# Criando conexão com o banco (se não existente, cria o banco)
conexao = sqlite.connect("loja.db")

# Criando a conexão para execução de queries
cursor = conexao.cursor()

# O Pragma modifica o comportamento do banco de dados. É preciso ativar as chaves estrangeiras a partir deste código
cursor.execute("PRAGMA foreign_keys = ON")

def criarTabelas():

    # Criando tabela pedido
        
        # Tabela Pedido
        sql = """
                CREATE TABLE IF NOT EXISTS pedido(
                    IDPEDIDO INTEGER PRIMARY KEY AUTOINCREMENT,
                    NUMNOTAFISCAL STRING NOT NULL,
                    VALORTOTAL NUMERIC NOT NULL,
                    DATAPEDIDO DATE NOT NULL,
                    IDCLIENTE INTEGER NOT NULL,
                    CODMERC INTEGER NOT NULL,
                    
                    FOREIGN KEY (IDCLIENTE) REFERENCES cliente(IDCLIENTE),
                    FOREIGN KEY (CODMERC) REFERENCES mercadoria(CODMERC)
                )

        """
        cursor.execute(sql)
     
        # Tabela Mercadoria
        sql = """
                CREATE TABLE IF NOT EXISTS mercadoria(
                    CODMERC INTEGER PRIMARY KEY,
                    DESCMERC STRING NOT NULL,
                    PRECOMERC NUMERIC NOT NULL,
                    QTDESTOQUE INTEGER NOT NULL
                )

        """
        cursor.execute(sql)
        
        # Tabela Cliente
        sql = """
                CREATE TABLE IF NOT EXISTS cliente(
                    IDCLIENTE INTEGER PRIMARY KEY AUTOINCREMENT,
                    CPF STRING NOT NULL,
                    RG STRING,
                    ENDERECO STRING NOT NULL,
                    EMAIL STRING NOT NULL,
                    TELEFONEFIXO STRING,
                    CELULAR STRING NOT NULL
                )

        """
        cursor.execute(sql)

        # Tabela Fornecedor
        sql = """
                CREATE TABLE IF NOT EXISTS fornecedor(
                    CODFORNEC INTEGER PRIMARY KEY,
                    RAZSOC STRING NOT NULL,
                    NOMEFANTASIA STRING NOT NULL,
                    CNPJ STRING NOT NULL,
                    ENDERECO STRING NOT NULL,
                    TELCENTRAL STRING NOT NULL,
                    CODCONTATO INTEGER NOT NULL,
                    
                    FOREIGN KEY (CODCONTATO) REFERENCES contatos(CODCONTATO)
                )

        """
        cursor.execute(sql)
        
        # Tabela Contato
        sql = """
                CREATE TABLE IF NOT EXISTS contatos(
                    CODCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
                    TELEFONE STRING NOT NULL,
                    EMAIL STRING NOT NULL
                )

        """
        cursor.execute(sql)

        # Fechando conexão com o banco
        conexao.close()
    



# Criando as tabelas

# Usa o try catch pra poder executar a função. Caso já exista o banco, ele não cria 
try:  
    criarTabelas()
    
# Verificando se o banco existe. Existindo, pula a execução e não retorna erro
except sqlite.OperationalError:
    pass


