class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self):
        return f"Usuário {self.nome} - CPF {self.cpf}"

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
        self.saques_diarios = 0

    def __str__(self):
        return f"Conta corrente {self.numero_conta} - Agência {self.agencia} - Usuário {self.usuario.nome}"

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido. Por favor, informe um valor positivo.")

    def sacar(self, valor):
        if self.saques_diarios < 3 and valor <= 500.0 and valor <= self.saldo:
            self.saldo -= valor
            self.saques.append(valor)
            self.saques_diarios += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        elif self.saques_diarios >= 3:
            print("Você já realizou 3 saques diários. Não é possível realizar mais saques hoje.")
        elif valor > 500.0:
            print("Valor de saque inválido. O limite máximo por saque é de R$ 500,00.")
        else:
            print("Você não tem saldo suficiente para realizar este saque.")

    def extrato(self):
        print("Extrato da Conta:")
        for deposito in self.depositos:
            print(f"Depósito: R$ {deposito:.2f}")
        for saque in self.saques:
            print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []

    def cadastrar_usuario(self, nome, data_nascimento, cpf, endereco):
        if cpf in [u.cpf for u in self.usuarios]:
            print("CPF já cadastrado. Não é possível cadastrar outro usuário com o mesmo CPF.")
            return
        self.usuarios.append(Usuario(nome, data_nascimento, cpf, endereco))
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

banco = Banco()

while True:
    print("\nOpções:")
    print("1. Cadastrar usuário")
    print("2. Cadastrar conta corrente")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Visualizar Extrato")
    print("6. Listar contas")
    print("7. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        cpf = input("Informe o CPF (somente números): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        banco.cadastrar_usuario(nome, data_nascimento, cpf, endereco)
    elif opcao == "2":
        usuario_cpf = input("Informe o CPF (somente números): ")
        banco.cadastrar_conta(usuario_cpf)
    elif opcao == "3":
        numero_conta = int(input("Informe o número da conta: "))
        for conta in banco.contas:
            if conta.numero_conta == numero_conta:
                valor = float(input("Informe o valor do depósito: "))
                conta.depositar(valor)
                break
            else:
               print("Conta não encontrada.")
    elif opcao == "4":
        numero_conta = int(input("Informe o número da conta: "))
        for conta in banco.contas:
            if conta.numero_conta == numero_conta:
                valor = float(input("Informe o valor do saque: "))
                conta.sacar(valor)
                break
        else:
            print("Conta não encontrada.")
    elif opcao == "5":
        numero_conta = int(input("Informe o número da conta: "))
        for conta in banco.contas:
            if conta.numero_conta == numero_conta:
                conta.extrato()
                break
        else:
            print("Conta não encontrada.")
    elif opcao == "6":
        for conta in banco.contas:
         print(f"Conta {conta.numero_conta} - Titular: {conta.usuario.nome}")
    elif opcao == "7":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")