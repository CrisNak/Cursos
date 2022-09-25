def éPrimo(k):
    fator = 2
    while k % fator!=0 and fator <=k/2:
        fator = fator + 1
    if k% fator == 0:
        return False
    else:
        return True
    
def maior_primo(n):
    while n > 0:
        if éPrimo(n):
            return n
        else:
            n = n -1

        
