# 11 - Faça um Programa que leia um vetor de 10 caracteres, 
# e diga quantas consoantes foram lidas. Imprima as consoantes.

vogais = {"a","e","i","o","u"}
consoantes = []
contVogais = 0
x = 1


while x <= 10:   
    letras = input("Digite uma letra: ")
    x += 1
    consoantes.append(letras)
      
    if letras in vogais:
        contVogais += 1 
    print("Consoantes: ", (len(consoantes)) - contVogais)

