from poo.banco.banco_lista import BancoLista
from poo.conta.conta import Conta


class CriarBanco:

    if __name__ == '__main__':
        #criando objs do tipo conta
        contaA = Conta('21.342-7')
        contaA.set_saldo(700)

        contaB = Conta('21.342-8')
        contaB.set_saldo(400)

        # criando obj do banco e cadastrando contas
        # banco = Banco()
        banco = BancoLista()
        banco.cadastrar(contaA)
        banco.cadastrar(contaB)

        print(type(banco.procurar_conta(contaA.get_numero()).get_numero()))
        print(type(banco.procurar_conta(contaB.get_numero())))

        banco.debitar(contaA.get_numero(),100)
        print(banco.saldo(contaA.get_numero()))

        banco.creditar(contaA.get_numero(),200)
        print(banco.saldo(contaA.get_numero()))

        banco.transferir(contaA.get_numero(), contaB.get_numero(), 800)

        banco.render_juros(contaA.get_numero())

