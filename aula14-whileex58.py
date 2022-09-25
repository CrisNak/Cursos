print("Acerte qual o número entre 0 a 10")
n = int(input("Tente acertar o número: "))
while n >10 or n <1:
    print("Este número não é válido")
    n = int(input("Tente acertar o número: "))
m = 0
while n != 8:
    print("Número errado")
    n = int(input("Tente acertar o número: "))
    m += 1
if n == 8:
    print("Você acertou!")
    print("Foram ", m, " tentativas antes de acertar.")
