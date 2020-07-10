usuario = input('Digite o seu nome: ')
qtd_caraceteres = len(usuario)

if qtd_caraceteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres!')
else:
    print('Você foi cadastrado sistema.')