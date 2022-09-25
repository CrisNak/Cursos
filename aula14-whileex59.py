n = int(input("Escreva um valor "))
m = int(input("Escreva outro valor "))
print("[1]somar \n [2]multiplicar \n [3]maior \n [4]novos números \n [5] sair do programa")
menu = int(input("Qual sua escolha: "))
while menu < 1 or menu >5:
    print("Opção inexistente")
    menu = int(input("Qual sua escolha: "))
while menu == 4:
    n = int(input("Escreva um valor "))
    m = int(input("Escreva outro valor "))
    print("[1]somar \n [2]multiplicar \n [3]maior \n [4]novos números \n [5] sair do programa")
    menu = int(input("Qual sua escolha: "))
    while menu < 1 or menu >5:
        print("Opção inexistente")
        print("[1]somar \n [2]multiplicar \n [3]maior \n [4]novos números \n [5] sair do programa")
        menu = int(input("Qual sua escolha: "))
if menu == 1:
    resultado = m + n
    print("Resultado: ", resultado)
elif menu == 2:
    resultado = m * n
    print("Resultado: ", resultado)
elif menu == 3:
    if m > n:
       print(m, " é maior")
    else:
       print(n, " é maior")
elif menu == 5:
    print("fim do programa")
        
        

    
