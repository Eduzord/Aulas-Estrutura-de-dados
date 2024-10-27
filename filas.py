class nodoFila:
    def __init__(self, valor = 0, proximo_nodo = None):
        self.dado = valor
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado,self.proximo)


class Fila:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def inserir(self,valor):
        novo_nodo = nodoFila(valor)

        if self.cabeca == None:

            self.cabeca = novo_nodo
            self.cauda = novo_nodo

        else:

            self.cauda.proximo = novo_nodo
            self.cauda = novo_nodo

    def atender(self):
        self.cabeca = self.cabeca.proximo

    def atender_prioridade(self,valor):
        corrente = self.cabeca
        anterior = None
        if corrente.dado == valor:
            self.cabeca = corrente.proximo
        else:
            while corrente and corrente.dado != valor:
                anterior = corrente
                corrente = corrente.proximo
            if corrente.dado == valor:
                anterior.proximo = corrente.proximo




    def __repr__(self):
        return "[" + str(self.cabeca) +"]"

no = nodoFila()
print(no)
fila = Fila()
print(Fila)
fila.inserir(5)
print(fila)
fila.inserir(15)
print(fila)
fila.inserir(75)
print(fila)
fila.inserir(55)
print(fila)
# fila.remover()
# print(fila)
# fila.remover()
# print(fila)
fila.atender_prioridade(75)
print(fila)
fila.atender()
print()
fila.atender()

