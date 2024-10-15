import sqlite3 as sqlite

def insertContato(telefone,email):
    cursor.execute('INSERT INTO contatos (TELEFONE,EMAIL) VALUES (? , ?)', (telefone,email))
    conn.commit()  

def capturarDadosUsuario():
    telefone = input("Insira seu telefone : ")
    email = input("Insira seu email: ")
    return telefone,email

conn = sqlite.connect('loja.db')
cursor = conn.cursor()
try:
    verificaContinuacaoPrograma = True
    while(verificaContinuacaoPrograma):
        telefone, email = capturarDadosUsuario()
        insertContato(telefone,email)
        resposta = input("Deseja continuar inserindo dados? [S/N] (caso algo diferente de 'S' seja colocado, ele automaticamente considerara como N)")
        if resposta != 'S' and resposta != 's':
            verificaContinuacaoPrograma = False
    conn.close()
    cursor = conn.close()
except sqlite.OperationalError:
    conn.close()
    cursor = conn.close()
    pass