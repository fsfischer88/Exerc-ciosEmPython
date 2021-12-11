# 11 - Faça um Programa que leia um vetor de 10 caracteres, 
# e diga quantas consoantes foram lidas. Imprima as consoantes.

vogais = ["a","e","i,","o","u"]
consoantes = []
i = 10

    
for x in consoantes:
    letras = input("Digite uma letra: ")
    if letras != vogais:
        consoantes.append(letras)
    else:
        print("Você não digitou nenhuma consoante")
    i -= 1
print(consoantes)