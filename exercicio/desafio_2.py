f = open("tabuada.txt")

fator1 = int(input("Digite um número inteiro meu nobre: "))
f.write(f'Tabuada do {fator1}\n')
for fator2 in range(1, 11, 1):
    f.write(f'{fator1} x {fator2} == {fator1 * fator2}\n')
f.write('-='*30)
f.close()
 
