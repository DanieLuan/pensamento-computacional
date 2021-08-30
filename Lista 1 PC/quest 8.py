texto = input('texto? ')
i1 = int(input('numero1? '))
i2 = int(input('numero2? '))

if i1 > i2:
  troc = i1
  i1 = i2
  i2 = troc

tamanho = int(len(texto))

if i1 >= tamanho or i2 >= tamanho:
  print('Erro! Índices precisam ser menores do que o tamanho do texto ({})'.format(tamanho))
  exit()

print('Partes')
print('Parte 1: {}'.format(texto[:i1]))
print('Parte 2: {}'.format(texto[:i2]))
print('Parte 3: {}'.format(texto[i1:i2]))
print('Parte 4: {}'.format(texto[i1:]))
print('Parte 5: {}'.format(texto[i2:]))