class CarroRua:
    """Esta classe representa um nodo de uma estrutura encadeada"""
    def __init__(self, placa = 0, nodo_anterior = None):
        self.placa = placa
        self.anterior = nodo_anterior

    def __repr__(self):
        return "%s -> %s" %(self.placa,self.anterior)

class RuaEstreita:

    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def inserir_nodo(self, novo_dado):
        # Cria um novo nodo com o dado a ser armazenado.

        novo_nodo = CarroRua(novo_dado)

        # Faz com que o novo nodo seja o topo da pilha.

        novo_nodo.anterior = self.topo

        # Faz com que a cabeça da lista referencie o novo nodo.
        self.topo = novo_nodo

    def remover_nodo(self):
        assert self.topo, "Impossível remover valor de pilha vazia."

        self.topo = self.topo.anterior

    def busca_carro(self,placa):
        atual = self.topo
        while atual and atual.placa != placa:
            atual = atual.anterior
        if not atual:
            print("Carro não está estacionado na rua")
        else:
            print("Carro está estacionado na rua")

    def remover_carro(self,placa):
        atual = self.topo
        fila_remover = []
        while atual and atual.placa != placa:
            fila_remover.append(atual.placa)
            atual = atual.anterior
        if not atual:
            print("Carro não está estacionado na rua")
        else:
            print(f"Para remover o carro deve-se o(s) remover {fila_remover}")


rua = RuaEstreita()
rua.inserir_nodo(321)
print(rua)
rua.inserir_nodo(219)
print(rua)
rua.inserir_nodo(567)
print(rua)
rua.busca_carro(219)
rua.remover_carro(111)
