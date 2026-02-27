import math
c1 = float(input("Digite o valor do cateto oposto: "))
c2 = float(input("Digite o valor do cateto adjacente: "))
hi = math.hypot(c1,c2)
print('A hipotenusa vai medir {:.2f}'.format(hi))



