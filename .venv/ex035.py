r1 = int(input('Primeiro comprimento: '))
r2 = int(input('Segundo comprimento: '))
r3 = int(input('Terceiro comprimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Eles podem formar um triângulo!')

    if r1 == r2 == r3:
        print('Tipo: EQUILÁTERO (todos lados iguais)')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Tipo: ISÓSCELES (dois lados iguais)')
    else:
        print('Tipo: ESCALENO (todos lados diferentes)')
else:
    print('NÃO podem formar um triângulo!')