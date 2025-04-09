print("+="*20)
print("Loja Messi")
print("=+"*20)

print("Olá cliente, quanto você comprou na")
print("nossa humilde loja? Diga-nos e podemos")
print("dar (lá ele) um desconto.")
print("**"*20)

valor = float(input("Valor da compra: R$ "))
print("**"*20)
print("Pelos meus cálculos................")

if valor < 50:
    print("Com um valor menor que 50, fica difícil.")
elif 50 <= valor < 100:
    print("Consegui um descontinho de 5% pra você.")
else:
    print("Consegui um desconto de 10%, meu chegado.")

print("Até a próxima.... Loja Messi.")
