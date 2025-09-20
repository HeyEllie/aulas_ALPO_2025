''' Faça um algoritmo que peça o nome do usuário e sua idade. Se a idade foi maior ou igual que 18 anos, escreva: Fulano, você já pode obter sua CNH;
# Se a idade for menor que 18 anos, escreva: Fulano, você não pode obter sua CNH.
'''

#variaveis
n = ""
idade = 0.0

#programa
n = input("Informe o nome do usuário: ")
idade = float(input("Informe a idade do usuário: "))

if (idade >= 18 ):
    print(f"{n}, você já pode obter sua CNH!")
else: 
    print(f"{n}, você ainda não pode obter sua CNH!")