def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_colunas):
        linha=[]
        for j in range(num_linhas):
            matriz[j][i] = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))
        

    return matriz
