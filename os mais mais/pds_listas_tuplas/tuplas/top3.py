ranking = []
# cadastrar 5 alunos
for _ in range(5):
    nome= input('Nome:').strip()
    nota = float(input("Nota:").replace(',','.'))
    ranking.append((nome,nota))

#ordenar por nota
ranking_ordenado = sorted(ranking,key=lambda x: x[0], reverse=True)
print('\n=== TOP 3 ===')
for i, (nome,nota) in enumerate(ranking_ordenado[:3], start=1):
    print(f'{i} {nome} - {nota}')   