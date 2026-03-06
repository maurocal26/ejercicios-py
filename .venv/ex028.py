import random
print('-' * 35)
print('Adivinhe o Numero')
print('-' * 35)

n = random.randint(1, 5)
palpite = 0
print(f'Vou pensar em um numero entre 1 e 5')
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





