def MinMax(temperaturas):
    print("A menor temperatura do mês foi: ", minima(temperaturas), "C")
    print("A maior temperatura do mês foi: ", maxima(temperaturas), "C")

def maxima(temps):
    min = temps[0]
    i = 1
    while 1 < len(temps):
        if tems[i] > max:
            min = temps[i]
        i += 1
    return max

def minima(temps):
    min = temps[0]
    i = 1
    while 1 < len(temps):
        if tems[i] < min:
            min = temps[i]
        i += 1
    return min

def teste_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valorcalculado != 0:
        print("Valor errado para array ", temp)
        print("Valor esperado: ",valor_esperado, " . VAlor calculado: ", valor_calculado)
    

def testa_minima():
    print("Iniciando os testes")
    teste_pontual([0], 0)
    teste_pontual([0, 0, 0, 0, 0, 0], 0)
    teste_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    teste_pontual([-15, -12, 0, 20, 30], -15)     
    print("Finalizando os testes")
