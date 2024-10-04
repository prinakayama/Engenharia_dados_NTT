saldo = 0.0
depositos = []
saques = []
saques_diarios = 0

while True:
    print("\nOpções:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Visualizar Extrato")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido. Por favor, informe um valor positivo.")
            
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        if saques_diarios < 3 and valor <= 500.0 and valor <= saldo:
            saldo -= valor
            saques.append(valor)
            saques_diarios += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        elif saques_diarios >= 3:
            print("Você já realizou 3 saques diários. Não é possível realizar mais saques hoje.")
        elif valor > 500.0:
            print("Valor de saque inválido. O limite máximo por saque é de R$ 500,00.")
        else:
            print("Você não tem saldo suficiente para realizar este saque.")
            
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        for deposito in depositos:
            print(f"Depósito: R$ {deposito:.2f}")
        for saque in saques:
            print(f"Saque: R$ {saque:.2f}")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")