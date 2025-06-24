import datetime

def main():
    saldo = 0
    limite_saque = 500
    numero_saques_diarios = 0
    LIMITE_SAQUES = 3
    extrato = ""

    while True:
        menu = """
        ================ MENU ================
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [r] Redefinir Saques Diários
        [a] Alterar Limite de Saque
        [q] Sair
        ======================================
        => """
        opcao = input(menu).lower().strip()

        if opcao == "d":
            try: 
                valor = float(input("Informe o valor do depósito: R$ "))
                if valor > 0:
                    saldo += valor
                    data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    extrato += f"{data_hora} - Depósito: R$ {valor:.2f}\n"
                    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
                else:
                    print("Operação falhou! O valor informado é inválido.")
            except ValueError:
                print("Valor inválido! Por favor, digite um número.")

        elif opcao == "s":
            try: 
                valor = float(input("Informe o valor do saque: R$ "))

                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite_saque
                excedeu_saques = numero_saques_diarios >= LIMITE_SAQUES

                if excedeu_saldo:
                    print("Operação falhou! Você não tem saldo suficiente.")
                elif excedeu_limite:
                    print(f"Operação falhou! O valor do saque excede o limite de R$ {limite_saque:.2f}.")
                elif excedeu_saques:
                    print(f"Operação falhou! Número máximo de {LIMITE_SAQUES} saques diários excedido.")
                elif valor > 0:
                    saldo -= valor
                    data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    extrato += f"{data_hora} - Saque:    R$ {valor:.2f}\n"
                    numero_saques_diarios += 1
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                else:
                    print("Operação falhou! O valor informado é inválido.")
            except ValueError:
                print("Valor inválido! Por favor, digite um número.")

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                print(extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "r":
            numero_saques_diarios = 0
            print(f"Contador de saques diários redefinido para 0. Você pode realizar {LIMITE_SAQUES} novos saques.")

        elif opcao == "a":
            try: 
                novo_limite = float(input(f"Informe o novo limite máximo de saque diário (atual: R$ {limite_saque:.2f}): R$ "))
                if novo_limite > 0:
                    limite_saque = novo_limite
                    print(f"Limite de saque diário alterado para R$ {limite_saque:.2f} com sucesso!")
                else:
                    print("Operação falhou! O novo limite deve ser um valor positivo.")
            except ValueError:
                print("Valor inválido! Por favor, digite um número.")

        elif opcao == "q":
            print("Obrigado por usar nosso sistema bancário. Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()