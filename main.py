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
        print(f"{cores['vermelho']}{fx['negrito']}MAIS UM ERRO E VOCÊ SERÀ ENFORCADO!{limpar}")


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


def jogo():
    with open("palavras.txt", "r", encoding="utf-8") as f:
        palavras = [row[0:len(row)-1] for row in f]
    with open("dicas.txt", "r", encoding="utf-8") as f:
        dicas = [row[0:len(row)-1] for row in f]
    escolhida = choice(palavras)
    index = palavras.index(escolhida)
    dica = dicas[index]
    dif = 0
    while dif != 1 and dif != 2 and dif != 3:
        try:
            print("-=" * 40)
            print(f"Bem-vindo ao jogo da {cores['ciano']}{fx['negrito']}Forca{limpar}!")
            print(f"Escolha sua {cores['vermelho']}dificuldade{limpar}:")
            print(f"{cores['vermelho']}{fx['negrito']}(1) DIFÍCIL: 60 segundos por jogada{limpar}")
            print(f"{cores['amarelo_claro']}{fx['negrito']}(2) MÉDIO: 90 segundos por jogada{limpar}")
            print(f"{cores['verde_claro']}{fx['negrito']}(3) FÁCIL: 120 segundos por jogada{limpar}")
            dif = int(input("Escolha uma opção: "))
        except ValueError:
            print(f"{cores['vermelho']}Digite um número!{limpar}")
    play(escolhida, dif, dica)


def add():
    with open("palavras.txt", "a", encoding="utf-8") as f:
        with open('dicas.txt', 'a', encoding='utf-8') as dicas:
            print(f"=========={cores['verde_claro']}ADICIONAR{limpar}==========")
            palavra = dica = ''
            while True:
                palavra = input("Digite a palavra a ser adicionada: ").strip().lower()
                if ' ' not in palavra:
                    dica = input(f"Digite a dica da palavra '{palavra}': ").strip().lower()
                    break
                else:
                    print(f"{cores['vermelho']}DIGITE UMA PALAVRA VÁLIDA, SEM ESPAÇOS!{limpar}")

            f.write(palavra + '\n')
            dicas.write(dica + '\n')
            main()


def rmv():
    with open("palavras.txt", "r", encoding='utf-8') as f:
        palavras = [row[0:len(row) - 1] for row in f]
    with open("dicas.txt", 'r', encoding='utf-8') as f:
        dicas = [row[0:len(row) - 1] for row in f]
    print(f"=========={cores['vermelho']}REMOVER{limpar}==========")
    while True:
        palavra = input("Digite a palavra a ser removida: ").lower().strip()
        # palavra += '\n'
        if palavra in palavras:
            indice = palavras.index(palavra)
            palavras.pop(indice)
            dicas.pop(indice)
            break
        else:
            print(f"{cores['vermelho']}PALAVRA NÃO ENCONTRADA NO BANCO DE DADOS...{limpar}")
    palavrasstr = ''
    for txt in palavras:
        palavrasstr += (txt + '\n')
    dicasstr = ''
    for txt in dicas:
        dicasstr += (txt + '\n')
    with open("palavras.txt", "w", encoding='utf-8') as f:
        f.write(palavrasstr)
    with open("dicas.txt", "w", encoding='utf-8') as f:
        f.write(dicasstr)
    main()


def main():
    print(f"{cores['verde_claro']}Olá! Deseja jogar, adicionar palavra ao banco ou remover palavra do banco?")
    print(f"{cores['ciano']}{fx['negrito']}(1) JOGAR")
    print(f"{cores['verde_claro']}(2) ADICIONAR PALAVRA")
    print(f"{cores['vermelho']}(3) REMOVER PALAVRA{limpar}")
    escolha = input("Escolha sua opção: ")
    if escolha == '1':
        jogo()
    elif escolha == '2':
        add()
    elif escolha == '3':
        rmv()
    else:
        print("ESCOLHA UMA OPÇÃO VÁLIDA!")
        main()


if __name__ == '__main__':
    main()
