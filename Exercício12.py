# 12 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

vetor = []
numeros_pares = []
numeros_impares = []



for numeros in range(0,20):
    vetor.append(int(input("Digite um número: ")))

    if vetor[numeros] % 2 == 0:
        numeros_pares.append(vetor[numeros])
        
    elif vetor[numeros] % 2 != 0:
        numeros_impares.append(vetor[numeros])
      
print("Vetor com 20 números: ", str(vetor))
print("Vetor com numeros pares: ", str(numeros_pares))
print("Vetor com numeros impares: ", str(numeros_impares))






