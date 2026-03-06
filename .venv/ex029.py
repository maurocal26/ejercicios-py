km = int(input('Digite o a velocidade do carro: '))
v = (km - 80) * 7
if v > 80:
    print('voce foi multado')
    print('O valor a pagar e de R${}'.format(v))
else:
        print('Velocidade abaixo do limite permitido')






