# Bibliotecas importadas
import os

import sqlite3 as sqlite

# Criando conexão com o banco (se não existente, cria o banco)
conexao = sqlite.connect("loja.db")

# Criando a conexão para execução de queries
cursor = conexao.cursor()
def inserirDadosFornecedor():

    # Limpar o console
    os.system("cls")
    
    quantidadeRegistros = int(input("Quantos fornecedores serão registrados? "))
    
    for i in range(quantidadeRegistros):
        codFornecedor = int(input("Insira o código do fornecedor: "))
        
        # Verificando se já há um pedido com a nota fiscal digitada
        sql = """
            SELECT CODFORNEC FROM FORNECEDOR WHERE CODFORNEC = ?
        """
        cursor.execute(sql, (codFornecedor, ))
        
        resultadoConsulta = cursor.fetchone()
        
        while resultadoConsulta != None:
            print(f"Já existe fornecedor com o código {codFornecedor} no banco de dados")
            
            codFornecedor = int(input("Insira o código do fornecedor: "))
            sql = """
                SELECT CODFORNEC FROM FORNECEDOR WHERE CODFORNEC = ?
            """
            cursor.execute(sql, (codFornecedor, ))
            resultadoConsulta = cursor.fetchone()
        
            if resultadoConsulta == None:
                break
        
        razaoSocial = input("Insira a razão social: ")
        nomeFantasia = input("Insira o nome fantasia: ")
        cnpj = int(input("Insira o CNPJ (sem pontos, barra e hífen): "))
        endereco = input("Insira o endereço: ")
        telefoneCentral = input("Insira o telefone: ")
        codContato = input("Insira o código do contato: ")
        sql = """
            SELECT CODCONTATO FROM FORNECEDOR WHERE CODCONTATO = ?
        """
        cursor.execute(sql, (codContato, ))
        
        resultadoConsulta = cursor.fetchone()
        
        while resultadoConsulta == None:
            print(f"Não existe contato com o código {codContato} no banco de dados")
            
            codContato = int(input("Insira o código do contato: "))


            sql = """
                SELECT CODCONTATO FROM CONTATOS WHERE CODCONTATO = ?
            """
            cursor.execute(sql, (codContato, ))
            resultadoConsulta = cursor.fetchone()
        
            if resultadoConsulta != None:
                break
        
        # Execuando o SQL
        try:
            sql = """
                INSERT INTO fornecedor(CODFORNEC, RAZSOC, NOMEFANTASIA, CNPJ, ENDERECO, TELCENTRAL, CODCONTATO) VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(sql, (codFornecedor, razaoSocial, nomeFantasia, cnpj, endereco, telefoneCentral, codContato, ))
            conexao.commit()
            os.system("cls")
        except Exception as e:
            print(f"Erro {e}")
            
    conexao.close()
inserirDadosFornecedor()