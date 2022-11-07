from conta import Conta

class ContaEspecial(Conta):
    def __init__(self, numero):
        super().__init__(numero)
        self.bonus = 0

    def renderBonus(self):
        super().creditar(self.bonus)
        self.bonus = 0.01
        saldo = float(self.saldo)
        saldo += saldo * self.bonus
        self.set_saldo(saldo)
        self.bonus = 0

    def creditar(self, valor):
        self.bonus = self.bonus + (valor * 0.01)
        super().creditar(valor)