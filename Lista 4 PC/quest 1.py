ae = ['a','b','c','d','e']
fj = ['f','g','h','i','j']
ko = ['k','l','m','n','o']
pz = ['p','q','r','s','t','u','v','w','x',',y','z']
textEncrypt = []
def encrypt(text):
    list(text)
    print(text)
    for i in range(len(text)):
        if text[i] in ae:
            textEncrypt.append('1')
        elif text[i] in fj:
            textEncrypt.append('2')
        elif text[i] in ko:
            textEncrypt.append('3')
        elif text[i] in pz:
            textEncrypt.append('4')
        else:
            textEncrypt.append('5')
    return ''.join(textEncrypt)
    
txt = input('Digite o texto: ').lower()
print('Encriptado: {}'.format(encrypt(txt)))