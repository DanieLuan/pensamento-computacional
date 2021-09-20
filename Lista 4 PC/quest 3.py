def line():
    print('-'*30)

def primo(num):
    diviList = []
    for i in range(1,num+1):
        if num % i == 0:
            diviList.append(i)
    return diviList


#Codigo Principal
line()
N = int(input('Qual o valor de N? '))
line()
num = []
print('Digite os valores:')
for i in range(N):
    numAux = int(input(''))
    num.append(numAux)
line()
print('A classificação é:')

for i in range(N):
    divi = len(primo(num[i]))
    if divi == 2:
        print('{} é primo'.format(num[i]))
    else:
        print('{} não é primo, os divisores são: {}'.format(num[i], primo(num[i])))