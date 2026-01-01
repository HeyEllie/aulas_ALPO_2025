linha = 0
coluna = 0 


mat = [['']*5, ['']*5, ['']*5, ['']*5, ['']*5]
print("A)")
for linha in range (0,5,1):
    for coluna in range (0,5,1):
        mat[linha][coluna] = '*'
        print(f" {mat[linha][coluna]} ", end='')
    print()
print()


mat = [[' ']*5, [' ']*5, [' ']*5, [' ']*5, [' ']*5]
print("B)")
for linha in range (0,5,1):
    for coluna in range (0,5,1):
        if (linha == 0) or ( coluna == 0) or (linha == 4) or (coluna == 4):
            mat[linha][coluna] = '*'
        print(f" {mat[linha][coluna]} ", end='')
    print()
print()


mat = [['']*5, ['']*5, ['']*5, ['']*5, ['']*5]
print("C)")
for linha in range (0,5,1):
    for coluna in range (0,5,1):
        if linha >= coluna:
            mat[linha][coluna] = '*'

for linha in range(0,5,1):
    for coluna in range(0,5,1):
        print(f" {mat[linha][coluna]} ", end='')
    print()
print()




