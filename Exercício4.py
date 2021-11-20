# 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogal = {"a","i","o","u"}
letra = str(input("Digite uma letra: "))


for x in vogal:
    if letra not in vogal:
        print("Essa letra é uma consoante")
        break
    else:
        print("Esta letra é uma vogal")
        break
