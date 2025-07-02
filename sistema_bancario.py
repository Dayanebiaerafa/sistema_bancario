import datetime
import textwrap

# --- Função do Menu ---
def exibir_menu():
    menu_opcoes = """
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [r]\t Redefinir Saques do Dia
    [a]\t Alterar Limite de Saque
    [nu]\t Novo Cliente
    [nc]\t Nova Conta
    [lu]\t Ver Clientes
    [lc]\t Ver Contas
    [q]\t Sair do Banco
    """
    print("\n================ MENU ================")
    print(textwrap.dedent(menu_opcoes).strip())
    print("======================================")
    return input("=> Sua escolha: ").lower().strip()

# --- Funções Auxiliares (Ajudantes) ---

def buscar_usuario(cpf, usuarios):
    """Busca um usuário na lista pelo CPF. Retorna o usuário ou None."""
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def buscar_conta(numero_conta, contas):
    """Busca uma conta na lista pelo número. Retorna a conta ou None."""
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            return conta
    return None

# --- Funções de Operações do Banco ---

# Funções que NÃO precisam das "constantes" diretamente:
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"{data_hora}\t\tDepósito:\tR$ {valor:.2f}\n"
        print(f"=== Depósito de R$ {valor:.2f} feito com SUCESSO! ===")
    else:
        print("@@@ Erro: O valor para depositar tem que ser positivo! @@@")
    return saldo, extrato

def visualizar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Nenhuma movimentação foi feita ainda." if not extrato else extrato)
    print(f"Saldo atual:\t\tR$ {saldo:.2f}")
    print("==========================================")

# Funções que AGORA precisam receber as "constantes" como argumento:
def sacar(*, saldo, valor, extrato, limite_saque_por_transacao, numero_saques, limite_saques_diarios):
    if valor <= 0:
        print("@@@ Erro: O valor para sacar tem que ser positivo! @@@")
    elif valor > saldo:
        print("@@@ Erro: Você não tem saldo suficiente! @@@")
    elif valor > limite_saque_por_transacao: # Usa o parâmetro
        print(f"@@@ Erro: O valor de saque excede o limite de R$ {limite_saque_por_transacao:.2f}. @@@")
    elif numero_saques >= limite_saques_diarios: # Usa o parâmetro
        print(f"@@@ Erro: Você já fez seu limite de {limite_saques_diarios} saques diários. @@@")
    else:
        saldo -= valor
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        extrato += f"{data_hora}\t\tSaque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f"=== Saque de R$ {valor:.2f} feito com SUCESSO! ===")
    return saldo, extrato, numero_saques

def redefinir_saques_diarios(numero_saques_atuais, limite_saques_diarios):
    """Redefine o contador de saques diários para 0."""
    print(f"=== Contagem de saques do dia zerada. Você pode fazer {limite_saques_diarios} novos saques! ===")
    return 0

def alterar_limite_saque(limite_atual_param): 
    """Permite ao usuário alterar o limite máximo por saque. Retorna o novo limite."""
    try:
        novo_limite = float(input(f"Qual o NOVO limite máximo por saque (o atual é R$ {limite_atual_param:.2f})? R$ "))
        if novo_limite > 0:
            print(f"=== Limite de saque alterado para R$ {novo_limite:.2f} com SUCESSO! ===")
            return novo_limite
        else:
            print("@@@ Erro: O novo limite precisa ser um valor positivo! @@@")
    except ValueError:
        print("@@@ Erro: Valor inválido! Digite um NÚMERO para o limite. @@@")
    return limite_atual_param 

def criar_conta_corrente(contas, usuarios, agencia_fixa): 
    """Cria uma nova conta corrente vinculada a um usuário existente."""
    cpf_titular = input("Qual o CPF do cliente para vincular à conta: ")
    titular = buscar_usuario(cpf_titular, usuarios)
    
    if not titular:
        print("\n@@@ Erro: Cliente não encontrado! Cadastre o cliente primeiro. @@@")
        return contas

    numero_nova_conta = len(contas) + 1
    
    contas.append({
        "agencia": agencia_fixa, 
        "numero_conta": numero_nova_conta,
        "usuario": titular,
        "saldo": 0,
        "extrato": "",
        "numero_saques_hoje": 0
    })
    print(f"\n=== Conta {agencia_fixa}-{numero_nova_conta} criada para {titular['nome']}! ===")
    return contas

# --- Funções de Cadastro (Não precisam das "constantes" como parâmetro) ---

def criar_usuario(usuarios):
    """Cadastra um novo usuário no sistema."""
    cpf = input("Qual o CPF do cliente (somente números, por favor): ")
    if buscar_usuario(cpf, usuarios):
        print("\n@@@ Erro: Já existe um cliente com este CPF! @@@")
        return usuarios

    nome = input("Qual o nome completo do cliente: ")
    data_nascimento = input("Qual a data de nascimento (DD-MM-AAAA): ")
    endereco = input("Qual o endereço (Rua, Nro - Bairro - Cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("\n=== Cliente cadastrado com SUCESSO! ===")
    return usuarios

def listar_usuarios(usuarios):
    print("\n============== LISTA DE CLIENTES ==============")
    if not usuarios:
        print("Nenhum cliente cadastrado ainda.")
        return

    for i, cliente in enumerate(usuarios):
        print("-" * 25 + f" Usuário {i+1} " + "-" * 25)
        print(f"{'Nome:':<15}{cliente['nome']}")
        print(f"{'CPF:':<15}{cliente['cpf']}")
        print(f"{'Data de Nasc.:':<15}{cliente['data_nascimento']}")
        print(f"{'Endereço:':<15}{cliente['endereco']}")
        print("-" * 65)
    print("===============================================")

def listar_contas(contas):
    print("\n=============== LISTA DE CONTAS ===============")
    if not contas:
        print("Nenhuma conta cadastrada ainda.")
        return

    for i, conta in enumerate(contas):
        print("-" * 25 + f" Conta {i+1} " + "-" * 25)
        print(f"{'Agência:':<20}{conta['agencia']}")
        print(f"{'Número da Conta:':<20}{conta['numero_conta']}")
        print(f"{'Titular:':<20}{conta['usuario']['nome']}")
        print(f"{'CPF do Titular:':<20}{conta['usuario']['cpf']}")
        print(f"{'Saldo:':<20}R$ {conta['saldo']:.2f}")
        print("-" * 60)
    print("===============================================")

# --- Função Principal do Banco (Onde Tudo Acontece!) ---

def main():
    # As "constantes" 
    AGENCIA_FIXA = "0001"
    limite_saque_por_transacao = 500 # Variável local, minúscula por convenção
    limite_saques_diarios = 3       # Variável local, minúscula por convenção

    usuarios = []
    contas = []

    while True:
        opcao = exibir_menu()

        if opcao in ("d", "s", "e", "r"):
            if not contas:
                print("@@@ Erro: Nenhuma conta cadastrada. Crie uma conta primeiro. @@@")
                continue
            
            try:
                num_conta = int(input("Qual o NÚMERO da conta para operar: "))
                conta = buscar_conta(num_conta, contas)
                
                if not conta:
                    print("@@@ Erro: Conta não encontrada. Verifique o número. @@@")
                    continue

                if opcao == "d":
                    valor = float(input("Quanto você quer depositar? R$ "))
                    conta["saldo"], conta["extrato"] = depositar(conta["saldo"], valor, conta["extrato"])
                elif opcao == "s":
                    valor = float(input("Quanto você quer sacar? R$ "))
                    # Passando as "constantes" como argumentos para a função sacar
                    conta["saldo"], conta["extrato"], conta["numero_saques_hoje"] = \
                        sacar(saldo=conta["saldo"], valor=valor, extrato=conta["extrato"],
                              limite_saque_por_transacao=limite_saque_por_transacao, # Passa como argumento
                              numero_saques=conta["numero_saques_hoje"],
                              limite_saques_diarios=limite_saques_diarios) # Passa como argumento
                elif opcao == "e":
                    visualizar_extrato(conta["saldo"], extrato=conta["extrato"])
                elif opcao == "r":
                    # Passando a constante como argumento
                    conta["numero_saques_hoje"] = redefinir_saques_diarios(conta["numero_saques_hoje"], limite_saques_diarios)
            except ValueError:
                print("@@@ Erro: Valor inválido! Digite um número para a conta ou valor. @@@")

        elif opcao == "a":
            # A main agora atualiza sua própria variável local
            limite_saque_por_transacao = alterar_limite_saque(limite_saque_por_transacao)
            
        elif opcao == "nu":
            usuarios = criar_usuario(usuarios)
        
        elif opcao == "nc":
            # Passando a constante como argumento
            contas = criar_conta_corrente(contas, usuarios, AGENCIA_FIXA)

        elif opcao == "lu":
            listar_usuarios(usuarios)
        
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("=== Obrigado por usar nosso sistema bancário. Volte sempre! ===")
            break

        else:
            print("@@@ Erro: Opção inválida! Escolha uma das opções do menu. @@@")

if __name__ == "__main__":
    main()