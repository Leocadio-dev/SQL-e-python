import sqlite3 as sqlite

# Criando conexão com o banco (se não existente, cria o banco)
conexao = sqlite.connect("loja.db")

# Criando a conexão para execução de queries
cursor = conexao.cursor()

def criarTabelas():

    # Criando tabela pedido
        
        # Tabela Pedido
        sql = """
                CREATE TABLE pedido(
                    IDPEDIDO INTEGER PRIMARY KEY AUTOINCREMENT,
                    NUMNOTAFISCAL STRING NOT NULL,
                    VALORTOTAL NUMERIC NOT NULL,
                    DATAPEDIDO DATE NOT NULL,
                    IDCLIENTE INTEGER NOT NULL,
                    CODMERC INTEGER NOT NULL
                )

        """
        cursor.execute(sql)
     
        # Tabela Mercadoria
        sql = """
                CREATE TABLE mercadoria(
                    CODMERC INTEGER PRIMARY KEY,
                    DESCMERC STRING NOT NULL,
                    PRECOMERC NUMERIC NOT NULL,
                    QTDESTOQUE INTEGER NOT NULL
                )

        """
        cursor.execute(sql)
        
        # Tabela Cliente
        sql = """
                CREATE TABLE cliente(
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
                CREATE TABLE fornecedor(
                    CODFORNEC INTEGER PRIMARY KEY,
                    RAZSOC STRING NOT NULL,
                    NOMEFANTASIA STRING NOT NULL,
                    CNPJ STRING NOT NULL,
                    ENDERECO STRING NOT NULL,
                    TELEFONECENTRAL STRING NOT NULL,
                    CODCONTATO INTEGER NOT NULL
                    
                )

        """
        cursor.execute(sql)
        
        # Tabela Contato
        sql = """
                CREATE TABLE contatos(
                    CODCONTATO INTEGER PRIMARY KEY,
                    TELEFONE STRING NOT NULL,
                    EMAIL STRING NOT NULL,
                    CODFORNEC INTEGER NOT NULL
                )

        """
        cursor.execute(sql)

        sql = """
            FOREIGN KEY (IDCLIENTE) REFERENCES cliente(IDCLIENTE),
            FOREIGN KEY (IDMERC) REFERENCES mercadoria(CODMERC),
            FOREIGN KEY (CODFORNEC) REFERENCES fornecedor(CODFORNEC),
            FOREIGN KEY (CODCONTATO) REFERENCES contatos(CODCONTATO)
        """
        cursor.execute(sql)
        
        # Fechando conexão com o banco
        conexao.close()
    



# Criando as tabelas

# Usa o try catch pra poder executar a função. Caso já exista o banco, ele não cria 
try:  
    bancoCriado = criarTabelas()
    
# Verificando se o banco existe. Existindo, pula a execução e não retorna erro
except sqlite.OperationalError:
    pass


