'''
'' Faça um progarma que leia uma matriz 5x5 de inteiros e um vetor de 5 posições também de inteiros. O algoritmo deve ler os valores nacessários para incializar a matriz e, feito isto, armazenar
em cada coluna do vetor a soma dos elementos da coluna correspondente da matriz. Ao final, mostrar a matriz e também o vetor
'''

cont = 0
cont1 = 0
linha = 0
coluna = 0 
mat = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]
vet = [0] * 5

for linha in range(0,5,1):
    for coluna in range(0,5,1):
        mat[linha][coluna] = int(input(f"Informe o valor da matriz posição {linha}{coluna}: "))
        

for linha in range(0,5,1):
    for coluna in range(0,5,1):
        vet[coluna] +=  mat[linha][coluna]



for linha in range(0,5,1):
    for coluna in range(0,5,1):
        print(f"[{mat[linha][coluna]}]", end='')
    print()
print()
for cont in range (0,5,1):
    print(f"[{vet[cont]}]", end='')
