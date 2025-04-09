# Ler as notas da 1a. e 2a. avaliações de um aluno. 
# Calcular a média aritmética simples e escrever uma 
# mensagem que diga se o aluno foi ou não aprovado 
# (considerar que nota igual ou maior a 6 o aluno 
# é aprovado). Escrever também o resultado da média 
# calculada.
print('-='*20)
print('Sua Vida Acadêmica')
print("=-"*20)

nota1 = float(input('Aluno, digite sua primeira nota: '))
print("**"*20)
nota2 = float(input('Agora, sua segunda nota: '))
print('**'*20)

media = (nota1 + nota2) / 2
print(f"Sua média é {media}")
if media >= 6: 
    print('Resultado: Aprovado')
else:
    print('Resultado: Reprovado')
print('**'*20)
