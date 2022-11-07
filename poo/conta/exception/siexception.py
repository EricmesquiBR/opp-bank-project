class SIException(Exception):
  def __init__(self, saldo, numero, message='Saldo Insuficiente'):
    self.saldo = saldo
    self.numero = numero
    self.message = message
    super().__init__(self.message)

  def numeroConta(self):
    return self.numero

  def saldoConta(self):
    return self.saldo