''' '' que leia uma matA se tamanho 4 x 6 e uma matriz matB de tamanho 4 x 6 e criar:
a? uma amtriz matsoma que seja a soma de matA e matB
B) uma matriz matA, matB, matsoma, matdiferenca após todo álculo estar concluído da forma demonstarda abaixo "uma do lado da outra"'''

linha = 0 
coluna = 0 
matA = [[0] * 6, [0] * 6, [0] * 6, [0] * 6]
matB = [[0] * 6, [0] * 6, [0] * 6, [0] * 6]
matsoma =[[0] * 6, [0] * 6, [0] * 6, [0] * 6]
matdiferenca = [[0] * 6, [0] * 6, [0] * 6, [0] * 6]


for linha in range (0, 4, 1):
    for coluna in range (0,6,1):
        matA[linha][coluna] = int(input(f"Informe o número para a posição {linha} {coluna}: "))
print()
    
for linha in range (0, 4, 1):
    for coluna in range (0,6,1):
        matB[linha][coluna] = int(input(f"Informe o número para a posição {linha} {coluna}: "))
print()


for linha in range (0, 4, 1):
    for coluna in range (0,6,1):
        matsoma[linha][coluna] = (matA[linha][coluna]) + (matB[linha][coluna])
print()

for linha in range (0, 4, 1):
    for coluna in range (0,6,1):
        matdiferenca[linha][coluna] = (matA[linha][coluna]) - (matB[linha][coluna])
print()

print(" Matriz  A          ", end='')
print(" Matriz  B             ", end='')
print(" Matriz  soma     ", end='')
print(" Matriz  subtração  ")


for linha in range(0,4,1):
    for coluna in range(0,6,1):
        print(f"[{matA[linha][coluna]}]" , end='')
    print("   ", end='')
    for coluna in range(0,6,1):
        print(f"[{matB[linha][coluna]}]" , end='')
    print("   ", end='')
    for coluna in range(0,6,1):
        print(f"[{matsoma[linha][coluna]}]", end='')
    print("   ", end='')
    for coluna in range(0,6,1):
        print(f"[{matdiferenca[linha][coluna]}]", end='')
    print()
