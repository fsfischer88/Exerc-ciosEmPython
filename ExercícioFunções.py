#1.	Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma_valores(valor1,valor2,valor3):
    total = int(valor1) +int(valor2) +int(valor3)
    return total

print(soma_valores(10,10,10))



#2.	Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, 
# se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

valor = int(input("Digite um valor: "))

def numero(valor):
   
    if valor >= 0:
        print("P - O Valor é positivo!")
    elif valor <= 0:
        print("N - O Valor é negativo!")
    else:
        print("Você digitou um valor inválido")
    
numero(valor)


 

#3.	Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
# A função “altera” o valor de custo para incluir o imposto sobre vendas.


taxaImposto = float(input("Digitie o valor do imposto: "))
custo_prod = float(input("Digite o custo do Produto: "))


def somaImposto():
    preco_final = taxaImposto*(custo_prod) + custo_prod
    print("O preço final do produto é: ",preco_final)

somaImposto()





