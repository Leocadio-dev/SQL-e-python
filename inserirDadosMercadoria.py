import sqlite3 as sqlite

def insertMercadoria(descricao, preco, qtdestoque):
    cursor.execute('INSERT INTO mercadoria (DESCMERC, PRECOMERC, QTDESTOQUE) VALUES (?, ?, ?)', (descricao, preco, qtdestoque))
    conn.commit()

def capturarDadosUsuario():
    descricao = input("Insira a descrição do produto: ")
    preco = round(float(input("Insira o valor do produto: ")), 2)
    qtdestoque = int(input("Insira a quantidade em estoque: "))

    return descricao, preco, qtdestoque

conn = sqlite.connect('loja.db')
cursor = conn.cursor()

try:
    verificaContinuacaoPrograma = True
    while(verificaContinuacaoPrograma):
        descricao, preco, qtdestoque = capturarDadosUsuario()
        insertMercadoria(descricao, preco, qtdestoque)
        resposta = input("Deseja inserir mais mercadorias? [S/N] (caso algo diferente de 'S' seja colocado, ele considerara automaticamente como N)")

        if resposta != 'S' and resposta != 's':
            verificaContinuacaoPrograma = False
    conn.close()
    cursor = conn.close()
except sqlite.OperationalError:
    conn.close()
    cursor = conn.close()
    pass