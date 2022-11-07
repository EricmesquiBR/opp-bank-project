from poo.conta.conta import Conta


class CriarConta:

   if __name__ == '__main__':
       conta = Conta('21.342-7')
       conta.creditar(500.87)
       conta.debitar(45.00)
       print(conta.get_saldo())
