''' '' que leia uma matriz 3x5 de int, preencha a matriz e depois:
1 - mostre a matriz original;
2 - mostre a quantidade de números pares;
3 - mostre a quantidade de números ímapres.
 '''

linha = 0
coluna = 0 
mat = [[0]*5, [0]*5, [0]*5]
par = 0
impar = 0 

for linha in range (0,3,1):
    for coluna in range (0,5,1):
        mat[linha][coluna] = int(input(f"Informe um número para a posição {linha} {coluna}: "))

for linha in range (0,3,1):
    for coluna in range (0,5,1):
        if mat[linha][coluna] % 2 == 0:
            par += 1
        else:
            impar += 1

for linha in range(0,3,1):
    for coluna in range(0,5,1):
        print(f"[{mat[linha][coluna]}]", end='')
    print()
print()

print()
print(f"Pares {par} e ímpares {impar}")