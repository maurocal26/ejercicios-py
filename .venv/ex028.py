import random
print('-' * 35)
print('Adivinhe o Numero')
print('-' * 35)

n = random.randint(1, 1000)
palpite = 0
print(f'Vou pensar em um numero entre 1 e 1000')
while palpite != n:

    palpite = int(input('Em que numero eu pensei? : '))


    if palpite < n:
        print('Muito baixo tente novamente!')
    elif palpite > n:
        print('Muito alto tente novamente!')
    else:
        print('-' * 35)
        print('Parabéns voce acertou!')
        print('-' * 35)





