"""
Operadores Lógicos
and, or, not
in e not in
"""

usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Igor'
senha_bd = '1234'

if usuario == usuario_bd and senha == senha_bd:
    print('Você está logado!')
else:
    print('Usuário ou senha inválidos!')