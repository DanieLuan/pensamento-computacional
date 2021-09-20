n = int(input('Qual o N? '))
num = []
print('Digite os valores: ')
for i in range(n):
    numEntry = int(input('{}. '.format(i+1)))
    num.append(numEntry)
op = int(input('Qual a op? '))
A = int(input('Qual o A? '))
B = int(input('Qual o B? '))
while True:
    if op == 0:
        soma = num[A-1] + num[B-1]
        print('{} + {} = {}'.format(num[A-1], num[B-1], soma))
        break
    elif op == 1:
        prod = num[A-1] * num[B-1]
        print('{} * {} = {}'.format(num[A-1], num[B-1], prod))
        break
    else:
        print("Erro! Opção de operação é invalida!")
        op = int(input('Digite a Op novamente: '))