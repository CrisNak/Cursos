saque = int(input("Qual o valor a ser sacado? "))
while saque != 0:
    notacinquenta = saque // 50


50, 20, 10 e 1



somaproduto = somamil = 0
continuar = 's'
while continuar == 's':
    produto = str(input("Qual o nome do produto? "))
    preço = int(input("Qual o preço do produto? "))
    continuar = str(input("Quer continuar [s/n]? "))
    somaproduto = somaproduto + preço
    maisbarato = preço
    if preço > 1000:
        somamil += 1
    if preço <= maisbarato:
        maisbarato = preço
    else:
        maisbarato = maisbarato
    if continuar == 'n':
        print("Total de gasto na compra: ", somaproduto)
        print("O número de produtos que custam mais de R$1000,00 é: ", somamil)
        print("O produto mais barato é: ", maisbarato)
        break


