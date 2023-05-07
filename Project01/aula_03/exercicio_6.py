nome_aluno = input("Digite seu nome: ")
nota_matematica = float(input("Digite sua nota: "))
nota_portugues = float(input("Digite sua nota: "))
nota_ingles = float(input("Digite sua nota: "))
media_aluno = (nota_matematica + nota_ingles + nota_portugues) / 3
if media_aluno >= 7.0:
    print(f"Parabéns  {nome_aluno} sua média foi de {media_aluno} e está aprovado :) ")
else:
    print(f"Óla {nome_aluno} sua média foi de {media_aluno} infelizmente você está de recuperação !!!!!")