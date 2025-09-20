'''
'' que leia uma amtriz 5x5 e gere uma matriz em que cada elemento é o cubo do elemento respectivo  na matriz orginal. Imprima a matriz orginal e depois a matriz final
** potenciação
'''
linha = 0
coluna = 0
mat = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]
mat2 = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]

for linha in range(0,5,1):
    for coluna in range(0,5,1):
        mat[linha][coluna] = int(input(f"Informe o número para a posição {linha} {coluna}: "))
        
print("---------matriz original-------")
for linha in range(0, 5,1):
    for coluna in range(0,5,1):
        print(f"[{mat[linha][coluna]}]", end='')
    print()

for linha in range(0,5,1):
    for coluna in range(0,5,1):
        mat2[linha][coluna] = (mat[linha][coluna])**3

print("-------matriz com o cubo dos respectivos números sa original---------")
for linha in range(0,5,1):
    for coluna in range(0,5,1):
        print(f"[{mat2[linha][coluna]}]", end='')
    print()