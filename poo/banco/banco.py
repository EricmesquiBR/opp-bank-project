from poo.conta.conta import Conta
from poo.conta.conta_poupanca import ContaPoupanca

class Banco:

    def __init__(self):
        self.contas = [None] * 100
        self.indice = 0

    def cadastrar(self, conta: Conta):
        self.contas[self.indice] = conta
        self.indice += 1

    def procurar_conta(self, numero):
        i = 0
        achou = False
        while achou is False and i < self.indice:
            if self.contas[i].get_numero() == numero:
                achou = True
            else:
                i += 1
        if achou is True:
            return self.contas[i]
        else:
            return None

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
        else:
            print("Conta Inexistente!")

    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        else:
            print("Conta Inexistente!")

    def saldo(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            return conta.get_saldo()
        else:
            print("Conta Inexistente!")

    def transferir(self, origem, destino, valor):
        origem = self.procurar_conta(origem)
        destino = self.procurar_conta(destino)

        if origem and destino:
            if self.saldo(origem.get_numero()) >= valor:
                origem.debitar(valor)
                destino.creditar(valor)
                print("Transferência realizada com sucesso!")
            else:
                print("Saldo Insuficiente, faça um empréstimo")
        else:
            print("Transferência Impossível! Conta Inexistente!")

    def render_juros(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            if isinstance(conta, ContaPoupanca):
                conta.render_juros(0.01)
                print("Saldo com juros: {}".format(conta.get_saldo()))
            else:
                print("Conta não é poupança!")