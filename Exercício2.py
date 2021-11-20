# 2 - Faça um Programa que peça um valor e mostre na tela se o valor
# é positivo ou negativo.


valor = int(input("Digite um número: "))

if valor > 0:
    print("Este número é positivo:", valor)
elif valor == 0:
    print("Este número é Zero:", valor)
else:
    print("Este número é negativo:", valor)

