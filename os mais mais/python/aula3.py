import random
import time

def limpar_tela():
    print("/n"*50)

def exibir_titulo():
    print("="*50)
    print("👾 JOGO DE ADVINHAÇÃO MÁGICA 👾")
    print("="*50)
    print()

    while True:
    
            print("❌ opção inválida! tente novamente.")

def dar_dica(numero_secreto,tentativa):
    if tentativa==numero_secreto:
        return"🎉 ACERTOU!"
    
    diferença=abs(numero_secreto,tentativa)

    if diferença<=5:
        return"🔥 MUITO QUENTE! ESTÁ QUASE LA!"
    elif diferença<=10:
        return" quente! tá perto!"
    elif diferença<=20:
        return"morno... meio perto!"
    elif diferença<=50:
        return"❄ está frio..."
    else:
        return"🧊CONGELANDOOOOO!!!"
    

    def jogar():
        limpar_tela()
        exibir_titulo()

        pontuação_total=0
        rodadas=0

        jogar_novamente="s"
        
        while jogar_novamente.lower()=="s"
        rodadas += 1
        print

    