import random

print('===JOGO(RANDOM)===')

numero_secreto=random.randint(1,10)

for tentativa in range(1,4):
    chute=int(input('tentativa'+str(tentativa)+'/3. seu chute:'))

    if chute==numero_secreto:
        print('Acertou!')
        break
    else:
        print('Errou!')
print('o número secreto era:',numero_secreto)