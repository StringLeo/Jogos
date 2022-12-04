from rich.console import Console
from random import choice
from unidecode import unidecode

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
    return acertos

def verificaVitoria(palavraDigitada, palavraJogo):
    console = Console()
    if palavraDigitada == palavraJogo:
        console.print(f'\nVocê ganhou! [black on green]{palavraJogo.upper()}[/] era a palavra secreta.')
        return  True

def validaPalavra(palavra):
    try:
        palavra = float(palavra)
        if isinstance(palavra, (float, int)):
            print(f'\nPor favor, digitar somente palavras.')
            return True
    except:
        palavra = str(palavra)
    if len(palavra) != 5:
        print("\nPor favor, digitar somente palavras com 5 letras.")
        return True

def start():
    DIGITAR_PALAVRA = "\nDigite uma palavra: "
    MAX_TENTATIVAS = 6
    tentativas = 0
    Acertos = []
    palavras = []

    with open('Wordle/WordList.txt', 'r') as arquivo:
            palavrasAcento = arquivo.read().split()
            palavras = [unidecode(palavra) for palavra in palavrasAcento]

    palavraJogo = choice(palavras)
    console = Console()
    while tentativas < MAX_TENTATIVAS:
        palavraDigitada = input(DIGITAR_PALAVRA)    
        if validaPalavra(palavraDigitada):
            continue
        Acertos += verificaLetra(palavraDigitada, palavraJogo)
        console.print(''.join(Acertos))
        Acertos.append('\n')
        tentativas += 1

        if verificaVitoria(palavraDigitada, palavraJogo):
            break
        elif tentativas == MAX_TENTATIVAS:
            print(f'\n\nQue pena! Você não conseguiu descobrir a palavra secreta')
            break    

if __name__ == '__main__':
    print("\t ----> TERMO <----")
    start()
