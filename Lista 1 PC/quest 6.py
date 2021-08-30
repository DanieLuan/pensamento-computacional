text1 = str(input('Texto 1? ')).lower()
text2 = str(input('Texto 2? ')).lower()
text3 = str(input('Texto 3? ')).lower()

print('Seguem os textos em ordem:')
#Texto 1 sendo o primeiro
if text1 < text2 and text1 < text3:
  print('1o. {}'.format(text1))
  if text2 < text3:
    print('2o. {}'.format(text2))
    print('3o. {}'.format(text3))
  else:
    print('2o. {}'.format(text3))
    print('3o. {}'.format(text2))
#Texto 2 sendo o primeiro
elif text2 < text1 and text2 < text3:
  print('1o. {}'.format(text2))
  if text1 < text3:
    print('2o. {}'.format(text1))
    print('3o. {}'.format(text3))
  else:
    print('2o. {}'.format(text3))
    print('3o. {}'.format(text1))
#Texto 3 sendo o primeiro
else:
  print('1o. {}'.format(text3))
  if text1 < text2:
    print('2o. {}'.format(text1))
    print('3o. {}'.format(text2))
  else:
    print('2o. {}'.format(text2))
    print('3o. {}'.format(text1))