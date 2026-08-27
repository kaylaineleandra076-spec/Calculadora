from operacao import Operacao

class Divisao(Operacao):
    simbolo = "/"
    nome = "Divisão"

    def calcular(self):
        return self.a / self.b