s = float(input('Digite o seu salario: '))
if s <= 1250:
    print('Esse e seu salario com o aumento {}'.format((s * 10) / 100 + s))
else:
    print('Sua aumento e de 15%')
    print('{}'.format((s * 15) / 100 + s))