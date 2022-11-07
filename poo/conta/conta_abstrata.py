from abc import ABC, abstractmethod


class ContaAbstrata(ABC):

    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0

    def creditar(self, valor):
        self.saldo = self.saldo + valor

    @property
    @abstractmethod
    def debitar(self, valor):
        pass

    def get_numero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        self.saldo = saldo
