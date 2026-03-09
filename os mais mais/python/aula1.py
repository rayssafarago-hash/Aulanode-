numero_secreto = 7 
for tentativa in range (1,4):
    chute = int(input('tentativa'+ str(tentativa)+'/3. Seu chute:'))
    if chute == numero_secreto:
        print('Acertou')
        break
    else:
        print('errou')