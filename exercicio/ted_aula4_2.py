# Problema: As maçãs custam R$ 1,30 cada,
# se forem compradas menos de uma dúzia, 
# e R$ 1,00 se forem compradas pelo menos
# 12. Escreva um programa que leia o número
# de maçãs compradas, calcule e escreva
# o custo total da compra.

print("-="*20)
print("Comprando Maçãs")
print('=-'*20)
print("Vendo maçãs a R$1,30, mas se comprar a dúzia sai por R$1,00")

macas = int(input("Quantas maçãs, meu consagrado? "))
print("**"*20)

if macas < 1:
    print('Então viesse fazer aqui, meu chapa?')
else:
    print(f'Com {macas} maçã(s),')
    if macas < 12:
        soma = macas * 1.30
        print(f'Com menos de 12, você leva tudo por: R${soma:.2f}')
    else:
        soma = macas
        print(f'Com mais de 12, você leva tudo por: R${soma:.2f}')
        print("Você é um cliente fiel, meu irmão.")

print("Por aqui fico eu, até a próxima!")
