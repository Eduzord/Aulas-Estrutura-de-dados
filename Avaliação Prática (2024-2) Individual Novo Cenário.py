## Para filas encadeadas, um dos possíveis usos seria um sistema de geração de senhas de atendimento, que vai incrementando o contador de senha
# bem como possibilite também atender uma pessoa que seja prioridade:


class NovaSenha:
    def __init__(self, valor = 0, proximo_nodo = None):
        self.dado = valor
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado,self.proximo)


class Fila:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.contador_senha = 1

    ##Aqui eu implementei um método que cria uma nova senha a partir de um atributo da classe fila e após isso
    ## incrementa o atributo, formando uma sequencia de atendimento.
    def inserir(self):
        novo_nodo = NovaSenha(self.contador_senha)
        self.contador_senha += 1

        if self.cabeca == None:

            self.cabeca = novo_nodo
            self.cauda = novo_nodo

        else:

            self.cauda.proximo = novo_nodo
            self.cauda = novo_nodo

    def atender(self):
        self.cabeca = self.cabeca.proximo

    ##Também implementei um método para atender algum número que tenha prioridade de atendimento

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

fila = Fila()
fila.inserir()
print(fila)
fila.inserir()
print(fila)
fila.inserir()
print(fila)
fila.atender()
print(fila)
fila.inserir()
print(fila)