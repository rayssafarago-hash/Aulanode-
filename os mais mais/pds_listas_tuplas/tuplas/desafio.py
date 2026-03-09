#Liste  de itens da cantina (tuplas)
cardapio=[
    ('coxinha', 6.0),
    ('suco', 5.5),
    ('pastel', 7.0),
    ('refrigerante', 6.5)
]

#Mostrar todos os itens
print('Itens do pedido')

for produto, preco in cardapio:
    print(produto, '- R$', preco)

#Calcular total
soma = 0 

for produto, preco in cardapio:
    soma += preco

print('\nTotal do pedido: R$', soma)

#ITEM MAIS CARO
mais_caro = max(cardapio, key=lambda x: x[1])

print('item mais caro:', mais_caro[0])
print('Preço: R$', mais_caro[1])
