import sqlite3
# Conexão com SGDB
conn = sqlite3.connect("dbProjeto.db")#sempre lembrar de escolher o banco correto

# Obter dados  
print("==============================")
print("#       Cadastramento        #")
print("="*30)

vcpf = input("digite apenas os numeros do CPF: ")
vnome = input("digite seu NOME: ")
vgenero = input("Qual seu genero: ")
vsexo = input("Qual seu sexo biologico: ")
vorientacao = input("qual a sua orientação sexual: ")
vusuario = input("qual nome de Usuario: ")
vsenha = input("Password: ")
vconfirma = input("deseja confirmar os dados:(S ou N) ")
if vconfirma.upper() == "S":
    # enviar instrução sql para ser executada pelo banco
    conn.execute("insert into cadastro values(?,?,?,?,?,?,?)", (vcpf,vnome,vgenero,vsexo,vorientacao,vusuario,vsenha))
    conn.commit()
    print("cadastro feito com sucesso!")   
## fechar conexão 
conn.close
quit()












