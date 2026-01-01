'''  '' matriz 4 x 3 real e imprima a soma dos elementos de uma  linha L fornecida pelo user'''

linha = 0
coluna = 0 
mat = [[0]*3, [0]*3, [0]*3, [0]*3]
soma = 0

for linha in range(0,4,1):
    for coluna in range(0,3,1):
        mat[linha][coluna] = int(input(f"Informe um número para a posição {linha} {coluna}: "))


for linha in range(0,4,1):
    for coluna in range(0,3,1):
        print(f"[{mat[linha][coluna]}]", end='')
    print()
print()

pergunta = int(input("Qual linha você deseja fazer a soma? "))
if ((pergunta >= 0) and (pergunta <= 3)):
    for coluna in range(0,3,1):
        soma += mat[pergunta][coluna]
else:
    print(f"A linha {pergunta} deve estar entre 0 e 3")

print(F"{soma}")



