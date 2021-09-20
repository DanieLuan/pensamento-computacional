while True:
    nQntd = int(input('Qual o valor de N? '))
    if nQntd > 2:
        break
    else:
        print('N deve ser maior que 2!')
nNum = []
print('Digite os dados: ')
for i in range(nQntd):
    nAux = float((input(' ')))
    nNum.append(nAux)
    if nNum[i] < nNum[i-1] and i>1:
        print('Erro! Os números devem estar em ordem crescente!')
        quit()
#1 e 3 Quartil
n1Quartil = nNum[int(nQntd*(1/4))]
n3Quartil = nNum[int(nQntd*(3/4))]
#Mediana
if nQntd % 2 != 0:
    mediana = nNum[int(len(nNum)/2)]
else:
    meio1 = nNum[int(len(nNum)/2)]
    meio2 = nNum[int(len(nNum)/2)-1]
    mediana = (meio1+meio2) /2
#Limite Inferior
interQuart = n3Quartil-n1Quartil
limInfAux =  n1Quartil - interQuart*1.5
limInf = nNum[1]
minF = []
for i in nNum:
    distF = abs(i-limInfAux)
    minF.append(distF)
    if distF <= min(minF):
        limInf = i
#Limite superior
limSupAux = interQuart*1.5 + n3Quartil
limSup = nNum[1]
Min = []
for i in nNum:
    dist = abs(i-limSupAux)
    Min.append(dist)
    if dist <= min(Min):
        limSup = i
#Final
print('~'*30)
print('Limite Inferior: {}'.format(limInf))
print('1o Quartil: {}'.format(n1Quartil))
print('Mediana: {}'.format(mediana))
print('3o Quartil: {}'.format(n3Quartil))
print('Limite Superior: {}'.format(limSup))
print('~'*30)