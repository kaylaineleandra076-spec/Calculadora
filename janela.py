import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTabWidget,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    
)
 
 
from soma import Soma
from subtracao import Subtracao
from multiplicacao import Multiplicacao
from divisao import Divisao
from exponenciacao import Exponenciacao
 
OPERACOES = {
    "+": Soma,
    "-": Subtracao,
    "*": Multiplicacao,
    "/": Divisao,
    "**": Exponenciacao
}
 
ESTILO = """
QWidget {
    background-color: #f2f2f2;
    font-family: Segoe UI, Arial;
}
QLabel#visor {
    background-color: #ffffff;
    border: 1px solid #cccccc;
    color: #222222;
    font-size: 28px;
    padding: 12px;
}
QLabel#conta {
    color: #777777;
    font-size: 13px;
    padding-left: 4px;
}
QPushButton {
    background-color: #ffffff;
    border: 1px solid #cccccc;
    color: #222222;
    font-size: 18px;
    min-width: 56px;
    min-height: 48px;
}
QPushButton:hover {
    background-color: #e8e8e8;
}
QPushButton:pressed {
    background-color: #dcdcdc;
}
"""
 
class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
 
        self.digitado = "0"
        self.primeiro = None
        self.classe = None
        self.zerar = False
 
        self.conta = QLabel("")
        self.conta.setObjectName("conta")
        self.conta.setAlignment(Qt.AlignRight)
 
        self.visor = QLabel(self.digitado)
        self.visor.setObjectName("visor")
        self.visor.setAlignment(Qt.AlignRight)
 
        grade = QGridLayout()
        
        botoes = [
            ("c", 0, 0), ("<", 0, 1), ("+/-", 0, 2), ("/", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("*", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3),
            ("0", 4, 0), (",", 4, 1), ("=", 4, 2)
        ]
 
        for texto, linha, coluna in botoes:
            botao = QPushButton(texto)
            largura = 2 if texto == "=" else 1
            grade.addWidget(botao, linha, coluna, 1, largura)
            botao.clicked.connect(self.criar_acao(texto))
 
        layout = QVBoxLayout()
        layout.addWidget(self.conta)
        layout.addWidget(self.visor)
        layout.addLayout(grade)
        self.setLayout(layout)
 
    def criar_acao(self, texto):
        def acao():
            self.clicar(texto)
        return acao
 
    def clicar(self, texto):
        if texto == "c":
            self.limpar()
        elif texto == "<":
            self.apagar()
        elif texto == "+/-":
            self.inverter_sinal()
        elif texto == "=":
            self.calcular()
        elif texto == ",":
            self.digitar(texto)
        elif texto.isdigit():
            self.digitar(texto)
        else:
            self.escolher_operacao(texto)
 
    def digitar(self, tecla):
        if tecla == "," and "," in self.digitado:
            return
 
        elif self.zerar:
            self.digitado = tecla
            self.zerar = False
 
        elif self.digitado == "0" and tecla != ",":
            self.digitado = tecla
 
        else: 
            self.digitado += tecla
 
        self.visor.setText(self.digitado)
 
    def valor_do_visor(self):
        return float(self.digitado.replace(",","."))
 
    def mostrar(self, numero):
        self.digitado = f"{numero:g}"
        self.zerar = True
        self.visor.setText(self.digitado)
 
    def escolher_operacao(self, simbolo):
        self.primeiro = self.valor_do_visor()
        self.classe = OPERACOES[simbolo]
        self.zerar = True
        self.conta.setText(f"{self.primeiro:g} {simbolo}")
 
    def calcular(self):
        if self.classe is None:
            return
        segundo = self.valor_do_visor()
        operacao = self.classe(self.primeiro, segundo)
 
        try:
            resultado = operacao.calcular()
            self.conta.setText(f"{operacao}")
            self.mostrar(resultado)
            self.primeiro = None
            self.classe = None
        except ZeroDivisionError:
            QMessageBox.warning(self, "Erro", "Divisão por zero")
            self.limpar()
            return
 
    def limpar(self):
        self.digitado = "0"
        self.primeiro = None
        self.classe = None
        self.zerar = False
        self.conta.setText("")
        self.visor.setText(self.digitado)
 
    def apagar(self):
        self.digitado = self.digitado[:-1]
        if self.digitado == "" or self.digitado == "-":
            self.digitado = "0"
        self.visor.setText(self.digitado)
 
    def inverter_sinal(self):
        if self.digitado.startswith("-"):
            self.digitado = self.digitado[1:]
        else:
            self.digitado = "-" + self.digitado
        self.visor.setText(self.digitado)
 
 
def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(ESTILO)
    janela = Calculadora()
    janela.show()
    sys.exit(app.exec())
 
 
if __name__ == "__main__":
    main()
 