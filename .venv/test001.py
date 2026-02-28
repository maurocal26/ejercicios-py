import math

print('=== CALCULADORA DE CILINDRO ===')
raio = float(input('Digite o raio do cilindro (em cm): '))
altura = float(input('Digite a altura do cilindro (em cm): '))

# Cálculos
area_base = math.pi * (raio ** 2)
area_lateral = 2 * math.pi * raio * altura
area_total = 2 * area_base + area_lateral
volume = math.pi * (raio ** 2) * altura

# Resultados
print('\n=== RESULTADOS ===')
print(f'Área da base: {area_base:.2f} cm²')
print(f'Área lateral: {area_lateral:.2f} cm²')
print(f'Área total do cilindro: {area_total:.2f} cm²')
print(f'Volume: {volume:.2f} cm³')