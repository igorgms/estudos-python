"""
Formatando valores com modificadores

:s = Texto (strings)
:d - inteiros(int)
:f - Números de ponto flutuante(float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^)(QUANTIDADE)(TIPO s, d ou f)

> - ESQUERDA
< - DIREITA
^ - CENTRO
"""

num1 = 10
num2 = 3

divisao = num1 / num2

# :.2f significa que no resultado da divisão será impresso com duas casas decimais
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')  # Outra forma de fazer

num = 2
print(f'{num:0>10}')

num3 = 12588
print(f'{num3:0<10}')

nome = 'igor gomes'

print(nome.lower())  # Tudo minusculo
print(nome.upper())  # Tudo maiusculo
print(nome.title())  # As primeiras maiusculas