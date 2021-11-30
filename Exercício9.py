# 9 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

import random
from typing import List

numeros = []

for lista in range(0,10):
    numero_aleatorio = random.randrange(0,100)
    numeros.append(numero_aleatorio)

print(numeros)

numeros.reverse()

print(numeros)

