numDias = int(input('Digite o número de dias: '))
semanas = numDias//7
numDiasResto = numDias%7
#nenhum dia
if numDias == 0:
  print('{} dias equivale à nenhum dia'.format(numDias))
#menos de 1 semana
elif numDias < 7:
  print('{} dias equivale à menos de uma semana'.format(numDias))
#1 semana até 7 dias
elif semanas == 1 and numDias < 8:
  print('{} dias equivalem à {} semana'.format(numDias, semanas))
#1 semana e 1 dia
elif semanas == 1 and numDiasResto == 1:
  print('{} dias equivalem à {} semana e {} dia.'.format(numDias, semanas, numDiasResto))
#1 semana e n dias
elif semanas == 1 and numDias < 14:
  print('{} dias equivalem à {} semana e {} dias.'.format(numDias, semanas, numDiasResto))
#n semanas
elif semanas > 1 and numDiasResto == 0:
  print('{} dias equivalem à {} semanas.'.format(numDias, semanas))
#n semanas e 1 dia
elif semanas > 1 and numDiasResto == 1:
  print('{} dias equivalem à {} semanas e 1 dia.'.format(numDias,semanas))
#n semanas e n dias
else:
  print('{} dias equivalem à {} semanas e {} dias'.format(numDias,semanas,numDiasResto))