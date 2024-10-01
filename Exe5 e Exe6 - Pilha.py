import random
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


### Exercício 5

vetor = []
for i in range(15):
    vetor.append(random.randint(1,100))

def TPilha(pilha,vetor):
    for i in vetor:
        if i%2 ==0:
            pilha.inserir_nodo(i)
        elif pilha.topo == None:
            print(f"Pilha vazia, não possivel remover")
        else:
            pilha.remover_nodo()
    print(pilha)
    print("Esvaziando pilha:")
    atual = pilha.topo
    while atual:
        print(f"Removendo {atual.dado}")
        pilha.remover_nodo()
        atual = atual.anterior

pilha1 = Pilha()
print(vetor)
TPilha(pilha1,vetor)

### Exercício 6

vetor_inteiros = []
for i in range(15):
    vetor_inteiros.append(random.randint(-100, 100))

print(vetor_inteiros)

def TPilha2(P,N,vetor):
    for i in vetor:
        if i > 0:
            P.inserir_nodo(i)
        elif i < 0:
            N.inserir_nodo(i)
        else:
            if P.topo == None or N.topo == None:
                print(f"Uma das pilhas está vazia, não é possível remover")
            else:
                P.remover_nodo()
                N.remover_nodo()
    print(f"Imprimindo Pilha de Positivos")
    print(P)
    print(f"Imprimindo Pilha de Negativos")
    print(N)

pilhaPositivos = Pilha()
pilhaNegativos = Pilha()

# vetor_teste = [-6,-4,-2,0,2,4,6]
#
# TPilha2(pilhaPositivos,pilhaNegativos,vetor_teste)
TPilha2(pilhaPositivos,pilhaNegativos,vetor_inteiros)



