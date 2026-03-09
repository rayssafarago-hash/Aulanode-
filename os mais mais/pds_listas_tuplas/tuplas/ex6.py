ranking = []

for _ in range(5):
    nome= input('Filme:').strip()
    ano = input('Ano do filme:').strip()
    nota = float(input("nota:").replace(',','.'))
    ranking.append((nome,ano,nota))
    
    
ranking_ordenado = sorted(ranking,key=lambda x: x[2], reverse=True)
print('\n=== TOP 3 ===')
for i, (nome, ano, nota) in enumerate(ranking_ordenado[:3], start=1):
    print(f'{i} {nome} - {nota} - {ano}')   