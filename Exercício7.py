# Faça um programa que leia e valide as seguintes informações:
#   Nome: maior que 3 caracteres;
#   Idade: entre 0 e 150;
#   Salário: maior que zero;
#   Sexo: 'f' ou 'm';
#   Estado Civil: 's', 'c', 'v', 'd';


while(True):
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        print("Nome ok")
        break
    else:
        print("Nome precisa ter mais de 3 letras. Digite novamente: ")

while(True):
    idade = int(input("Digite sua idade: ")) 
    if idade > 0 and idade < 150:
        print("Idade ok")
        break
    else:
        print("Sua idade precisa ser maior que 0 e menor que 150 anos. Digite novamente: ")

while(True):
    salario = float(input("Digite seu salário: "))
    if salario > 0:
        print("Salário ok")
        break
    else:
        print("Seu salário precisa ser maior que 0. Digite novamente: ")

while(True):
    sexo = str(input("Digite seu sexo, F para Feminino e M para masculino: "))
    if sexo == "F":
        print("Seu sexo é Feminino")
        break
    elif sexo == "M":
        print("Seu sexo é Masculino")
        break
    else:
        print("Você não digitou um sexo válido. Digite novamente: ")

while(True):
    estado_civil = str(input("Digite seu estado civíl:"))
    if estado_civil == "Solteiro":
        print("Você é solteiro!")
        break
    elif estado_civil == "Casado":
        print("Você é Casado!")
        break
    elif estado_civil == "Divorciado":
        print("Você é Divorciado!")
        break
    elif estado_civil == "Viúvo":
        print("Você é Viúvo!")
        break
    else:
        print("Você não digitou um estado civíl válido. Digite novamente: ")

   
print("Seu nome é ",nome,",você é do sexo",sexo,",seu estado civíl é",estado_civil,",você tem ", idade," anos de idade,", "e o seu salário é", salario)




