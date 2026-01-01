'''  
  '' que leia e armazene valores int em uma matriz 3 x 3. Após entrada, identifique o maior valor presente na mat.
  feito isso, criar uma mat de resposta 3x3 , na qual cada ekemento será o valor correspondente da primeira matriz multiplicado
  pelo maior valore encontrado. Ao final mostrar as duas matriezs
'''
maior_valor = 0
linha = 0
coluna = 0
mat = [[0]*3, [0]*3, [0]*3]
mat1 = [[0]*3, [0]*3, [0]*3]

for linha in range(0,3,1):
    for coluna in range(0,3,1):
        mat[linha][coluna] = int(input(f"Informe o número para a position {linha} {coluna}: "))
        if mat[linha][coluna] > maior_valor:
            maior_valor = mat[linha][coluna]

for linha in range(0,3,1):
    for coluna in range(0,3,1):
        mat1[linha][coluna] = mat[linha][coluna] * maior_valor

print("----- Matriz 3 x 3  original -----")
for linha in range(0,3,1):
    for coluna in range(0,3,1):
        print(f"[{mat[linha][coluna]}]", end='')
    print()
print()

print("----- Matriz 3 x 3  multiplicada por 2 -----")
for linha in range(0, 3,1):
    for coluna in range(0,3,1):
        print(f"[{mat1[linha][coluna]}]", end='')
    print()
print()
