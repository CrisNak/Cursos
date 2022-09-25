def imprime_matriz(minha_matriz):
    for i in range(len(minha_matriz)):
        for j in range(len(minha_matriz[i])):
            if j == len(minha_matriz) - 1:
                print(minha_matriz[i][j], end=" ")
            else:
                print(minha_matriz[i][j], end=" ")
        print() 
                
       
        


