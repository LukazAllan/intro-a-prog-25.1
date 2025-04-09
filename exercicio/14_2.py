contador = 1000
while contador <= 2000:
    if contador % 11 == 5:
        print(f'O {contador}, obteve resto 5 para divisao por 11.')
    else:
        print(f'O {contador}, não.')
    contador += 1
print('fim')
