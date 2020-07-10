nome = input('Digite o seu nome: ')

tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print('Seu nome é muito curto!')
elif tamanho_nome <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande!')


