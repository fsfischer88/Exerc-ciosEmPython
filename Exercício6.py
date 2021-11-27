# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.


nome = input("Digite seu usuário: ")


while(True):
    senha = input("Digite sua senha: ")
    if nome != senha:
        print("Cadastrado com sucesso!")
        break
    else:
        print("Sua senha não pode ser igual ao seu nome, digite uma nova senha: ")
  
    