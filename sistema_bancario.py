def menu():
    menu = '''\n
    Escolha uma opção abaixo:
    ======================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo usuário
    [5]\tNova conta
    [6]\tListas contas
    [7]\tSair
    ======================

    ->'''
    return input((menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n=== Operação falhou, valor informado inválido! ===")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limites_saques):
    excedeu_saques = numero_saques >= limites_saques
    excedeu_limite = valor > limite
    excedeu_saldo = valor > saldo

    if excedeu_saldo:
        print("\n=== Operação falhou! Você não tem saldo suficiente. ===")

    elif excedeu_limite:
        print("\n=== Operação falhou! O valor do saque excede o limite. ===")

    elif excedeu_saques:
        print("\n=== Operação falhou! Número máximo de saques excedido. ===")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque R$ {valor: .2f}\n"
        numero_saques += 1
        print("\n === Saques realizado com sucesso! ===")
    
    else:
        print("\n=== Operação falhou! O valor informado é inválido. ===")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("=============== Extrato =================")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Já existe usuário cadastrado com esse CPF! ===")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente números):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    else:
        print("\n=== Usuário não encontrado, fluxo de ciração de conta encerrado! ===")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
                Agência: {conta['agencia']}
                C/C: {conta['numero_conta']}
                Titular: {conta['usuario']['nome']}
                """
        print("=" * 100)
        print(linha)

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito:"))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque:"))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limites_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("Operação inválida, por favor selecione a operação desejada.")

main ()