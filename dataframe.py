import pandas as pd

dicionario1 = {'A':[ [1,2], [2,3] ],
               'B':[[2,3], [3, 4] ]}

tabela = pd.DataFrame(dicionario1)

def combinar(row):
    novo_set = set(row['A']) | set(row['B'])
    novo_set = list(novo_set)
    return novo_set


tabela['Combinação'] = tabela.apply(combinar, axis=1)
print(tabela)

# lista_1 = set([1,2,3])
# lista_2 = set([2,3,4])
#
# print(lista_1 | lista_2)