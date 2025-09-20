'''
escreva um algoritmo pra mostrar na tela os valores do 1 até max, onde max é um número definido pelo usuário
'''
max = 0

n = int(input("Informe o maximo de 1: "))
for max in range(1,n + 1,1):
    print(f"{max}")
