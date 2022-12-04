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
            acertos += lugarCorreto(letra)
        elif letra in palavraJogo:
            acertos += letraCorreta(letra)
        else:
            acertos += letraIncorreta(letra)
    return acertos
