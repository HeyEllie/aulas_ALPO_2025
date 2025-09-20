'''
costruir um algo que leia a altura de 20 pessoas. O algo dev calcular e imprimir quantas pessoas possuem altura 
maior que 2 metros e a média de todas as 20 alturas
'''
al = 0.0
al_s = 0.0
al_2m =0.0
al_m = 0.0

for contador in range(1,21,1):
    al = float(input(f"Informe a altura {contador}: "))
    al_s += al

    if (al > 2):
        al_2m += 1

al_m = al_s / 20

print(F"Existem {al_2m} pessoas maiores que 2 metros e a média é: {al_m}")
