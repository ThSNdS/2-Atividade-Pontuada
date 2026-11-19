import os
os.system('cls')

lista_extratos = []
saldo = 500.00
tentativas = 0
login_correto = 'Adm'
senha_correta = '456'
depositos = 0
saques = 0
def mostrar_saldo():
    print(f'\nSeu saldo equivale a: {saldo:.2f}')
    input('Pressione uma tecla para prossigir.')
def depositar():
    deposito = float(input('Digite a quantidade que deseja despositar: '))
    if deposito <= 0:
        print('Valor inválido.')
        print(f'O saldo continua: {saldo:.2f}')
        return 0
    else:
        print(f'O saldo atualizado é: {saldo + deposito}')
        lista_extratos.append(deposito)
        return deposito
def sacar():
    saque = float(input('Digite a quantidade que deseja sacar: '))
    if saque <= 0:
        print('Valor inválido, nenhuma quantidade retirada.')
        print(f'O saldo continua: {saldo}')
        return 0
    elif saque > saldo:
        print('Valor inválido, saque maior que saldo disponivel.')
        print(f'O saldo continua: {saldo}')
        return 0
    elif saque > 1000.00:
        print('Valor inválido, saque maior que do o limite.')
        print(f'O saldo continua: {saldo}')
        return 0
    else:
        saque_total = saque * -1
        lista_extratos.append(saque_total)
        return saque_total
def mostrar_extrato():
    if len(lista_extratos) == 0:
        print('Sem Extrato.')
    else:
        for i in range(len(lista_extratos)):
            numero = lista_extratos[i]
            if numero < 0:
                tipo = 'Depósito'
                depositos += 1
            else:
                tipo = 'Saque'
                saques += 1
            print(f'Extrato: {tipo} de {numero}')
        print(f'Foram {depositos} depósitos e {saques} saques.')
    input('Pressione uma tecla para continuar...')

while tentativas < 3:
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
    if login == login_correto and senha == senha_correta:
        print('Acesso gratido!')
        break
    else:
        print('Login ou senha incorreto.')
        tentativas += 1

if tentativas < 3:
    while True:
        os.system('cls')
        opcao = input('''
    === BANCO COFRINHO ° CAIXA ===
    1 - Ver saldo
    2 - Depositar
    3 - Sacar
    4 - Ver extrato
    0 - Sair
    _______________________________
    Escolha uma opçâo: ''')
        match opcao:
            case '1':
                mostrar_saldo()
            case '2':
                deposito_final = depositar()
                saldo += deposito_final
                input('Pressione uma tecla para continuar...')
            case '3':
                saque_final = sacar()
                saldo += saque_final
                input('Pressione uma tecla para continuar...')
            case '4':
                mostrar_extrato()
            case '0':
                input('O Programa ira finalizar pressione uma tecla para encerrar.')
                break
            case _:
                print(f'\nOpção inválida.')
                input('Pressione uma tecla para prossigir.')
else:
    exit
