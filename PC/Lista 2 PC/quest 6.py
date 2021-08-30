cont = True
while cont == True:
    n1 = int(input('n1? '))
    n2 = int(input('n2? '))
    if n2 > n1:
        cont = False
    else:
        print('Erro! n2 precisa ser maior que n1!')
qPrim = 0
prim = []
divi = 0
for i in range(n1,n2+1):
    for j in range(1,i+1):
        if i % j == 0:
            divi += 1
    if divi == 2:
        qPrim += 1
        prim.append(i)
    divi = 0
print('*'*30)
print(f'Existem {qPrim} numero(s) primo(s) entre {n1} e {n2}!')
print(f'Eles são: {prim}')
print('*'*30)