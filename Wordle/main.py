from rich.console import Console
from random import choice
from unidecode import unidecode

chars_validos = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def lugarCorreto(letra):
    return f'[black on green]{letra}[/]'

def letraCorreta(letra):
    return f'[black on yellow]{letra}[/]'

def letraIncorreta(letra):
    return f'[black on white]{letra}[/]'

def verificaLetra(jogada, PALAVRA_JOGO):
    acertos = []
    for i, letra in enumerate(jogada):
        if jogada[i] == PALAVRA_JOGO[i]:
            acertos += lugarCorreto(letra)
        elif letra in PALAVRA_JOGO:
            acertos += letraCorreta(letra)
        else:
            acertos += letraIncorreta(letra)
    acertos.append("\n")
    return acertos

def validaPalavra(palavra):
    try:
        for letra in palavra:
            if letra not in chars_validos:
                print(f'\nPor favor, digitar somente palavras.')
                return True
            elif len(palavra) != 5:
                print("\nPor favor, digitar somente palavras com 5 letras.")
                return True
    except:
        return False
    
def start():
    MAX_TENTATIVAS = 6
    tentativas = 0
    Acertos = []

    with open('Wordle/WordList.txt', 'r') as arquivo:
            palavrasAcento = arquivo.read().split()
            palavras = [unidecode(palavra) for palavra in palavrasAcento]
    PALAVRA_JOGO = choice(palavras).upper()

    while True:
        print("\t ----> TERMO <----")
        palavraDigitada = input("\nDigite uma palavra: ").upper()    
        if validaPalavra(palavraDigitada):
            continue
        Acertos += verificaLetra(palavraDigitada, PALAVRA_JOGO)
        console = Console()
        console.print(''.join(Acertos))
        tentativas += 1

        if palavraDigitada == PALAVRA_JOGO:
            console.print(f'\nVocê ganhou! [black on green]{PALAVRA_JOGO}[/] era a palavra secreta.')
            return  True
        elif tentativas == MAX_TENTATIVAS:
            console.print(f'\nQue pena! Você não conseguiu descobrir a palavra secreta([black on white]{PALAVRA_JOGO}[/]).')
            break    

if __name__ == '__main__':
    start()
