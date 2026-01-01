''' uma esolca esta realizando matrículas para um curso aberto á comunidade, com limite de 20 vagas. Assumindo que os alunos sã ocadastrados por computador, escreva um algo. que 
- leia a idade e o sexo do aluno;
-informe que a turma está lotada, quando o num. de inscritos atingir a quantidade de vagas;
-mostre a idade média dos candidatos , esta funcionalidade deve ser desenvolvida em uma funçã o;
- mostre a quant. de mulheres inscritas, esta funcionalidade deve ser desenvolvida em uma função;
-mostre os candidatos (homans e mulheres) maiores de idade, esta funcionalidade deve ser desenvolvida em uma função;
-deve ser desenvolvida uma função para imprimir os resuiltados da tela
 '''

veti = [0]*20
vets = [" "]*20
media = 0.0
quant_w = 0
quant_total = 0
soma = 0 

def idade_m(i):
    global media
    media = i / 20

def quant_women(q):
    global quant_w
    if q == "F":
        quant_w =+ 1


def maior_i(m):
    global quant_total
    if m >= 18:
        quant_total =+ 1

def print():
    print("A turma está lotada !!")
    print(f"A média de idades foi de {media}")
    print(f"A quantidade de mulheres inscritas foi de {quant_w}")
    print(f"A quantidade de candidatos que sã omaiores de idade foi de {quant_total}")

for cont in range(0,20,1):
    veti[cont] = int(input(f"Informe a idade do aluno para a posição {cont}: "))
    vets[cont] = input(f"Informe o sexo do(a) aluno(a) para a posição {cont}.\n F para feminino; M para masculino: ").upper()
    soma += veti[cont]
    quant_women(vets[cont])
    maior_i(veti[cont])

idade_m(soma)

print()