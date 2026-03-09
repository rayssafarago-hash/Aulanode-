CARDAPIO = [('COXINHA', 6.0), ('SUCO', 5.5)]
#TOTAL
soma = 0
for prod, preco in CARDAPIO:
    soma += preco
    print('Total:',soma)

mais_caro = max(CARDAPIO, key=lambda x: x[1])
print('Mais caro:', mais_caro)