from time import sleep

print('\033[7;46;30mOlá, Seja bem vindo!\033[m')
print('Vamos resolver uma conta de matemática?')
print('PROCESSANDO...')
sleep(2.5)
v = int(input(('Quanto é 12 x 2? :')))
if v == 24:
    print('PARABÉNS! Você ACERTOU.')
else:
    print('QUE PENA, Você ERROU. Tente novamente')
