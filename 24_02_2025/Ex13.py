'''
Faça um programa que receba uma medida em pés.
Faça as conversões a seguir e mostre os resultados.
  a) polegadas
  b) jardas
  c) milhas
Sabe-se que:
  1 pé = 12 polegadas
  1 jarda = 3 pés
  1 milha = 1760 jardas
  '''

#variaveis
pés = 0.0
polegadas = 0.0
jardas = 0.0
milhas = 0.0

#programa
pés = float(input("Informe a medida de pés: "))

polegadas = 12 * pés
jardas = pés / 3 
milhas =  jardas / 1760

print(f"A medida em polegadas é: {polegadas}, em jardas: {jardas}, em milhas: {milhas} e em pés: {pés}")