import random
import getpass
import sys


HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


WORD_LIST = [
    'python', 'programacao', 'computador', 'algoritmo', 'variavel',
    'funcao', 'lista', 'dicionario', 'arquivo', 'teste'
]


def escolher_palavra():
    escolha = input('Deseja inserir uma palavra secreta (professor)? (s/N): ').strip().lower()
    if escolha == 's':
        try:
            palavra = getpass.getpass('Digite a palavra secreta (será ocultada): ').strip().lower()
        except Exception:
            palavra = input('Digite a palavra secreta: ').strip().lower()
        palavra = ''.join(ch for ch in palavra if ch.isalpha())
        if not palavra:
            print('Palavra inválida — será escolhida aleatoriamente.')
            return random.choice(WORD_LIST)
        return palavra
    else:
        return random.choice(WORD_LIST)


def mostrar_estado(palavra, letras_adivinhadas, tentativas):
    print(HANGMAN_PICS[6 - tentativas])
    exibicao = ' '.join([ch if ch in letras_adivinhadas else '_' for ch in palavra])
    print('\nPalavra: ', exibicao)
    print('Letras adivinhadas:', ' '.join(sorted(letras_adivinhadas)))
    print(f'Tentativas restantes: {tentativas}\n')


def jogar():
    palavra = escolher_palavra()
    letras_adivinhadas = set()
    tentativas = 6

    while tentativas > 0:
        mostrar_estado(palavra, letras_adivinhadas, tentativas)

        if all(ch in letras_adivinhadas for ch in palavra):
            print('Parabéns — você descobriu a palavra:', palavra)
            return

        entrada = input('Digite uma letra: ').strip().lower()
        if not entrada or len(entrada) != 1 or not entrada.isalpha():
            print('Entrada inválida — digite uma única letra.\n')
            continue

        letra = entrada
        if letra in letras_adivinhadas:
            print('Você já tentou essa letra. Tente outra.')
            continue

        letras_adivinhadas.add(letra)
        if letra not in palavra:
            tentativas -= 1
            if tentativas == 0:
                mostrar_estado(palavra, letras_adivinhadas, tentativas)
                print('Fim de jogo — você perdeu. A palavra era:', palavra)
                return


def main():
    print('--- Jogo da Forca ---')
    while True:
        jogar()
        again = input('\nJogar novamente? (s/N): ').strip().lower()
        if again != 's':
            print('Obrigado por jogar!')
            break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nJogo interrompido pelo usuário.')
        try:
            sys.exit(0)
        except SystemExit:
            pass