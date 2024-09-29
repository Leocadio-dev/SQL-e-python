import sqlite3 as sqlite

def insertContato(telefone,email, codfornec):
    cursor.execute('INSERT INTO contatos (TELEFONE,EMAIL,CODFORNEC) VALUES (?, ? , ?)', (telefone,email, codfornec))
    conn.commit()  

def capturarDadosUsuario():
    telefone = input("Insira seu telefone : ")
    email = input("Insira seu email: ")
    codfornec = int(input("Insira o codigo do fornecedor: "))
    cursor.execute('SELECT CODFORNEC from fornecedor where CODFORNEC = ?',  str(codfornec))
    dados = cursor.fetchall()
    if len(dados) == 0:
        while(len(dados) == 0):
            cursor.execute('SELECT CODFORNEC from fornecedor')
            print("Todos os fornedores no banco de dados: \n", cursor.fetchall())
            codfornec = int(input("Fornecedor não existe no banco! \n Insira o codigo do fornecedor: "))
            cursor.execute('SELECT CODFORNEC from fornecedor where CODFORNEC = ?', str(codfornec))
            dados = cursor.fetchall()
    return telefone,email,codfornec

conn = sqlite.connect('loja.db')
cursor = conn.cursor()
try:
    verificaContinuacaoPrograma = True
    while(verificaContinuacaoPrograma):
        telefone, email, codfornec = capturarDadosUsuario()
        insertContato(telefone,email,codfornec)
        resposta = input("Deseja continuar inserindo dados? [S/N] (caso algo diferente de 'S' seja colocado, ele automaticamente considerara como N)")
        if resposta != 'S':
            verificaContinuacaoPrograma = False
    conn.close()
    cursor = conn.close()
except sqlite.OperationalError:
    conn.close()
    cursor = conn.close()
    pass