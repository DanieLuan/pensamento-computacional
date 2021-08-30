n1 = int(input('n1? '))
n2 = int(input('n2? '))
n3 = int(input('n3? '))

#Definindo o número maior começando por n1
maior = n1
if n2 > n1 and n2 > n3:
  maior = n2
if n3 > n1 and n3 > n2:
  maior = n3
#Definindo o número menor começando por n3
menor = n3
if n2 < n1 and n2 < n3:
  menor = n2
if n1 < n2 and n1 < n3:
  menor = n1
#Definindo o número do meio começando por n2
meio = n2
if n1 > n2 and n1 < n3:
  meio = n1
if n1 < n2 and n1 > n3:
  meio = n1
if n3 > n2 and n3 < n1:
  meio = n3
if n3 < n2 and n3 > n1:
  meio = n3
#Situação onde todos são diferentes
if n1 != n2 and n2 != n3 and n3 != n1: 
  print('Maior: {0}'.format(maior))
  print('Menor: {0}'.format(menor))
  print('Meio: {0}'.format(meio))
#Todos são iguais
elif n1 == n2 and n2 == n3:
  print('Todos são iguais a {}'.format(n1))
#Situações onde 2 são iguais
#n1=n2
if n1 == n2 and n1 != n3:
  if n1 > n3:
    print('Maiores: {}'.format(n1))
    print('Menor: {}'.format(n3))
  else:
    print('Maior: {}'.format(n3))
    print('Menores: {}'.format(n1))
#n1=n3
if n1 == n3 and n1 != n2:
  if n1 > n2:
    print('Maiores: {}'.format(n1))
    print('Menor: {}'.format(n2))
  else:
    print('Maior: {}'.format(n2))
    print('Menores: {}'.format(n1))
#n2=n3
if n2 == n3 and n2 != n1:
  if n2 > n1:
    print('Maiores: {}'.format(n2))
    print('Menor: {}'.format(n1))
  else:
    print('Maior: {}'.format(n1))
    print('Menores: {}'.format(n2))