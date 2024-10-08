class nodoFila:
    def __init__(self, id = 0,nome = "default",prioridade = 0,espera = 0, proximo_nodo = None):

        self.id = id
        self.name = nome
        self.priority = prioridade
        self.wait = espera
        self.proximo = proximo_nodo



    def __repr__(self):
        return '\n[ %s\n %s\n %s\n %s]\n-> %s' % ("Id: "+str(self.id),"Name: "+self.name, "Priority: "+str(self.priority),"Wait: " +str(self.wait), self.proximo)


class Fila:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def __repr__(self):
        return "[" + str(self.cabeca) +"]"

    def push(self,id,nome,prioridade,espera):
        novo_nodo = nodoFila(id,nome,prioridade,espera)

        if self.cabeca == None:

            self.cabeca = novo_nodo
            self.cauda = novo_nodo

        else:

            self.cauda.proximo = novo_nodo
            self.cauda = novo_nodo
    def exibir_processos(self):
        print(self)

    def executar_processo(self):
        self.cabeca = self.cabeca.proximo
    def matar_maior_tempo_de_espera(self):
        corrente = self.cabeca
        anterior = None
        maior_tempo = 0
        while corrente:
            if corrente.wait > maior_tempo:
                maior_tempo = corrente.wait
            anterior = corrente
            corrente = corrente.proximo

        print(f'Eliminando processo com maior tempo de espera: {maior_tempo}')
        corrente = self.cabeca
        anterior = None
        if corrente.wait == maior_tempo:
            self.cabeca = corrente.proximo
        else:
            while corrente and corrente.wait != maior_tempo:
                anterior = corrente
                corrente = corrente.proximo
            if corrente.wait == maior_tempo:
                anterior.proximo = corrente.proximo

fila = Fila()
fila.push(104,"Window Manager",4,5)
fila.push(101,"Processo 1",3,10)
fila.push(99,"Processo 2",1,25)
fila.push(99,"Processo 3",5,15)
print("Exibindo processos\n")
fila.exibir_processos()

fila.matar_maior_tempo_de_espera()
print("Mostrando processos após matar maior tempo de espera \n")
fila.exibir_processos()

print("Mostrando processos antes de executar_processo\n")
fila.exibir_processos()
print("Executando método executar_processo\n")
fila.executar_processo()
fila.exibir_processos()

