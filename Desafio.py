print("Escolha a opção Desejada:")

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[t] Transferência

==> """

saldo = 4000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "s":
        print("Saque")
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "t":
        print("Transferência")
        valor = float(input("Informe o valor da transferência: "))
        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Transferência: R$ {valor:.2f}\n"
            print(f"Transferência de R$ {valor:.2f} realizada com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "e":
        print("\n========== Extrato ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================================")
    elif opcao == "q":
        print("Sair")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
