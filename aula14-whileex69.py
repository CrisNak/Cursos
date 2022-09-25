somadezoito = somahomens = somamulheresidade = 0
continuar = 's'
while continuar == 's':
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [m/f] :"))
    continuar = str(input("Quer continuar [s/n]? "))
    if idade > 18:
        somadezoito +=1
    if sexo == 'm':
        somahomens +=1
    if sexo == 'f' and idade > 20:
        somamulheresidade += 1
    if continuar == 'n':
        print("O número de maiores de 18 anos é: ", somadezoito)
        print("O número de homens é: ", somahomens)
        print("O número de mulheres maiores de 20 anos é: ", somamulheresidade)
        break

    

