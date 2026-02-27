from math import radians, sin, cos, tan
ang = float(input('digite um angulo qualquer: '))
sen = sin(radians(ang))
print('O angulo {} tem Seno de {:.2f}'.format(ang, sen))
cos = cos(radians(ang))
print('O angulo {} tem Cosseno de {:.2f}'.format(ang, cos))
tan = tan(radians(ang))
print('O angulo {} tem Tangente de {:.2f}'.format(ang, tan))
