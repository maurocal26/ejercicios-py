f = str(input('Digite uma frase: ')).strip().upper()
f2 = f.count('A')
f3 = f.find('A')
f4 = f.rfind('A')
print('Sua frase aparece {} vezes'.format(f2))
print('Aparece pela primeira vez {}'.format(f3))
print('Aparece pela ultima vez {}'.format(f4))

