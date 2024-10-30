# 5. No seu sistema operacional ao abrir o “gerenciador de tarefas”
# você pode exibir os processos que estão em execução, veja como
# isso é apresentado no windows:

# Você já parou pra pensar como é possível executar todos esses
# aplicativos em apenas um processador? Isso existe graças a uma
# funcionalidade chamada de tempo compartilhado (“timeshared”). Essa funcionalidade mantém uma sequência de
# processos em uma fila, esperando para serem executados.
# Modifique a fila dinâmica que você implementou anteriormente
# para armazenar as informações desses processos.

# Você já parou pra pensar como é possível executar todos esses
# aplicativos em apenas um processador? Isso existe graças a uma
# funcionalidade chamada de tempo compartilhado (“timeshared”). Essa funcionalidade mantém uma sequência de
# processos em uma fila, esperando para serem executados.
# Modifique a fila dinâmica que você implementou anteriormente
# para armazenar as informações desses processos.

# Explicação do Código:
# Classe Processo:

# __init__(self, nome, tempo_execucao): Cria um objeto para representar um processo com atributos
# nome e tempo_execucao.
# Classe Nodo:

# __init__(self, processo): Define um nodo que contém um processo (objeto Processo) 
# e uma referência para o próximo nodo na fila.
# Classe FilaDeProcessos:

# adicionar_processo(self, nome, tempo_execucao): 
# Método para adicionar um processo ao final da fila. 
# Ele cria um novo objeto Processo, o coloca em um Nodo,
# e adiciona esse nodo ao final da fila.
# remover_processo(self): Método para remover o primeiro 
# processo da fila e retornar suas informações. Ajusta as
# referências de início e fim conforme necessário.
# imprimir_fila(self): Percorre a fila e imprime 
# o nome e o tempo de execução de cada processo para visualizar a ordem dos processos na fila.
# esta_vazia(self): Verifica se a fila está vazia, retornando True ou False.
# Exemplo de Uso:

# Adiciona processos à fila, exibe a fila original, remove o primeiro processo
# e exibe a fila novamente para demonstrar como a fila de processos é manipulada.
# Essa implementação simula como um sistema de tempo compartilhado gerencia a
# execução de múltiplos processos em um processador, mantendo a ordem de chegada 
# e permitindo adicionar, remover e visualizar processos facilmente. 

class Processo:
    def __init__(self, nome, tempo_execucao):
        # Inicializa um processo com um nome e um tempo de execução
        self.nome = nome
        self.tempo_execucao = tempo_execucao


class Nodo:
    def __init__(self, processo):
        # Inicializa um nodo com um processo e uma referência para o próximo nodo (inicialmente None)
        self.processo = processo
        self.proximo = None


class FilaDeProcessos:
    def __init__(self):
        # Inicializa a fila com referências para o início e o final (ambos começam como None)
        self.inicio = None  # O primeiro processo na fila
        self.fim = None  # O último processo na fila

    def adicionar_processo(self, nome, tempo_execucao):
        # Cria e insere um novo processo no final da fila
        novo_processo = Processo(nome, tempo_execucao)  # Cria um novo processo com as informações fornecidas
        novo_nodo = Nodo(novo_processo)  # Cria um novo nodo contendo o processo
        if self.fim is None:
            # Se a fila está vazia, o novo nodo será o primeiro e o último
            self.inicio = novo_nodo
            self.fim = novo_nodo
        else:
            # Se a fila não está vazia, adiciona o novo nodo ao final e atualiza a referência
            self.fim.proximo = novo_nodo
            self.fim = novo_nodo

    def remover_processo(self):
        # Remove e retorna o primeiro processo da fila, se não estiver vazia
        if self.inicio is None:
            # Se a fila está vazia, não há nada para remover
            return None
        
        # Guarda o processo que será removido
        processo_removido = self.inicio.processo
        
        # Atualiza o início da fila para o próximo nodo
        self.inicio = self.inicio.proximo
        
        if self.inicio is None:
            # Se a fila ficou vazia após remover, também atualiza o fim para None
            self.fim = None
        
        # Retorna o processo removido
        return processo_removido

    def imprimir_fila(self):
        # Percorre e imprime todos os processos na fila
        atual = self.inicio  # Começa a partir do primeiro processo na fila
        while atual is not None:
            # Imprime o nome e o tempo de execução do processo
            print(f"Processo: {atual.processo.nome}, Tempo de Execução: {atual.processo.tempo_execucao}s")
            atual = atual.proximo  # Move para o próximo processo
        print()  # Adiciona uma nova linha ao final da impressão

    def esta_vazia(self):
        # Verifica se a fila está vazia (início será None)
        return self.inicio is None


# Exemplo de uso
fila = FilaDeProcessos()  # Cria uma nova instância de FilaDeProcessos

# Adiciona alguns processos à fila
fila.adicionar_processo("Processo A", 5)
fila.adicionar_processo("Processo B", 3)
fila.adicionar_processo("Processo C", 8)
fila.adicionar_processo("Processo D", 2)

# Imprime a fila de processos
print("Fila de Processos Original:")
fila.imprimir_fila()

# Remove um processo e imprime a fila novamente
fila.remover_processo()  # Remove "Processo A"
print("Fila de Processos após remover o primeiro processo:")
fila.imprimir_fila()
