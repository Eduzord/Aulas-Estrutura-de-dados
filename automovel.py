class Carro:

    def __init__(self, placa = "XX-123", chassi="1234",velocidade=0):
        self.placa = placa
        self.chassi = chassi
        self.velocidade = velocidade
        self._nrodas = 4
        self.__odo = 0

    def get_placa(self):
        return self.placa

    def get_velocidade(self):
        print(f'A velocidade atual é {self.velocidade}km/h')

    def acelerar(self, push):
        self.velocidade += 1 * push
        self.__odo = self.__odo + 1 * push
        return

    def freiar(self):
        if self.velocidade > 0:
            self.velocidade -= 1
        else:
            print("O carro não está em movimento.")
        return

    def set_nrodas(self, n):
        self._nrodas = n

    def buzinar(self):
        print("BI BI")
        return

    def km(self):
        return self.__odo


# Instanciando um objeto

fusca = Carro(placa="SLP-555")

print(fusca.get_placa())



fusca.buzinar()

fusca.get_velocidade()

for i in range(10):
    fusca.acelerar(2)

fusca.get_velocidade()

print(fusca._nrodas)