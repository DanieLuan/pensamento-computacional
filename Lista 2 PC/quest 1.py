n1 = int(input("n1: ")) # entrada do valor N1
while n1 < 2: # se n1 for menor que 2, repita a entrada
    print("Erro! n1 precisa ser maior que 1!")
    n1 = int(input("n1 novamente: "))
n2 = int(input("n2: "))
while n2 < 2: # se n2 for menor que 2, repita a entrada
    print("Erro! n2 precisa ser maior que 1!")
    n2 = int(input("n2 novamente: "))
if n1 > n2: # se n1 for maior que n2, inverta
    n11 = n1
    n1 = n2
    n2 = n11
numImparNprimo = [] # criação da lista com os valores impares e nao primos
divi = 0 # divisores a serem contados
for i in range(n1,n2+1):
    for j in range(1, i+1): # FATORAÇÃO : ver todos os possíveis divisóres do num
        if i % j == 0: # é divisor se o resto for 0
            divi += 1
    if divi > 2 and i % 2 != 0: # SE o num de divi. for > q 2 (nao primo)& num % 2 for resto diferente de 0 (impar)
        numImparNprimo.append(i)
    divi = 0 # reseta os divisores do numero
print(f"números ímpares não primos[{n1}-{n2}]:{numImparNprimo}")