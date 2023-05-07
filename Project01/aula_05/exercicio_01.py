
def borda(frase):
    tam = len(frase)
    if tam:
        print('+','-' * tam,'+')
        print('|',frase,'|')
        print('+', '-' * tam, '+')

borda('Óla, World')
borda('Lógica de Programação de Algoritimos')