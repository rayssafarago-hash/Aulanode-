print('=== Sistema de Menu Escolar ===')

alunos = []

def mostrar_menu():
    print('---MENU---')
    print('1 - Cadastrar aluno')
    print('2 - Calcular média de um aluno')
    print('3 - Listar alunos cadastrados')
    print('0 - Sair')

def casdatrar_aluno():
    nome = input('Nome do aluno:') .strip()

    n1 = float(input('Nota 1:'))
    n2 = float(input('Nota 2:'))

    aluno = {
        'nome': nome,
        'n1': n1,
        'n2': n2}

    alunos.append(aluno)
    print('Aluno cadastrado!')

def calcular_media():
    if len(alunos) == 0:
        print('Nenhum aluno cadastrado ainda!')
        return

    nome = input('Digite o nome do aluno:') .strip()

    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            media = (aluno['n1'] + aluno['n2']) / 2
          
            if media >= 7:
                status = 'Aprovado'
            else:
                status = 'Reprovado'
            print('Media de', aluno['nome'], ':', media, '-', status)
            return

    print('Aluno não encontrado!')

def listar_alunos():
    if len(alunos) == 0:
        print('Nenhum aluno cadastrado ainda!')
        return

    print('---Alunos---')
    for aluno in alunos:
        media = (aluno['n1'] + aluno['n2']) / 2

        print(aluno['nome'], '- média:', media)

def main():
    while True:
        mostrar_menu()
        opcao = input('Escolha uma opção:') .strip()

        if opcao == '1':
            casdatrar_aluno()
        elif opcao == '2':
            calcular_media()
        elif opcao == '3':
            listar_alunos()
        elif opcao == '0':
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida! Tente de novo.')

main()