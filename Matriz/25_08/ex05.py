'''
 '' que leia uma matriz 2x3 real e depois imprimaa matriz original e depois gere e imprima sua matriz transposta (3x2 equivalente)
'''
linha= 0
coluna = 0
mat = [[0]*3, [0]*3]
mat_trans = [[0]*3, [0]*3, [0]*3]

for linha in range(0, 2,1):
    for coluna in range(0,3,1):
        mat[linha][coluna] = int(input(f"Informe um número para a posição {linha} {coluna}: "))

print("--------Matriz orginal----------")
for linha in range(0, 2,1):
    for coluna in range(0,3,1):
        print(f"[{mat[linha][coluna]}]", end='')
    print()


for linha in range(0,3,1):
    for coluna in range(0,2,1):
        mat_trans[linha][coluna] =  mat[coluna][linha]
        
print("------------Matriz transposta----------")
for linha in range(0, 3,1):
    for coluna in range(0,2,1):
        print(f"[{mat_trans[linha][coluna]}]", end='')
    print()
