''' 1kg - 1000g
Pedro comprou um saco de ração em quilos. Pedro possui dois gatos para os quais fornece a quantidade de ração em gramas. 
Faça um programa que recebe o peso do saco de ração e a quantidade de ração fornecida para cada gato (a quantidade para cada gato de ser obtida de forma individual).
Calcule e mostre quanto restará de ração em quilos no saco após cinco dias.
'''

#variaveis
racao = 0.0
gato1 = 0.0
gato2 = 0.0
racao_final = 0.0
quilos = 0.0

#programa
racao = float(input("Informe o peso do saco de ração: "))
gato1 = float(input("Informe a quantidade de ração fornecida para o primeiro gato: "))
gato2 = float(input("Informe a quantidade de ração fornecida para o segundo gato: "))

quilos = ((gato1 + gato2) / 1000 ) * 5
racao_final = racao - quilos

print(f"O restante de ração que sobrou no saco é {racao_final}kg")

