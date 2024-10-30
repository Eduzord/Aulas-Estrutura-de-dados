# Questão 1
# A estrutura ligada mais adequada para resolver esse problema seria a FILA
# A justificativa é porque o cenário exige uma ordem de resolução do tipo FIFO, ou seja,
# Primeiro a entrar, primeiro a sair.


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
            self.primeira_tarefa = nova_tarefa
        else:
            self.ultima_tarefa.proxima_tarefa = nova_tarefa
            self.ultima_tarefa = nova_tarefa

    def finalizar_tarefa(self):
            while self.primeira_tarefa.sub_tarefas:
                self.primeira_tarefa.sub_tarefas.finalizar_subtarefa()
                print("Finalizando subtarefa ")
            self.primeira_tarefa = self.primeira_tarefa.proximo


## EXPLICAÇÃO DO CÓDIGO:
## Um objeto Tarefa é criado recebendo como elemento da fila uma outra fila de Subtarefas.
## A fila de subtarefas pode receber até 10 elementos dentro de sí.
## Dentro da FilaDeTarefas, gostariamos de ter implementado um médoto finalizar_tarefa percorrendo toda a fila de subtarefas
## Finalizar toda a fila e então passar para a próxima tarefa.



fila_subtarefas = FilaSubtarefas()
fila_subtarefas.nova_subtarefa("Teste1")
print(fila_subtarefas)
fila_subtarefas.nova_subtarefa("Teste2")
print(fila_subtarefas)

fila_tarefas = FilaDeTarefas()
fila_tarefas.nova_tarefa(fila_subtarefas)
#print(fila_tarefas)
print(fila_tarefas)
fila_tarefas.finalizar_tarefa()
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
