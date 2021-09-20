def imprimePartes(lista, e):

    nList = []
    nSeqList = []
    aux = 0
    #Verifica se todos elementos das listas são iguais
    for i in range(N):
        if lista[i] == e:
            aux += 1
    if N == aux: # Se forem iguais, é pq a lista não possui sequencias
        print('Nenhuma')
        quit()
    #Verificar cada elemento da lista para criar uma nova lista com pequenas listas dentro, sendo elas as pequenas sequências
    for i in lista:
        if i == e:
            nList.append(nSeqList)
            nSeqList = []
        else:
            nSeqList.append(i)
    nList.append(nSeqList)
    for i in range(len(nList)):
        if len(nList[i]) != 0:
            print(nList[i])

# Código Principal
N = int(input('Digite o valor de N: '))

Nlist = []

print('Qual a sequência? ')
for i in range(N):
    Naux = int(input(''))
    Nlist.append(Naux)

elemt = int(input('Qual o elemento separador? '))
print('Sequências resultantes: ')
imprimePartes(Nlist, elemt)