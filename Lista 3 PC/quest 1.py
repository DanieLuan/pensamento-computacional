qntNomes = int(input('Quantos nomes? '))
nomes = []
for i in range(qntNomes):
    nome = input('Nome {}: '.format(i+1))
    nomes.append(nome)  
nomes.reverse()
print('Você digitou: ')
for i in range(qntNomes):
    print('{}'.format(nomes[i]))