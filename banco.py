import datetime


conta = 0
extrato = []
MAX_SAQUE = 3
LIMITE_SAQUE = 500

menu ="""
========================
MENU
------------------------
Escolha uma das operações abaixo:
------------------------
1) Depositar
2) Sacar
3) Extrato
4) Sair
------------------------"""


def inserir_valor():
    valor_inserido = input("Digite o valor: ")
    try:
        valor = float(valor_inserido)
        if valor >= 0:
            return valor
        else:
            print("------------------------")
            print("\nNão é permitido valor negativo, tente novamente.")
            return False
    except ValueError:
        print("------------------------")
        print("\nO Valor digitado não é um número.")
        return False


def depositar():
    print("------------------------")
    global conta,extrato
    valor = inserir_valor()
    print("------------------------")
    if valor:
        conta += valor
        extrato.append(["Deposito", str(datetime.datetime.now()),valor])
        print("\nO valor foi depositado com sucesso!")


def sacar():
    print("------------------------")
    global conta
    valor = inserir_valor()
    print("------------------------")
    if valor:
        hoje = str(datetime.date.today())
        saques_diarios = 0
        for item in extrato:
            if hoje in item[1] and "Saque" in item[0]:
                saques_diarios += 1
        if saques_diarios < MAX_SAQUE:
            if valor <= LIMITE_SAQUE:
                if valor <= conta:
                    conta -= valor
                    print(f"\nO valor de {valor} foi sacado com sucesso!")
                    extrato.append(["Saque", str(datetime.datetime.now()),"-"+str(valor)])
                else:
                    print(f"\nSaldo insuficiente para o valor {valor}. Verifique saldo disponivel.")
            else:
                print(f"\nO valor solicitado esta acima do limite (R$ {LIMITE_SAQUE}) permitido por transação.")
        else:
            print(f"\nLimites de {MAX_SAQUE} saques diários atingido!")


def ver_extrato():
    print(f"""
========================
EXTRATO
------------------------
Detalhes:""")
    for item in extrato:
        print(item)
    print("------------------------")
    print(f"Seu saldo atual é {conta}")
    print("========================")



while True:
    print(menu)
    operacao = input("Digite a operação desejada: ")
    if operacao is '1':
        depositar()
    elif operacao is '2':
        sacar()
    elif operacao is '3':
        ver_extrato()
    else:
        break
