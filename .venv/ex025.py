n = input('Digite seu nome completo: ')

nome_minusculo = n.lower()
partes_do_nome = nome_minusculo.split()

if 'silva' in partes_do_nome:
    print('Você tem Silva como sobrenome')

else:
    print('Você não tem Silva no nome')