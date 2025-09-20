'''
 '' que receba de 10 alunos suas quatro notas. Após recebe estes dados deve ser calculado a média aritmética das notas do aluno e armazenada na própria
matriz. Ao final de tudo imprimir a listagem contendo todas as notas e também a média do aluno
'''
linha = 0
coluna = 0 
mat = [[0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5,]

for linha in range(0,10,1):
    for coluna in range(0,5,1):
        mat[linha][coluna] = float(input(f"Informe a nota do aluno para a position {linha} {coluna}: "))
        soma = sum(mat[linha])
        media = soma / 4 
        if coluna == 4:
            mat[linha][coluna] = media


for linha in range(0,10,1):
    for coluna in range(0,5,1):
        print(f"[{mat[linha][coluna]}]", end='')
    print()
    print(f"Média: {mat[linha][4]}")

print(f"Média: {mat[linha][4]}")