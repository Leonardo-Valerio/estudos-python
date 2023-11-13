from quick_sort import *
def binary_search(lista, item, inicio=0,fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio <= fim:
        meio = (inicio + fim)//2
        chute = lista[meio]
        if chute == item:
            return f'o valor {chute} se encontra no indíce {meio}'
        if chute < item:
            return binary_search(lista,item,meio+1,fim)
        else:
            return binary_search(lista,item, inicio,meio-1)
    else:
        return None

lista = quick_sort([70, 20, 4, 29, 39, 98, 59, 80, 17, 52])

print(binary_search(lista,17))
