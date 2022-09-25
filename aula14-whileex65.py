n = int(input("Escreva o número inteiro :"))
x = str(input("Você quer continuar a digitar valores? [S/N]"))
m = 1
soma = 0
while x == 'S':
    m += 1
    soma = soma + n
    x = str(input("Você quer continuar a digitar valores? [S/N]"))
    n = int(input("Escreva o número inteiro "))
if x == 'N':
    print(soma /m)
    print("Maior valor lido: ",)
    print("Menor valor lido: ",)
        

    
