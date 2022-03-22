from random import choice
from time import time
from cores import *

palavra_certa = ''
letras_usadas = []
vidas = 7
primeira = True
display = ''


def venceu(palavra):
    tem_letra = False
    for char in palavra:
        if char != '_':
            tem_letra = True
    return False if tem_letra else True


def printar_boneco(vidas_l):
    if vidas_l == 7:
        print("|-------| ")
        print("|      ---")
        print("|         ")
        print("|         ")
        print("---       ")
    elif vidas_l == 6:
        print("|-------| ")
        print("|      ---")
        print("|       O ")
        print("|         ")
        print("---       ")
    elif vidas_l == 5:
        print("|-------| ")
        print("|      ---")
        print("|       O ")
        print("|       | ")
        print("---       ")
    elif vidas_l == 4:
        print("|-------| ")
        print("|      ---")
        print("|       O ")
        print("|      /| ")
        print("---       ")
    elif vidas_l == 3:
        print("|-------| ")
        print("|      ---")
        print("|       O ")
        print("|      /|\\ ")
        print("---       ")
    elif vidas_l == 2:
        print("|-------| ")
        print("|      ---")
        print("|       O ")
        print("|      /|\\ ")
        print("---    / ")
    elif vidas_l == 1:
        print("|-------| ")
        print("|      ---")
        print("|       O ")
        print("|      /|\\ ")
        print("---    / \\ ")


def play(escolhida, dificuldade, dica):
    if dificuldade == 1:
        dificuldade = 60
    elif dificuldade == 2:
        dificuldade = 90
    elif dificuldade == 3:
        dificuldade = 120
    global vidas, primeira, display, palavra_certa
    print("-" * 50)
    print(f"{cores['ciano']}{fx['negrito']}JOGO DA FORCA{limpar}")
    printar_boneco(vidas)
    if primeira:
        display = '_' * len(escolhida)
        palavra_certa = escolhida
        primeira = False
    for char in display:
        print(char, end="")
    print()
    print(f"{cores['amarelo_claro']}{fx['negrito']}DICA: {dica}{limpar}")
    print("Letras usadas: ", end="")
    for letra in letras_usadas:
        print(letra, end=", ")
    print()
    tempo_play = time()
    chute = input("Digite uma letra: ").upper()[0]
    tempo_play = round(time() - tempo_play)
    if tempo_play > dificuldade:
        print(f"{cores['vermelho']}{fx['negrito']}VOCÊ DEMOROU DEMAIS!")
        print(f"Você demorou {tempo_play} segundos, e o máximo era {dificuldade}...")
        print(f"{cores['vermelho']}{fx['negrito']}FIM DE JOGO {limpar}")
        vidas = 7
        letras_usadas.clear()
        primeira = False
        display = ''
        return False
    if chute in letras_usadas:
        print(f"{cores['vermelho']}{fx['negrito']}LETRA JÁ ESCOLHIDA...{limpar}")
        play(escolhida, dificuldade, dica)
    elif chute.isalpha():
        letras_usadas.append(chute)
        if chute in escolhida.upper():
            qtd_chute = escolhida.upper().count(chute)
            for i in range(qtd_chute):
                pos = escolhida.upper().index(chute)
                lst = list(display)
                lst[pos] = chute
                display = ''.join(lst)
                lst = list(escolhida)
                lst[pos] = '_'
                escolhida = ''.join(lst)
            print(f"{cores['verde_claro']}Acertou!{limpar}")
            if venceu(escolhida):
                vidas = 7
                letras_usadas.clear()
                primeira = False
                display = ''
                print(f"{cores['verde_claro']}Parabéns, você venceu!!!")
                print(f"A palavra era {fx['negrito']}{cores['amarelo']}" + palavra_certa + f"{limpar}{cores['verde_claro']}!")
                print(f"{cores['verde_claro']}{fx['negrito']}FIM DE JOGO {limpar}")
                return True
            else:
                play(escolhida, dificuldade, dica)
        else:
            if vidas <= 1:
                vidas = 7
                letras_usadas.clear()
                display = ''
                print(f"{cores['branco']}Você foi enforcado...")
                print(f"A palavra certa era {fx['negrito']}{cores['amarelo']}" + palavra_certa + f"{limpar}")
                print(f"{cores['vermelho']}{fx['negrito']}FIM DE JOGO {limpar}")
                return False
            vidas -= 1
            print(f"{cores['vermelho']}Errou...{limpar}")
            play(escolhida, dificuldade, dica)
    else:
        print(f"{cores['vermelho']}{fx['negrito']}DIGITE UMA LETRA VÁLIDA!{limpar}")
        play(escolhida, dificuldade, dica)


def main():
    with open("palavras.txt", "r", encoding="utf-8") as f:
        palavras = [row[0:len(row)-1] for row in f]
    with open("dicas.txt", "r", encoding="utf-8") as f:
        dicas = [row[0:len(row)-1] for row in f]
    escolhida = choice(palavras)
    index = palavras.index(escolhida)
    dica = dicas[index]
    print("-=" * 40)
    print(f"Bem-vindo ao jogo da {cores['ciano']}{fx['negrito']}Forca{limpar}!")
    print(f"Escolha sua {cores['vermelho']}dificuldade{limpar}:")
    print(f"{cores['vermelho']}{fx['negrito']}(1) DIFÍCIL: 60 segundos por jogada{limpar}")
    print(f"{cores['amarelo_claro']}{fx['negrito']}(2) MÉDIO: 90 segundos por jogada{limpar}")
    print(f"{cores['verde_claro']}{fx['negrito']}(3) FÁCIL: 120 segundos por jogada{limpar}")
    dif = int(input("Escolha uma opção: "))
    play(escolhida, dif, dica)


if __name__ == '__main__':
    main()