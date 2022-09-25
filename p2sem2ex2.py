def menor_nome(nomes):
        nomes1 = []
        for i in nomes:
                cadanome = i.strip()
                nomes1.append(cadanome)
        for c in nomes1:
                nomemenor = c
                if (len(c)) < (len(nomemenor)):
                        nomemenor = nomemenor
                else:
                        nomemenor = c
        return nomemenor.capitalize()
