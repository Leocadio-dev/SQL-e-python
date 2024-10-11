import sqlite3 as sqlite
import os

conexao = sqlite.connect("loja.db")
cursor = conexao.cursor()

while True:
    os.system("cls")
    cpf = input("Digite o seu CPF (sem pontos e traços): ")
    while len(cpf) > 11 | len(cpf) < 11:
        
        print("CPF inválido")
        cpf = input("Digite o seu CPF (sem pontos e traços): ")
        
        if len(cpf) == 11:
            break
    
    # Verificando se o CPF já existe no banco
    sql = """
        SELECT COUNT(*) FROM cliente WHERE cpf = ?
    """
    cursor.execute(sql, (cpf,))
    resultado = cursor.fetchone()

    if resultado[0] == 0:
        break  # Sai do loop se o CPF não existir
    
    # Limpando tela
    os.system("cls")
    
    print("CPF já cadastrado. Por favor, digite um CPF diferente.")

rg = input("Digite o seu RG (opcional): ")
endereco = input("Digite o seu endereco: ")
email = input("Digite o seu email: ")
telfixo = input("Digite o seu telefone fixo (opcional): ")
celular = input("Digite o seu número de celular: ")

# Query SQL para inserir os dados
sql = """
    INSERT INTO cliente (cpf, rg, endereco, email, telefonefixo, celular) VALUES (?, ?, ?, ?, ?, ?)
"""

# Executa a query com os dados do usuário
cursor.execute(sql, (cpf, rg, endereco, email, telfixo, celular))
conexao.commit()

# Fecha a conexão
conexao.close()
