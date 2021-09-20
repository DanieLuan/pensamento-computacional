qntAlunos = int(input('Quantos alunos? '))
alunosList = []
print('Digite os nomes dos alunos: ')
for i in range(qntAlunos):
    nomeEntry = input('')
    alunosList.append(nomeEntry)
print('Nova Lista:')
for i in range(qntAlunos):
    if (i+1) % 2 !=0:
        print(alunosList[i]) #Mantém os alunos em cadeiras impares
    if (i+1) % 2 == 0 and (qntAlunos % 2) != 0: #Caso a lista seja de numero impar
        print(alunosList[-(i+1)])
    if (i+1) % 2 == 0 and (qntAlunos % 2) == 0: #Caso a lista seja de numero par
        print(alunosList[-(i)])