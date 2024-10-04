from datetime import datetime
from abc import ABC, abstractclassmethod, abstractproperty
from textwrap import dedent

class ContaCorrente:
    contador_contas = 1

    def __init__(self, agencia, usuario):
        self.agencia = agencia
        self.numero_conta = ContaCorrente.contador_contas
        ContaCorrente.contador_contas += 1
        self.usuario = usuario
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
        self.transacoes_diarias = 0
        self.saques_diarios = 0
        self.ultimo_dia_transacao = None
        self.historico = Historico()

    def __str__(self):
        return f"Conta corrente {self.numero_conta} - Agência {self.agencia} - Usuário {self.usuario.nome}"

    def depositar(self, valor):
        if self.transacoes_diarias < 10:
            if valor > 0:
                self.saldo += valor
                self.depositos.append((valor, datetime.now()))
                self.transacoes_diarias += 1
                self.atualizar_ultimo_dia_transacao()
                self.historico.adicionar_transacao(Deposito(valor))
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Valor de depósito inválido. Por favor, informe um valor positivo.")
        else:
            print("Você excedeu o número de transações permitidas no dia. Por favor, tente novamente amanhã.")

    def sacar(self, valor):
        if self.transacoes_diarias < 10:
            if self.saques_diarios < 3 and valor <= 500.0 and valor <= self.saldo:
                self.saldo -= valor
                self.saques.append((valor, datetime.now()))
                self.transacoes_diarias += 1
                self.saques_diarios += 1
                self.atualizar_ultimo_dia_transacao()
                self.historico.adicionar_transacao(Saque(valor))
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            elif self.saques_diarios >= 3:
                print("Você já realizou 3 saques diários. Não é possível realizar mais saques hoje.")
            elif valor > 500.0:
                print("Valor de saque inválido. O limite máximo por saque é de R$ 500,00.")
            else:
                print("Você não tem saldo suficiente para realizar este saque.")
        else:
            print("Você excedeu o número de transações permitidas no dia. Por favor, tente novamente amanhã.")

    def extrato(self):
        print("Extrato da Conta:")
        for deposito in self.depositos:
            print(f"Depósito: R$ {deposito[0]:.2f} em {deposito[1].strftime('%d-%m-%Y %H:%M:%S')}")
        for saque in self.saques:
            print(f"Saque: R$ {saque[0]:.2f} em {saque[1].strftime('%d-%m-%Y %H:%M:%S')}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def atualizar_ultimo_dia_transacao(self):
        hoje = datetime.now().date()
        if self.ultimo_dia_transacao != hoje:
            self.transacoes_diarias = 1
            self.saques_diarios = 0
            self.ultimo_dia_transacao = hoje
        else:
            self.transacoes_diarias += 1

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []

    def cadastrar_usuario(self, nome, data_nascimento, cpf, endereco):
        if cpf in [u.cpf for u in self.usuarios]:
            print("CPF já cadastrado. Não é possível cadastrar outro usuário com o mesmo CPF.")
            return
        try:
            data_nascimento_obj = datetime.strptime(data_nascimento, "%d-%m-%Y")
        except ValueError:
            print("Data de nascimento inválida. Por favor, informe uma data no formato dd-mm-yyyy.")
            return
        self.usuarios.append(Usuario(nome, data_nascimento_obj, cpf, endereco))
        print(f"Usuário {nome} cadastrado com sucesso!")

    def cadastrar_conta(self, usuario_cpf):
        for usuario in self.usuarios:
            if usuario.cpf == usuario_cpf:
                self.contas.append(ContaCorrente("0001", usuario))
                print(f"Conta corrente criada com sucesso para o usuário {usuario.nome}.")
                return
        print("Usuário não encontrado. Não é possível criar conta corrente.")

    def listar_contas(self):
        for conta in self.contas:
            print(conta)

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao

    def transacoes_do_dia(self):
        data_atual = datetime.utcnow().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"{datetime.now()}: {func.__name__.upper()}")
        return resultado

    return envelope

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """

    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    if not cliente:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # NOTE: não permite cliente escolher a conta
    return cliente

@log_transacao
def depositar(banco):
    numero_conta = int(input("Informe o número da conta: "))
    for conta in banco.contas:
        if conta.numero_conta == numero_conta:
            valor = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)
            break
    else:
        print("Conta não encontrada.")

@log_transacao
def sacar(banco):
    numero_conta = int(input("Informe o número da conta: "))
    for conta in banco.contas:
        if conta.numero_conta == numero_conta:
            valor = float(input("Informe o valor do saque: "))
            conta.sacar(valor)
            break
    else:
        print("Conta não encontrada.")

@log_transacao
def exibir_extrato(banco):
    numero_conta = int(input("Informe o número da conta: "))
    for conta in banco.contas:
        if conta.numero_conta == numero_conta:
            conta.extrato()
            break
    else:
        print("Conta não encontrada.")

@log_transacao
def criar_cliente(banco):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, banco.usuarios)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    banco.cadastrar_usuario(nome, data_nascimento, cpf, endereco)

@log_transacao
def criar_conta(banco):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, banco.usuarios)


def listar_contas(banco):
    for conta in banco.contas:
        print(f"Conta {conta.numero_conta} - Titular: {conta.usuario.nome}")

def main():
    banco = Banco()

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(banco)

        elif opcao == "s":
            sacar(banco)

        elif opcao == "e":
            exibir_extrato(banco)

        elif opcao == "nu":
            criar_cliente(banco)

        elif opcao == "nc":
            criar_conta(banco)

        elif opcao == "lc":
            listar_contas(banco)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

main()