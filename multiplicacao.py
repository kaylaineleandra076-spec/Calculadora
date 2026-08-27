from operacao import Operacao

class Multiplicacao(Operacao):
    simbolo = "*"
    nome = "Multiplicação"

    def calcular(self):
        return self.a * self.b