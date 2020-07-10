nome = 'Igor Gomes Firmino'
idade = 26
altura = 1.80
peso = 90.5
ano_atual = 2020
ano_nasc = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura} mts de altura, e pesa {peso} Kgs')
print(f'o IMC de {nome} é: {imc:.2f}')
print(f'{nome} nasceu em {ano_nasc}')