
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    maiores = []
    menores = []
    iguais = []
    for i in range(len(lista)):
       if pivo > lista[i]:
           menores.append(lista[i])
       elif pivo < lista[i]:
           maiores.append(lista[i])
       elif pivo == lista[i]:
           iguais.append(lista[i])
    return quick_sort(menores) + iguais + quick_sort(maiores)

lista = [7,7,2,8,4,2,5,1,3]

print(quick_sort(lista))
