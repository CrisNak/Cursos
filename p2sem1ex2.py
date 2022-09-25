def soma_matrizes(m1, m2):
    soma_matrizes = []
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        soma_matrizes = []
        for i in range(len(m1)):
            linha =[]
            for j in range(len(m1[0])):
                linha.append(m1[i][j] + m2[i][j])
            soma_matrizes.append(linha)
        return soma_matrizes
    else:
        print(False)
    

