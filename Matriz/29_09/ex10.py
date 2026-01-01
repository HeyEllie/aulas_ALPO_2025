''' '' que leia uma matriz 5x5 de inteiros. Após ler todos os elementos da matriz, calcule a média de todos
os elementos e verifique quantos elementos são iguais ou superior a média calculada. Ao final, deve ser mostrado a matriz original, o valor de média e a quantidade de elementos
que são igauis ou superior a media
'''
elementos = 0
media = 0
soma = 0
linha = 0
coluna = 0
mat = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]

for linha in range(0,5,1):
    for coluna in range(0,5,1):
        mat[linha][coluna] = int(input(f"Informe o número para a position {linha} {coluna}: "))
        soma += mat[linha][coluna]
        

media = soma / 25

for linha in range(0,5,1):
    for coluna in range(0,5,1):
        if (mat[linha][coluna]) >= media:
            elementos += 1


print("----- Matriz 5 x 5 -----")
for linha in range(0, 5,1):
    for coluna in range(0,5,1):
        print(f"[{mat[linha][coluna]}]", end='')
    print()

print("-----------------")
print(f"Média {media}")
print(f"Elementos iguais ou superiores a média {elementos}")