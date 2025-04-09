#Faça um algoritmo para ler: quantidade atual em estoque, 
#quantidade máxima em estoque e quantidade mínima em 
#estoque de um produto. Calcula  , end='escrever a quantidade 
#média ((quantidade média = quantidade máxima + quantidade mínima)/2). 
#Se a quantidade em estoque for maior ou igual a quantidade 
#média, escrever a mensagem 'Não efetuar compra', senão 
#escrever a mensagem 'Efetuar compra'.

print('-='*20)
print('Empresa legal')
print('-='*20)

qt_atual = float(input('Digite a quantidade atual: '))
qt_max = float(input('Digite a quantidade máxima: '))
qt_min = float(input('Digite a quantidade mínima: '))
print('**'*20)
qt_med = ( qt_max + qt_min ) / 2
print('Este programa entende que ', end='')
if qt_atual >= qt_med:
    print('não é necessário a compra... Não efetuar compra')
else:
    print('é necessário esta compra... Efetuar compra')
