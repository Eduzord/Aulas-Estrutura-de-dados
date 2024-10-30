class NodoArvore:
    def __init__(self, chave=None, esquerda=None,direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita


    def __repr__(self):
        return  '%s <- %s -> %s' %(self.esquerda and self.esquerda.chave,
                                   self.chave,
                                   self.direita and self.direita.chave)

def em_ordem(raiz):
    if not raiz:
        return
    # Visita filho da esquerda.
    em_ordem(raiz.esquerda)

    # Visita nodo corrente.
    print(raiz.chave)

    # Visita filho da direita.
    em_ordem(raiz.direita)





# raiz = NodoArvore(3)
# raiz.esquerda = NodoArvore(5)
# raiz.direita = NodoArvore(1)
# print("Árvore: ", raiz)

raiz = NodoArvore(40)

raiz.esquerda = NodoArvore(20)
raiz.direita = NodoArvore(60)

raiz.direita.esquerda = NodoArvore(50)
raiz.direita.direita = NodoArvore(70)
raiz.esquerda.esquerda = NodoArvore(10)
raiz.esquerda.direita = NodoArvore(30)

print(raiz)

em_ordem(raiz)