#Anna Sthéfany e Helena Ferreira

linha = 0
coluna = 0 
mat1 = [[0]*40, [0]*40, [0]*40] # ra, cpf, código
mat2= [[0.0]*40, [0.0]*40,[0.0]*40,[0.0]*40,[0.0]*40,] # notas dos alunos 
resposta = "s"


'''for linha in range(0,5,1):'''
for linha in range(0,3,1): #aqui nesse for vai pedir as informações com ra, cpf e código e guardar na matriz 1 e relacionar os código com a matriz  2
    mat1[linha][0] = int(input("Informe o RA do aluno: "))
    mat1[linha][1] = int(input("Informe o CPF do aluno: "))
    mat1[linha][2] = int(input("Informe o código do aluno: "))

    mat2[linha][0] = mat1[linha][2]
    mat2[linha][1] = int(input(f"Informe a nota 1 do aluno {mat1[linha][2]}: "))
    mat2[linha][2] = int(input(f"Informe a nota 2 do aluno {mat1[linha][2]}: "))
    mat2[linha][3] = int(input(f"Informe a nota 3 do aluno {mat1[linha][2]}: "))
    mat2[linha][4] = int(input(f"Informe a nota 4 do aluno {mat1[linha][2]}: "))


    soma = sum(mat2[linha])  # soma as notas das medias
    media = soma / 4 
        #if coluna == 5:
    mat2[linha][5] = media

while resposta != "N"  : # enquanto resposta diferente de n, ou seja, não
    consulta = int(input("Informe o tipo de consulta.\n1-RA; 2-CPF; 3-Código: "))
    if consulta == 1: # se for igual a ra mostra suas devidas informações
        ra = int(input("Informe o RA: "))
        for linha in range(0,3,1):
            if ra == mat1[linha][0]:
                for coluna in range(1,40,1):
                    print(f"As notas são\n [{mat2[linha][coluna]}]", end='')
                print()            
                print(f"Média: {mat2[linha][5]}")   

                if media >= 6:
                    print("Aprovado")
                else:
                    if media >= 4 and media <6:
                        print("Recuperação")
                    else:
                        if media < 4:
                            print("Reprovado")
            else:
                print("O RA não foi encontrado")          
    else:
        if consulta == 2: # se for igual a cpf mostra suas devidas informações
            cpf = input("Informe o CPF: ")
            for linha in range(0,3,1):
                if cpf == mat1[linha][1]:
                    for coluna in range(1,40,1):
                        print(f"As notas são\n [{mat2[linha][coluna]}]", end='')
                    print()
                    print(f"Média: {mat2[linha][5]}")
                    if media >= 6:
                        print("Aprovado")
                    else:
                        if media >= 4 and media <6:
                            print("Recuperação")
                        else:
                            if media < 4:
                                print("Reprovado")
                else:
                    print("O CPF não foi encontrado") 
        else:
            if consulta == 3: # se for igual a código mostra suas devidas informações
                codigo = input("Informe o Código: ")
                for linha in range(0,3,1):
                    if codigo == mat1[linha][2]:
                        for coluna in range(1,40,1):
                            print(f"As notas são\n [{mat2[linha][coluna]}]", end='')
                        print()
                        print(f"Média: {mat2[linha][5]}")
                        if media >= 6:
                            print("Aprovado")
                        else:
                            if media >= 4 and media <6:
                                print("Recuperação")
                            else:
                                if media < 4:
                                        print("Reprovado")
                    else:
                        print("O Código não foi encontrado") 
            else:
                print("Tipo de consulta inválida! ")# se não for nada, consulta inválida. Pede de novo

    resposta = input("Deseja fazer uma nova pesquisa?\nS-sim; N-não: ").upper()

            


       

