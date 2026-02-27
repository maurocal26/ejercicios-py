d = int(input('Por quantos dias o carro foi alugado? : '))
km = float(input('quantos km o carro percorreu? : '))
P = (d * 60) + (km * 0.15)
print('Preço a pagar: {} R$'.format(P))


