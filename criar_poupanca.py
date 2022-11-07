from poo.conta.conta_poupanca import ContaPoupanca
from poo.conta.conta import Conta
class CriarPoupanca:
    if __name__ == '__main__':

        conta = Conta("21.342-7")
        conta = ContaPoupanca(conta)
        conta.creditar(500.87)
        conta.debitar(45.00)
        print(conta.get_saldo())

        conta.render_juros(0.05)
        print(conta.get_saldo())
        #conta = Conta("21.342-7")
        #print(type(conta))
        #conta = ContaPoupanca("21.342-7")
        #print(type(conta))
    
        #conta.creditar(500.87)
        #conta.debitar(45.00)
        #print(conta.get_saldo())
        

