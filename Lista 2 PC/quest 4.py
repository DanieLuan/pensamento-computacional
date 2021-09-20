print("-"*30)
n1 = int(input('Digite n1: '))
n2 = int(input('Digite n2: '))
while (1 <= n1 <= n2 <= 10) == False:
    print("~"*30)
    print('Erro, 1 <= n1 <= n2 <= 10 | Tente novamente')
    print("~"*30)
    n1 = int(input('Digite n1: '))
    n2 = int(input('Digite n2: '))
for i in range(n1,n2+1):
    print("-"*8, end="")
    print(f" Tabuada de {i} ", end="")
    print("-"*8)
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")