def imprime_matriz(minha_matriz):
	cols = len(minha_matriz)
	for i in range(len(minha_matriz)):
		for j in range(len(minha_matriz[i])):
			if j == cols-1:
				print(minha_matriz[i][j], end=" ")
			else:
				print(minha_matriz[i][j], end=" ")
		print("\n", end="")        


