cont = True
while cont == True:
    n = int(input('n? '))
    if (0<n<10) == False:
        print('Número inválido! Deve ser entre 0 e 10')
    else:
        cont = False
print('')
for i in range(1,n+1):
    print(f"{i}"*i)
    print('')