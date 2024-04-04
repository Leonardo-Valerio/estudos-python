
# Organiza palavras em uma lista comum utilizando a key lambda para organizar pela len de cada item na lista

palavras = ['banana','maça' ,'laranja','abacaxi' ,'uva']

ordenada = sorted(palavras, key=lambda palavra:len(palavra) )
print(ordenada)


# Organiza números em uma lista comum de tuplas utilizando a key lambda para organizar pelo primeiro item de cada tupla

lista_tuplas = [(3,2),(2,8), (4,3)]
ordena = sorted(lista_tuplas, key=lambda tupla: tupla[0])
print(ordena)


# Organiza uma lista de dicionários utilizando a key lambda para organizar o json pela idade da pessoa
pessoas = [
    {'nome':'ana','idade':30},
    {'nome':'joão','idade':25},
    {'nome':'francisco','idade':35}
]

ordena_pessoas = sorted(pessoas,key=lambda pessoa:pessoa['idade'])
print(ordena_pessoas)

# Organiza duas listas pelo mesmo parametro e para isso, faço uma junção dela usando o zip e também com ele,
# separo as listas ordenadas em cada variavel, o intuito no exemplo é ordenar tanto a coluna nomes e idades pelo nome

nomes = ['ana','joão','francisco']
idades = [30,25,35]

nomes_ord, idades_ord = zip(*sorted(zip(nomes,idades), key=lambda x:x[0]))
print(f'nomes ordenados pela idade: {nomes_ord}')
print(f'idades ordenadas por idade: {idades_ord}')

# Organiza três listas pelo mesmo parametro e para isso, faço uma junção dela usando o zip e também com ele,
# separo as listas ordenadas em cada variavel, o intuito do exemplo é ordenar as duas listas pelo valor de estoque,
# assim tenho que acessar duas colunas diferentes para multiplicar seus respectivos valores

produtos = ['camiseta','calça', 'tênis']
estoque = [100,50,30]
preco = [20,40,100]

produtos_ord, estoque_ord, preco_ord = zip(*sorted(zip(produtos,estoque,preco), key=lambda produto:produto[1]*produto[2],reverse=True ))

print(produtos_ord)

json_produtod_ordenados = [
    {'produtos':produtos_ord},
    {'estoque':estoque_ord},
    {'preco':preco_ord}
]
print(json_produtod_ordenados)