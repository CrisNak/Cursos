n = int(input("Digite um número inteiro "))

soma = 0

while n > 0:
    m = n % 10
    soma = soma + m
    n = n // 10
print(soma)


