# Bibliotecas importadas
import os
from datetime import datetime, date

import sqlite3 as sqlite

# Criando conexão com o banco (se não existente, cria o banco)
conexao = sqlite.connect("loja.db")

# Criando a conexão para execução de queries
cursor = conexao.cursor()



def inserirDadosPedido():
    # Limpando o console pra melhor visualização
    os.system("cls")
    
    quantidadeRegistros = int(input("Quantos pedidos serão registrados?"))
    
    for i in range(quantidadeRegistros):

        # Criando variáveis de input
        numNotaFiscal = int(input("Digite o número da nota fiscal\n"))
        valorTotal = round(float(input("Digite o valor total do produto\n")), 2)

        # Primeira forma de adicionar a data do pedido (pegando automaticamente)
        dataPedido = date.today().strftime("%d/%m/%Y")
        
        # Usar pra fazer query verificando se o cliente existe
        cpfCliente = input("Qual o CPF do cliente que efetuou a compra (sem traços e pontos)\n")
        
        # Verificando se o id existe
        sql = """
            SELECT IDCLIENTE FROM CLIENTE WHERE CPF = ?;
        """
        # Fazendo a query no banco
        cursor.execute(sql, (cpfCliente, ))
        
        # Armazenando o resultado da primeira linha da query
        resultadoConsulta = cursor.fetchone()

        # Caso não tenha nada, o fetchone retorna None por padrão
        if resultadoConsulta == None:
            print(f"Não foi possível encontrar um cliente com o cpf {cpfCliente} no banco de dados.")
        else:
            # Armazena o id contido na query
            # A query fetchone retorna uma tupla somente, já o fetchall retorna uma lista com tuplas
            idCliente = resultadoConsulta[0]
            
            # Buscando o código da mercadoria
            codMerc = int(input("Digite o código da mercadoria "))
            
            # Verificando se o codigo de mercadoria existe
            sql = """
                SELECT CODMERC FROM MERCADORIA WHERE CODMERC = ?;
            """
            # Fazendo a query no banco
            cursor.execute(sql, (codMerc, ))
            resultadoConsulta = cursor.fetchone()
            if resultadoConsulta == None:
                print(f"Não foi possível encontrar uma mercadoria com o código {codMerc} no banco de dados.")
                
                
            else:
                # Se os códigos existirem, o programa executará a query de inserção
                try:
                    sql = """
                        INSERT INTO PEDIDO(NUMNOTAFISCAL, VALORTOTAL, DATAPEDIDO, IDCLIENTE, CODMERC) VALUES(
                            ?,?,?,?,?
                        )
                    """
                    cursor.execute(sql, (numNotaFiscal, valorTotal, dataPedido, idCliente, codMerc, ))
                    
                    # Insere as informações no banco
                    conexao.commit()
                except Exception as e:
                    print(f"Erro: {e}")
                
                            
        
        # Fechando o banco
    conexao.close()


inserirDadosPedido()

    # Segunda forma de adicionar a data do pedido (usuário inputando)
    # # Usando desta forma, pedir para o usuário digitar o dia, mês e ano no formato dd/mm/yyyy e fazer verificação se ele digitou assim usando o strftime talvez
    