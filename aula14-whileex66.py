n = s = m = 0 
while True:
    m +=1
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s+= n
print("A soma vale ", s)
print("Foram digitados ", m- 1, " números")
