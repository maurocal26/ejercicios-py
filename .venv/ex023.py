n = int(input('Digite um numero: '))

print('Analisando o numero {}'.format(n))

milhar = n // 1000
centena = (n % 1000) // 100
dezena = (n % 100) // 10
unidade = n % 10

print('Milhar: {}'.format(milhar))
print('Centena: {}'.format(centena))
print('Dezena: {}'.format(dezena))
print('Unidade: {}'.format(unidade))