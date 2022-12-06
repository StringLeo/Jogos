from rich.console import Console
from random import choice
from unidecode import unidecode

chars_validos = 'abcdefghijklmnopqrstuvwxyz'

def lugarCorreto(letra):
    return f'[black on green]{letra}[/]'

def letraCorreta(letra):
    return f'[black on yellow]{letra}[/]'

def letraIncorreta(letra):
    return f'[black on white]{letra}[/]'

def verificaLetra(jogada, palavraJogo):
    acertos = []
    for i, letra in enumerate(jogada):
        if jogada[i] == palavraJogo[i]:
            acertos += lugarCorreto(letra.upper())
        elif letra in palavraJogo:
            acertos += letraCorreta(letra.upper())
        else:
            acertos += letraIncorreta(letra.upper())
    acertos.append("\n")
    return acertos

def validaPalavra(palavra):
    try:
        for letra in palavra:
            if letra.lower() not in chars_validos:
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

    palavraJogo = choice(palavras)
    while tentativas < MAX_TENTATIVAS:
        palavraDigitada = input("\nDigite uma palavra: ")    
        console = Console()
        if validaPalavra(palavraDigitada):
            continue
        Acertos += verificaLetra(palavraDigitada, palavraJogo)
        console.print(''.join(Acertos))
        tentativas += 1

        if palavraDigitada == palavraJogo:
            console.print(f'\nVocê ganhou! [black on green]{palavraJogo.upper()}[/] era a palavra secreta.')
            return  True
        elif tentativas == MAX_TENTATIVAS:
            print(f'\n\nQue pena! Você não conseguiu descobrir a palavra secreta')
            break    

if __name__ == '__main__':
    print("\t ----> TERMO <----")
    start()
