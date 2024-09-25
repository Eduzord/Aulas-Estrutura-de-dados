class NodoLista:
    """Esta classe representa um nodo de uma lista encadeada."""
    def __init__(self,dado=0,proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado,self.proximo)

class ListaEncadeada:
    "Representa a lista"
    def __init__(self):
        self.cabeca = None

    def insere_inicio(self,novo_dado):
        novo_nodo = NodoLista(novo_dado)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo
    def insere_final(self,novo_dado,nodo_anterior):
        pass

    def busca(self,valor):
        chain = self.cabeca
        while chain and chain.dado != valor:
            chain = chain.proximo
        return chain.dado

    def remove(self,valor):
        chain = self.cabeca
        anterior = None


        if chain.dado == valor:
            self.cabeca = chain.proximo
        else:

            while chain and chain.dado != valor:
                #armazena o valor anterior da lista para ser usado
                anterior = chain
                chain = chain.proximo
            if chain.dado == valor:
                #faz com que o próximo do elemento anterior ao removido "pule"
                # para o elemento após o removido
                anterior.proximo = chain.proximo
                chain = None

    def remove_duplicatas(self):
        chain = self.cabeca
        anterior = None
        while chain:
            # armazena o valor anterior da lista para ser usado
            anterior = chain
            chain = chain.proximo
            while chain and chain.dado == anterior.dado:
                # faz com que o próximo do elemento anterior ao removido "pule"
                # para o elemento após o removido
                anterior.proximo = chain.proximo
                chain = chain.proximo



    def mostra_cabeca(self):
        return self.cabeca.dado


    def __repr__(self):
        return "[" + str(self.cabeca) +"]"

def insere_no_inicio(lista, novo_dado):
    # 1) Cria um novo nodo com o dado a ser armazenado.
    novo_nodo = NodoLista(novo_dado)

    # 2) Faz com que o novo nodo seja a cabeça da lista
    novo_nodo.proximo = lista.cabeca

    # 3) Faz com que a cabeça da lista referencie o novo nodo.
    lista.cabeca = novo_nodo
def busca(lista,valor):
    corrente = lista.cabeca
    while corrente and corrente.dado != valor:
        corrente = corrente.proximo
    return corrente.dado

def remove(lista,valor):
    chain = lista.cabeca
    anterior = None

    if chain.dado == valor:
        chain.cabeca = chain.proximo
        chain = None

        while chain and chain.dado != valor:
            #armazena o valor anterior da lista para ser usado
            anterior = chain
            chain = chain.proximo
        if chain.dado == valor:
            #faz com que o próximo do elemento anterior ao removido "pule"
            # para o elemento após o removido
            anterior.proximo = chain.proximo
            chain = None

def remove_duplicatas(lista):
    chain = lista.cabeca
    anterior = None
    while chain:
        #armazena o valor anterior da lista para ser usado
        anterior = chain
        chain = chain.proximo

        while chain and chain.dado == anterior.dado:
            #faz com que o próximo do elemento anterior ao removido "pule"
            # para o elemento após o removido
            anterior.proximo = chain.proximo
            chain = chain.proximo



lista = ListaEncadeada()
print("Lista vazia:", lista)

# insere_no_inicio(lista,5)
# print("Lista contém um único elemento:",lista)
# insere_no_inicio(lista, 10)
# print("Inserindo um novo elemento:", lista)
# insere_no_inicio(lista, 15)
# print("Inserindo um novo elemento:", lista)

lista.insere_inicio(10)
print(lista)
lista.insere_inicio(10)
print(lista)
lista.insere_inicio(7)
print(lista)
lista.insere_inicio(5)
print(lista)
lista.insere_inicio(1)
print(lista)
lista.insere_inicio(1)
print(lista)
lista.insere_inicio(1)
print(lista)
lista.insere_inicio(1)
print(lista)
lista.insere_inicio(0)
print(lista)
print(lista.busca(10))
# print(busca(lista,55))
# lista.remove(55)
# remove(lista,5)
print(lista)
# remove_duplicatas(lista)
lista.remove_duplicatas()
print(lista)
