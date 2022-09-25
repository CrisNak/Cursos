s = str(input("Digite o seu sexo [M/F]: ")).upper()

if s=="M":
    print("Masculino")
elif s == 'F' :
    print("Feminino")
else:
    while s != 'M' or s !='F':
        print("Esta opção não é aceita!")
        s = str(input("Digite o seu sexo [S/N]: ")).upper()
