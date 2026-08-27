from operacao import Operacao

class Exponenciacao(Operacao):
    simbolo = "**"
    nome = "Exponenciação"

    def calcular(self):
        return self.a ** self.b