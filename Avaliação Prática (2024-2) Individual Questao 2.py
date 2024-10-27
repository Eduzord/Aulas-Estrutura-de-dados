# Questão 2
# A estrutura ligada mais adequada para resolver esse problema seria a PILHA
# Pois o cenário diz que remoção do ultimo elemento inserido é necessária, exigindo uma ordem de saída do tipo LIFO —# último a entrar, primeiro a sair — e a estrutura ligada que nos fornece esse tipo de ordenação é a pilha.


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None

    def adicionar(self, item):
        novo_nodo = Nodo(item)
        novo_nodo.proximo = self.topo
        self.topo = novo_nodo

    def remover(self):

        if not self.esta_vazia():
            valor = self.topo.valor
            self.topo = self.topo.proximo
            return valor
        return None

    def esta_vazia(self):

        return self.topo is None


class Editor:
    def __init__(self):

        self.pilha = Pilha()
        self.texto = ""

    def digitar(self, texto):

        self.pilha.adicionar(self.texto)
        self.texto += texto

    def desfazer(self):

        if not self.pilha.esta_vazia():
            self.texto = self.pilha.remover()

    def mostrar_texto(self):

        return self.texto



editor = Editor()
editor.digitar("Olá, ")
editor.digitar("mundo!")
print(editor.mostrar_texto())

editor.desfazer()
print(editor.mostrar_texto())

editor.desfazer()
print(editor.mostrar_texto())