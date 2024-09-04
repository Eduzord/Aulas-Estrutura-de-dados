class Macaco:
    def __init__(self,nome):
        self.nome = nome
        self.bucho = []



    def comer(self,alimento):
        self.bucho.append(alimento)


    def verBucho(self):
        print(self.bucho)

    def digerir(self):
        self.bucho.remove(self.bucho[0])




George = Macaco("George")
George.verBucho()

George.comer("Banana")
George.verBucho()
George.comer("Melancia")
George.verBucho()
George.digerir()
George.verBucho()
