# Implemente um jogo onde o computador escolhe 
# um número aleatório entre 1 e 100, e o 
# usuário tenta adivinhar. Utilize um loop 
# para permitir que o usuário faça várias 
# tentativas, fornecendo dicas (maior ou 
# menor) a cada tentativa.
#from os import system as sys
from random import randint as rd

numero = rd(0, 100)
run = True
for x in range(5):
    tentativa = int(input("QUE NÚMERO PENSEI? "))
    if tentativa == numero:
        print('PARABÉNS, MEU CONSAGRADO.')
        break
    else:
        print("VOCÊ ERROU.", end=" ")
        if tentativa > numero:
            print('TENTE PRA BAIXO.')
        else:
            print('VOCÊ ME SUBESTIMA, TENTE PRA CIMA!')
print("SE VOCE DESCOBRIU, PARABÉNS. CASO CONTRÁRIO, SE LAMENTE EM SUA INSIGNIFICÂNCIA.")
