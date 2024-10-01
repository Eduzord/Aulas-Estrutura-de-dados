
### Exercício 1
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

    def __repr__(self):
        return "[" + str(self.cabeca) +"]"

    def push(self,valor):
        novo_nodo = nodoFila(valor)

        if self.cabeca == None:

            self.cabeca = novo_nodo
            self.cauda = novo_nodo

        else:

            self.cauda.proximo = novo_nodo
            self.cauda = novo_nodo

    def pop(self):
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






no = nodoFila()
print(no)
fila = Fila()
print(Fila)
fila.push(5)
print(fila)
fila.push(15)
print(fila)
fila.push(75)
print(fila)
fila.push(55)
print(fila)
# fila.remover()
# print(fila)
# fila.remover()
# print(fila)
fila.atender_prioridade(75)
print(fila)
# fila.pop()
# print(fila)
# fila.pop()
# print(fila)

### Exercício 2


def busca_valor(fila):
    valor = int(input("Qual valor você deseja buscar?"))
    atual = fila.cabeca
    contagem = 1
    while atual and atual.dado != valor:
        contagem +=1
        atual = atual.proximo

    if not atual:
        print("Não encontrei o valor :(")
    else:
        print(f"Encontrei o valor {valor} e sua posição na fila é {contagem}")


# busca_valor(fila)

### Exercício 3

def imprime_elementos(fila):
    elementos = []
    atual = fila.cabeca
    while atual:
        elementos.append(atual.dado)
        atual = atual.proximo
    print(elementos)

imprime_elementos(fila)

### Exercício 4

def inverte_fila(fila):
    elementos = []
    atual = fila.cabeca
    while atual:
        elementos.append(atual.dado)
        atual = atual.proximo
    elementos.reverse()
    print(f"Fila invertida {elementos}")

inverte_fila(fila)




