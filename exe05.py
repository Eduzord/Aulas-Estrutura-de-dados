# Para implementar o comportamento do comando Ctrl + Z (que normalmente serve como um comando de
#  desfazer) usando uma estrutura de dados de pilha, você pode seguir a lógica de empilhar ações
# (ou estados) quando elas ocorrem e desempilhá-las quando o usuário deseja desfazer a última ação.

class Nodo:
    def __init__(self, valor):
        # Inicializa um nodo com um valor e uma referência para o próximo nodo (inicialmente None)
        self.valor = valor
        self.proximo = None


class Pilha:
    def __init__(self):
        # Inicializa a pilha com o topo como None (sem itens)
        self.topo = None

    def empilhar(self, item):
        # Cria um novo nodo e o empilha no topo da pilha
        novo_nodo = Nodo(item)  # Cria um novo nodo com o valor do item
        novo_nodo.proximo = self.topo  # O próximo do novo nodo é o antigo topo
        self.topo = novo_nodo  # Atualiza o topo para o novo nodo

    def desempilhar(self):
        # Remove e retorna o item do topo da pilha, se não estiver vazia
        if not self.esta_vazia():
            valor = self.topo.valor  # Obtém o valor do nodo no topo
            self.topo = self.topo.proximo  # Atualiza o topo para o próximo nodo
            return valor  # Retorna o valor removido
        return None  # Retorna None se a pilha estiver vazia

    def esta_vazia(self):
        # Verifica se a pilha está vazia
        return self.topo is None  # Se topo é None, a pilha está vazia

    def topo_valor(self):
        # Retorna o valor do nodo no topo da pilha sem removê-lo
        if not self.esta_vazia():
            return self.topo.valor  # Retorna o valor do topo
        return None  # Retorna None se a pilha estiver vazia


class Editor:
    def __init__(self):
        # Inicializa um objeto Editor com uma pilha e uma string de texto vazia
        self.pilha = Pilha()  # Cria uma nova pilha para armazenar os estados
        self.texto = ""  # Inicializa o texto como uma string vazia

    def digitar(self, texto):
        # Adiciona texto ao editor e salva o estado atual na pilha
        self.pilha.empilhar(self.texto)  # Salva o estado atual do texto
        self.texto += texto  # Adiciona o novo texto

    def desfazer(self):
        # Restaura o último estado salvo na pilha
        if not self.pilha.esta_vazia():  # Verifica se a pilha não está vazia
            self.texto = self.pilha.desempilhar()  # Restaura o estado anterior

    def mostrar_texto(self):
        # Retorna o texto atual no editor
        return self.texto


# Exemplo de uso
editor = Editor()  # Cria uma nova instância do Editor
editor.digitar("Olá, ")  # Digita "Olá, "
editor.digitar("mundo!")  # Digita "mundo!"
print(editor.mostrar_texto())  # Saída: Olá, mundo!

editor.desfazer()  # Desfaz a última ação (remove "mundo!")
print(editor.mostrar_texto())  # Saída: Olá, 

editor.desfazer()  # Desfaz novamente (remove "Olá, ")
print(editor.mostrar_texto())  # Saída: (string vazia)
