A = str(input('Digite o texto A: '))
B = str(input('Digite o texto B: '))

meioA = int(len(A)/2)
meioB = int(len(B)/2)
print('Texto A dividido em duas Partes: {} e {}'.format(A[:meioA], A[meioA:]))
print('Texto B dividido em duas Partes: {} e {}'.format(B[:meioB], B[meioB:]))
print('{} + {} = {}'.format(A[:meioA], B[meioB:], A[:meioA]+B[meioB:]))
print('{} + {} = {}'.format(A[meioA:], B[:meioB], A[meioA:]+B[:meioB]))
print('{} + {} + {} + {} = {}'.format(A[0], B[1], A[-1], B[-1], A[0]+B[1]+A[-1]+B[-1]))