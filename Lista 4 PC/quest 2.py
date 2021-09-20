def line():
    print('-' * 30)

def principal():
    
    saldo = 1000;
    while True:
        opcao = exibeOpcoes()
        if opcao == 4:
            print('Obrigado por usar os serviços do Caixa Eletrônico')
            line()
            break
        saldo = processaOpcoes(opcao,saldo)
        
def exibeOpcoes():
    line()
    print('Qual operacao voce deseja realizar?')
    line()
    print('1 - SAQUE')
    print('2 - DEPOSITO')
    print('3 - SALDO')
    print('4 - SAIR')
    opcao = int(input('Escolha:')) 
    line()
    return opcao

def processaOpcoes(opcao,saldo):
    if opcao == 1: #funcionalidade saque
        valor_saque = float(input('Qual valor você deseja sacar? R$ '))
        saldo = saque(saldo,valor_saque)
    elif opcao == 2: #funcionalidade deposito
        valor_deposito = float(input('Qual o valor você deseja depositar? R$ '))
        saldo = deposito(saldo, valor_deposito)
    elif opcao == 3: #funcionalidade saldo
        saldoF(saldo)
    else :
      print('Opção inválida, tente novamente!')
    return saldo

def deposito(saldo, valorDeposito):
    if valorDeposito > 0:
        saldo += valorDeposito
        line()
        print('O valor do saldo agora é de R$ {}'.format(saldo))
        line()
    else:
        line()
        print('Valor inválido')
        line()
    return saldo

def saque(saldo,valorSaque):
    if valorSaque <= saldo:
        saldo -= valorSaque
        line()
        print('Saque autorizado. Agora o seu saldo atual é de: R$ {}'.format(saldo))
        line()
    else:
        line()
        print('Saldo insuficiente.')
        line()
    return saldo

def saldoF(saldo):
    line()
    print('O valor do saldo da conta é de R$ {}'.format(saldo))
    line()

#Programa principal
principal()