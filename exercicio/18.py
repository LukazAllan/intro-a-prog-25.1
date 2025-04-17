# Crie um programa que peça ao usuário para inserir 
# várias notas de um aluno e calcule a média. Utilize 
# um loop para continuar pedindo notas até que o 
# usuário digite um valor específico para encerrar a 
# entrada (por exemplo, -1).

materias = ["REDES", "ARQCOM", "LOGMAT", "IHC", "INTPRO"]
notas = []

print("-="*20)
print("Calculadora de Notas")
aluno = input("Qual o seu Nome? ")

print("=-"*20)
print(f"Olá, {aluno}. Diga-me suas notas:")
print("*"*40)
for materia in materias:
    nota1 = float(input(f"Nota 1 de {materia}: "))
    nota2 = float(input(f"Nota 2 de {materia}: "))
    notas.append((nota1, nota2))
    print("*="*20)

print("~~"*20)
print("~~"*20)
print(f"Você, {aluno}, manteve as seguintes médias:")
for materia in range(len(materias)):
    media_parcial = (notas[materia][0] + notas[materia][1]) / 2
    print(f"{materias[materia]}: {notas[materia][0]}, {notas[materia][1]}, média = {media_parcial}", end=" ")
    if media_parcial > 7:
        print('o qual você passou.')

    else:
        print('o qual você reprovou.')
