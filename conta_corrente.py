# REGRAS
# Deposito não aceitar valor negativos, 
# Saque não permitir mais de 3 operações com limite maximo de R$ 500,00 diários e não sendo possivel deixar a conta com valor negativo de saldo,
# Extrato todas as operações registrados com debito e crédito.

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor para depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação Falhou! O valor informado é inválido!")
        
    elif opcao == "s":
        valor = float(input("Informe o valor para saque: "))
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Falhou! Saldo Insuficiente.")

        elif excedeu_limite:
            print("Operação Falhou! Limite Excedido.")

        elif excedeu_saques:
            print("Operação Falhou! Quantidade de Saque excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            # print("Sucesso na Operação! Você ralizou {numero_saques} no dia de hoje.")
        else:
            print("Operação Falhou! Valor Invalido.")
            
    elif opcao == "e":
        print("\n================ Extrato ================")
        print("Não foram realizadas movimentação." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")
        
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, selecione novamente a operação desejada!")
