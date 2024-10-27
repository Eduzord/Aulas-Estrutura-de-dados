# Questão 1
# A estrutura ligada mais adequada para resolver esse problema seria a FILA
# Pois o cenário diz que existe uma ordem de prioridade para resolver as subtarefas do tipo FIFO, ou seja,
# primeiro a entrar, primeiro a sair; e a estrutura ligada que pode nos fornecer isto é a Fila encadeada.


class Tarefa:
    def __init__(self,fila_subtarefas,proxima_tarefa = None):
        self.sub_tarefas = fila_subtarefas
        self.proxima_tarefa = proxima_tarefa

    def __repr__(self):
        return "%s -> %s" % (self.sub_tarefas, self.proxima_tarefa)
class Subtarefa:
    def __init__(self,nome_subtarefa, proxima_subtarefa = None):
        self.sub_tarefa = nome_subtarefa
        self.proxima_subtarefa = proxima_subtarefa

    def __repr__(self):
        return "%s -> %s" % (self.sub_tarefa, self.proxima_subtarefa)

class FilaSubtarefas:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return "[" + str(self.primeiro) +"]"

    def nova_subtarefa(self,nome):
        nova_subtarefa = Subtarefa(nome)

        if self.primeiro == None:

            self.primeiro = nova_subtarefa
            self.ultimo = nova_subtarefa

        else:
            corrente = self.primeiro
            contador = 1
            while corrente:
                corrente = corrente.proxima_subtarefa
                contador += 1
            # print(contador)
            if contador <= 10:
                self.ultimo.proxima_subtarefa = nova_subtarefa
                self.ultimo = nova_subtarefa
            else:
                print("Limite de 10 subtarefas atingido!")

    def finalizar_subtarefa(self):
        self.primeiro = self.primeiro.proxima_subtarefa

class FilaDeTarefas:

    def __init__(self):
        self.primeira_tarefa = None
        self.ultima_tarefa = None

    def __repr__(self):
        return "[" + str(self.primeira_tarefa) +"]"
    def nova_tarefa(self,FilaSubtarefas):
        nova_tarefa = Tarefa(FilaSubtarefas)

        if self.primeira_tarefa == None:

            self.primeira_tarefa = nova_tarefa
            self.ultima_tarefa = nova_tarefa
        else:
            self.ultima_tarefa.proxima_tarefa = nova_tarefa
            self.ultima_tarefa = nova_tarefa

    def finalizar_tarefa(self):
        # print(self.primeira_tarefa.sub_tarefas.ultimo)
        while self.primeira_tarefa.sub_tarefas.primeiro:
            self.primeira_tarefa.sub_tarefas.finalizar_subtarefa()
            print("Finalizando subtarefa ")
        print("Todas as subtarefas finalizadas, passando para próxima tarefa...")
        self.primeira_tarefa = self.primeira_tarefa.proxima_tarefa


## EXPLICAÇÃO DO CÓDIGO:
## Um objeto Tarefa é criado recebendo como elemento da fila uma outra fila de Subtarefas.
## A fila de subtarefas só pode receber até 10 elementos dentro de sí.
## Dentro da FilaDeTarefas, o método "finalizar_tarefa" remove cada uma das subtarefas dentro da primeira tarefa na fila até se esgotarem, após isso, o programa atribui a próxima tarefa como a nova primeira da fila

## Não consegui pensar em outra forma de implementar tudo o que foi pedido



fila_subtarefas = FilaSubtarefas()
fila_subtarefas.nova_subtarefa("TestePrimeiraSubtarefas2")
fila_subtarefas.nova_subtarefa("TestePrimeiraSubtarefas2")
print("Imprimindo PRIMEIRO conjunto de subtarefas, composta por duas subtarefas:")
print(fila_subtarefas)
print("\n")

fila_subtarefas1 = FilaSubtarefas()
fila_subtarefas1.nova_subtarefa("TesteSegundaSubtarefas1")
fila_subtarefas1.nova_subtarefa("TesteSegundaSubtarefas2")
print("Imprimindo SEGUNDO conjunto de subtarefas, composta por duas subtarefas:")
print(fila_subtarefas1)
print("\n")

fila_tarefas = FilaDeTarefas()
fila_tarefas.nova_tarefa(fila_subtarefas)
print("Imprimindo fila de tarefas com a PRIMEIRA tarefa inclusa, composta por duas subtarefas")
print(fila_tarefas)
print("\n")

fila_tarefas.nova_tarefa(fila_subtarefas1)
print("Imprimindo fila de tarefas com a SEGUNDA tarefa inclusa, composta por duas subtarefas")
print(fila_tarefas)
print("\n")
print("Executando método para finalizar as subtarefas da PRIMEIRA tarefa da fila")
print("\n")
fila_tarefas.finalizar_tarefa()
print("Imprimindo a fila de tarefas após a PRIMEIRA tarefa finalizada")
print(fila_tarefas)


# fila_subtarefas.nova_subtarefa("Teste3")
# print(fila_subtarefas)
# fila_subtarefas.nova_subtarefa("Teste4")
# print(fila_subtarefas)
# fila_subtarefas.nova_subtarefa("Teste5")
# print(fila_subtarefas)
# fila_subtarefas.nova_subtarefa("Teste6")
# print(fila_subtarefas)
# fila_subtarefas.nova_subtarefa("Teste7")
# print(fila_subtarefas)
# fila_subtarefas.nova_subtarefa("Teste8")
# print(fila_subtarefas)
# fila_subtarefas.nova_subtarefa("Teste9")
# print(fila_subtarefas)
# fila_subtarefas.nova_subtarefa("Teste10")
# print(fila_subtarefas)
# fila_subtarefas.nova_subtarefa("Teste11")
# print(fila_subtarefas)
