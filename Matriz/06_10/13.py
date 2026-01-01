''' .. que leia uma matriz de 5x 5 do tipo int. Deve ser informado somente os elementos da diagonal principal.
Após a entrada, prencher as células acima da diagonal principal com 1 e as abaixo  com 2.'''

linha = 0
coluna = 0
mat = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]


for linha in range(0,5,1):
    for coluna in range(0,5,1):
        if linha == coluna:
            mat[linha][coluna] = int(input(f"Informe o número para {linha} {coluna}: "))
        
for linha in range (0,5,1):
    for coluna in range (0,5,1):
        if linha > coluna: 
            mat[linha][coluna] = 2
        else:
            if linha < coluna: 
                mat[linha][coluna] = 1

for linha in range(0,5,1):
    for coluna in range(0,5,1):
        print(f"[{mat[linha][coluna]}]", end='')
    print()
print()
