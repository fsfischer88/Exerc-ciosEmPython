# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e 
# continue pedindo até que o usuário informe um valor válido.

nota = float(input("Digite sua nota: "))

i = 0
while i <3:
    
    if nota >=0 and nota <= 10:
        print("Sua nota é: ", nota)
        break
    else:
        float(input("Digite uma nota válida: "))
    i += 1
  

      
  
        
        


    
   
        
        
       