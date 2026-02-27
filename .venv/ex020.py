import random

n1 = input("Primeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Terceiro aluno: ")
n4 = input("Quarto aluno: ")
Lista = [n1,n2,n3,n4]
random.shuffle(Lista)
print('A ordem de aprecentaçao sera {}'.format(Lista))