def list():
    N = int(input('N?'))
    lista = []
    print('Quais os valores?')
    for i in range(N):
        aux = int(input(''))
        lista.append(aux)
    return lista

def par(lista):
    minList = [0,0]
    minDist = []
    dist = 0
    for i in lista:
        for j in lista:
            if i != j:            
                dist = abs(i - j)
                minDist.append(dist)
                if dist <= min(minDist):
                    print(i)
                    print(j)
                    minList.insert(0,i)
                    minList.insert(1,j)
    return minList


#Código Principal
lista = list()
parMin = par(lista)
print('Par mais próximo: {} e {}'.format(parMin[0], parMin[1]))