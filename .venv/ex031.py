d = float(input('qual a distancia da viagem: '))
if d <= 200:
    print('O valor da sua pasagem e {}'.format(d * 0.50))
else:
    print('O valor da sua pasagem e {}'.format(d * 0.45))
