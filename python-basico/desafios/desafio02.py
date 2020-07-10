num = input('Digite um número inteiro: ')

try:
    num = int(num)
    if num % 2 == 0:
        print('O número é par!')
    else:
        print('O número é ímpar!')
except:
    print('O valor digitado não corresponde a um número inteiro!')

