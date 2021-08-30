n = int(input('Digite a quantidade de numeros: '))
f1 = 0
f2 = 1
fibSeq = [f1, f2]
if n == 0:
    print('Sequência de Fibonacci: ')
elif n > 0 and n < 3:
    print(f'Sequência de Fibonacci: {fibSeq[:n]}')
else:
    for f in range(3, n+1):
        fib = f1 + f2
        fibSeq.append(fib)
        f1 = f2
        f2 = fib
    print(f'Sequência de Fibonacci: {fibSeq}')