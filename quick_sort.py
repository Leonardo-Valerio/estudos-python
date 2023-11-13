
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

lista = [70, 20, 4, 29, 39, 98, 59, 80, 17, 52]

print(quick_sort(lista))
