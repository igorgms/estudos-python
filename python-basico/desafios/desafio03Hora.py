horario = input('Qual é o horário: ')

try:
    horario = int(horario)

    if horario <= 11:
        print('Bom dia!')
    elif horario <= 17:
        print('Boa tarde!')
    elif horario <= 23:
        print('Boa noite!')
    else:
        print('O horário não existe!')
except:
    print('O valor digitado não corresponde a nenhum horário!')