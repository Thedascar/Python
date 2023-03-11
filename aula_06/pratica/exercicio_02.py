palavras = ('Python','Java','Java Script','GoLang','Kotlin','Csharp')


for palavra in palavras:
    print(f'\nPalavras: {palavra} . Vogais: ',end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}',end=' ')