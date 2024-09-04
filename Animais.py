from abc import ABC, ABCMeta, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.qtd_patas = 4
        self.pares_de_asas = 0
        self.pupila = "circular"

    @abstractmethod
    def Comunicar(self):
        print("Olá!")

    def Quantas_Patas(self):
        print(self.qtd_patas)

    def ModPatas(self, patas):
        self.qtd_patas = patas

class Cachorro(Animal):
    def __init__(self,nome):
        Animal.__init__(self,nome)

    def Comunicar(self):
        print("Au au!")

class Gato(Animal):
    def __init__(self,nome):
        Animal.__init__(self,nome)
        self.pupila = "vertical"

    def Comunicar(self):
        print("Miau")

class Cavalo(Animal):
    def __init__(self,nome):
        Animal.__init__(self,nome)
        self.pupila = "horizontal"

    def Comunicar(self):
        print("Iiirrrrí")

class Peixe(Animal):
    def __init__(self,nome):
        Animal.__init__(self,nome)
        Peixe.ModPatas(self,0)


    def Comunicar(self):
        print("Glub glub")



bingo = Cachorro('Bingo')
bingo.Comunicar()
bingo.Quantas_Patas()

snow = Gato("Snow")
snow.Comunicar()
print(snow.pupila)
snow.Quantas_Patas()

nelson = Peixe("Nelson")
nelson.Quantas_Patas()

jorge = Cavalo("Jorge")
jorge.Comunicar()
jorge.Quantas_Patas()
print(jorge.pupila)