''' ''que leia os elementos de uma matriz inteira 5x5 e escreva os elementos da diagonal  principal'''

linha = 0
mat = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]
coluna = 0

for linha in range(0,5,1):
    for coluna in range(0,5,1):
        mat[linha][coluna] = int(input(f"Informe um números para a posição {linha} {coluna}: "))

for linha in range(0,5,1):
    for coluna in range(0,5,1):
        if linha == coluna:
            print(f"[{mat[linha][coluna]}]", end='')
        else:
            print(" ", end='')
        print()