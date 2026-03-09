nomes = ['Carla', 'Ana', 'Bruno']
print('Original:', nomes)

ordenado = sorted(nomes, key=str.lower)
print('Sorted:', ordenado)

nomes.sort(key=str.lower)
print('Sort:',nomes)