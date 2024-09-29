import sqlite3 as sqlite
import os
def insertMercadoria(codMerc, descricao, preco, qtdestoque):
    cursor.execute('INSERT INTO mercadoria (CODMERC, DESCMERC, PRECOMERC, QTDESTOQUE) VALUES (?, ?, ?, ?)', (codMerc, descricao, preco, qtdestoque))
    conn.commit()

def capturarDadosUsuario():
    os.system("cls")
    codMerc = input("Insira o código da mercadoria: ")
    # Verificando se o CODMERC é único na tabela
    sql = """
        SELECT CODMERC FROM MERCADORIA WHERE CODMERC = ?
    """
    cursor.execute(sql, (codMerc, ))
    resultadoConsulta = cursor.fetchone()
    # Entrará no laço e sairá somente quando o codMerc foi válido
    while resultadoConsulta != None:
        
        print(f"Já existe no banco de dados um produto com o código {codMerc}")
        codMerc = input("Insira o código da mercadoria: ")
        sql = """
            SELECT CODMERC FROM MERCADORIA WHERE CODMERC = ?
        """
        cursor.execute(sql, (codMerc, ))
        resultadoConsulta = cursor.fetchone()
        if resultadoConsulta == None:
            break
    
            
    descricao = input("Insira a descrição do produto: ")
    preco = round(float(input("Insira o valor do produto: ")), 2)
    qtdestoque = int(input("Insira a quantidade em estoque: "))

    return codMerc, descricao, preco, qtdestoque

conn = sqlite.connect('loja.db')
cursor = conn.cursor()

try:
    verificaContinuacaoPrograma = True
    while(verificaContinuacaoPrograma):
        codMerc, descricao, preco, qtdestoque = capturarDadosUsuario()
        insertMercadoria(codMerc, descricao, preco, qtdestoque)
        resposta = input("Deseja inserir mais mercadorias? [S/N] (caso algo diferente de 'S' seja colocado, ele considerara automaticamente como N)")

        if resposta != 'S' and resposta != 's':
            verificaContinuacaoPrograma = False
    conn.close()
    cursor = conn.close()
except sqlite.OperationalError:
    conn.close()
    cursor = conn.close()
    pass