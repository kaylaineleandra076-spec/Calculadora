from soma import Soma
from subtracao import Subtracao
from divisao import Divisao
from multiplicacao import Multiplicacao
from exponenciacao import Exponenciacao
 
OPCOES = {
    "1": Soma,
    "2": Subtracao,
    "3": Divisao,
    "4": Multiplicacao,
    "5": Exponenciacao
}
 
def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Valor invalido, digite um numero")
 
def ler_opcao():
    print("\n === Calculadora ===")
    for chave, classe in OPCOES.items():
        print(f"{chave} - {classe.nome}")
    print("0 - Sair")
    
    while True:
        escolha = input("Escolha um opção: ").strip()
        if escolha == "0" or escolha in OPCOES:
            return escolha
        print("Opção invalida")
 
def main():
    while True:
        escolha = ler_opcao()
        if escolha == "0":
            print("Até mais")
            break
 
        a = ler_numero("Digite um Numero: ")
        b = ler_numero("Digite outro Numero: ")
 
        try:
            operacao = OPCOES[escolha](a,b)
            print(f"\nResultado: {operacao}")
        except ZeroDivisionError:
            print("\nErro: não é possível dividir por zero.")
 
if __name__== "__main__":
    main()