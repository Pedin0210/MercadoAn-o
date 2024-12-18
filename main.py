from classPerson import Person
from classPerson import User


from login import cpf_validation
from login import email_validation

from login import password_validation
from login import users

#importa funções

while True:
        
    print("|=============== Login ===============|")
    print("|    Digite 1 para se Cadastrar       |")
    print("|    Digite 2 para logar como cliente |")
    print("|    Digite 3 para Sair               |")
    
#printa as opçoes
    try:
        option = int(input("|Digite a ação om base na tabela acima:"))
    except ValueError:
        print("|Digite um numero valido!")

        continue
#define a variavel option apartir de um input


    if option == 1:
        name = input("|Digite seu nome:")
        
        cpf = input("|Digite seu cpf:")
        if not cpf_validation(cpf):
            print("|Erro, cpf invalido")
            continue

        age = input("|Digite sua idade:")
        email = input("|Digite seu email para cadastrar:")
        if not email_validation(email):
            print("|Email invalido")
            break


        password = input("|Digite a senha para este conta:")

        for c in users:
            if c.getid() == id:
                print("|id já cadastrado")
                break
            if c.getEmail() == email:
                print("|Email ja cadastrado")
                break
        
        newUser = User(name, id, age, email, password)
        users.append(newUser)
    #cadastro com validaçao de email e senha

    
    elif option == 2:
        email = input("|Digite seu email:")
        password = input("|Digite sua senha:")

        if users:
            user_found = None
            for c in users:
                if c.getEmail() == email and c.getPassword() == password:
                    user_found = c
                    break
            if user_found:
                print(f"|{user_found.getName()}, seja bem vindo")
            else:
                print("|Email ou senha incorretos")
        else:
            print("|Nenhum cliente cadastrado")
    #login como usuario tendo verificaçao de email e senha


    elif option == 3:
        print("|Sessão encerrada!")
        break
    #encerra progama
    

 
