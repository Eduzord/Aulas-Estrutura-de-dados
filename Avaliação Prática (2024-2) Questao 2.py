# Questão 2
# A estrutura ligada mais adequada para resolver esse problema seria a PILHA
# A justificativa é porque o cenário exige a remoção do ultimo elemento inserido.


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None

    def empilhar(self, item):
        novo_nodo = Nodo(item)
        novo_nodo.proximo = self.topo
        self.topo = novo_nodo

    def desempilhar(self):

        if not self.esta_vazia():
            valor = self.topo.valor
            self.topo = self.topo.proximo
            return valor
        return None

    def esta_vazia(self):

        return self.topo is None

    def topo_valor(self):

        if not self.esta_vazia():
            return self.topo.valor
        return None
class Editor:
    def __init__(self):

        self.pilha = Pilha()
        self.texto = ""

    def digitar(self, texto):

        self.pilha.empilhar(self.texto)
        self.texto += texto

    def desfazer(self):

        if not self.pilha.esta_vazia():
            self.texto = self.pilha.desempilhar()

    def mostrar_texto(self):

        return self.texto


# Exemplo de uso
editor = Editor()
editor.digitar("Olá, ")
editor.digitar("mundo!")
print(editor.mostrar_texto())

editor.desfazer()
print(editor.mostrar_texto())

editor.desfazer()
print(editor.mostrar_texto())