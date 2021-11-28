# No exercício 7, adicionar quebra no nome para obter apenas o sobrenome, 
# para o usuário irá pedir os dois juntos

i = 0 

while(True):
    nome_sobrenome = input("Digite seu nome e sobrenome: ")
    nome_sobrenome.split()
    nome = nome_sobrenome.split()

    if len(nome[0]) > 3:
        print("Seu nome é: ",nome[0])
        print("Seu sobrenome é: ",nome[1])
        break
    else:
        print("Nome precisa ter mais de 3 letras. Digite novamente: ")
    i += 1
   
    