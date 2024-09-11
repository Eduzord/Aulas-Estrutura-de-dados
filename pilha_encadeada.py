from random import randint
class nodoPilha:
    """Esta classe representa um nodo de uma estrutura encadeada"""
    def __init__(self, dado = 0, nodo_anterior = None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return "%s -> %s" %(self.dado,self.anterior)

class Pilha:

    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def inserir_nodo(self, novo_dado):
        # Cria um novo nodo com o dado a ser armazenado.

        novo_nodo = nodoPilha(novo_dado)

        # Faz com que o novo nodo seja o topo da pilha.

        novo_nodo.anterior = self.topo

        # Faz com que a cabeça da lista referencie o novo nodo.
        self.topo = novo_nodo

    def remover_nodo(self):
        assert self.topo, "Impossível remover valor de pilha vazia."

        self.topo = self.topo.anterior

    def insere_n(self,qtd_elementos=0):
        if qtd_elementos <= 0:
            pass
        for i in range(qtd_elementos):
            self.inserir_nodo(randint(0,10))


P = Pilha()
P.inserir_nodo(555)
print(P)
P.inserir_nodo(5)
print(P)
P.inserir_nodo(15)
print(P)
P.inserir_nodo(75)
print(P)
P.inserir_nodo(66)
print(P)
P.inserir_nodo(24)
print(P)
# P.remover_nodo()
# print(P)
# P.remover_nodo()
# print(P)

#def mover_pilha(pilha_origem, pilha_saida)

"""Exercício 1: Escrever uma função que receba como parâmetro uma pilha.
A função deve retornar o maior elemento da pilha."""
def maior_pilha(Pilha):
    chain = Pilha.topo
    maior_valor = 0
    while chain and chain.dado != None:
        if chain.dado != None:
            if chain.dado > maior_valor:
                maior_valor = chain.dado
        else:
            pass
        chain = chain.anterior

    print(maior_valor)

maior_pilha(P)

#####
"""Exercício 2: Utilizando uma pilha resolver o exercício a seguir:
Dada uma sequência contendo N (N >0) números reais, imprimi-
la na ordem inversa."""
def inverter_pilha(Pilha):
    chain = Pilha.topo
    lista_valores = [ ]
    while chain and chain.dado != None:
        lista_valores.append(chain.dado)
        chain = chain.anterior
    lista_valores.reverse()
    print(lista_valores)

inverter_pilha(P)

#####

P2 = Pilha()
P2.inserir_nodo(555)
print(P2)
P2.inserir_nodo(5)
print(P2)
P2.inserir_nodo(15)
print(P2)
P2.inserir_nodo(75)
print(P2)
P2.inserir_nodo(66)
print(P2)
P2.inserir_nodo(24)
print(P2)


"""Exercício 3: Escreva uma função que receba como parâmetro duas pilhas e
verifique de elas são iguais.
Duas pilhas são iguais se possuem os mesmos elementos, na
mesma ordem."""
def compara_pilha(Pilha_1, Pilha_2):
    assert Pilha_1
    assert Pilha_2

    corrente_1 = Pilha_1.topo
    corrente_2 = Pilha_2.topo
    iguais = True
    while corrente_1 and corrente_1.dado != None:
        if corrente_1.dado != corrente_2.dado:
            iguais = False
            break
        corrente_1 = corrente_1.anterior
        corrente_2 = corrente_2.anterior
    if iguais:
        print("As pilhas são iguais!")
    else:
        print("As pilhas são diferentes!")

compara_pilha(P,P2)