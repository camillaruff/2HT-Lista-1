#Lista 1 - quest1


#SOLICITACAO DE INFORMACAO
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

#CALCULO MEDIA
media = (nota1 + nota2 + nota3 + nota4) / 4

#VERIFICACAO
if media < 4:
    situacao = "Em processo de Aprendizagem (Reprovado)"
elif media < 8:
    situacao = "Recuperação"
else:
    situacao = "Aprovado"

#EXIBICAO FINAL
print("Situação do aluno:", situacao)
