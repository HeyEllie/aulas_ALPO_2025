''' 
'' que leia uma matriz 3 x 6 com valores reais e depois resolva o intens abaixo: 
1 - imprima a matriz orginal;
2 - imprima a soma  de todos os elementos das colunas ímpares;
3 - '' a média aritmética dos leementos da segunda e quarta colunas;
4 - substitua os valores da sexta coluna pela soma dos valores das colunas 1 e 2;
5 - imprima a matriz modificada
'''

linha = 0
coluna = 0
mat = [[0]*6, [0]*6, [0]*6]
soma = 0
soma1 = 0
media = 0
soma2 = 0 


for linha in range(0,3,1):
    for coluna in range(0,6,1):
        mat[linha][coluna] = int(input(f"Informe o número para a position {linha} {coluna}: "))
        if (coluna == 1) or (coluna == 3) or (coluna == 5):
            soma += mat[linha][coluna]
        if (coluna == 1) or (coluna == 3):
            soma1 += mat[linha][coluna]

print("----- Matriz 3 x 6 -----")
for linha in range(0, 3,1):
    for coluna in range(0,6,1):
        print(f"[{mat[linha][coluna]}]", end='')
    print()
print()

for linha in range(0, 3,1):
    for coluna in range(0,6,1):
        if coluna == 5:
            mat[linha][coluna] = mat[linha][0] + mat[linha][1]

media = soma1 / 6

print("----- Matriz 3 x 6  mudada -----")
for linha in range(0, 3,1):
    for coluna in range(0,6,1):
        print(f"[{mat[linha][coluna]}]", end='')
    print()
print()

print("-----------------")
print(f"Soma colunas ímpares {soma}")
print(f"Média {media} ")

        
