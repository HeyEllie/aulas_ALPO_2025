'''
um determinado material radioativo perde netade de sua massa a cada 60 segundos. Dada a massa inicial, em gramas, fazer um programa que determine o tempo
necessário para que esa massa se torne menor que 0,5 gramas. Escreva a massa inicial, a massa final e o tmepo calculado em segundos
'''
massa_final = 0
tempo_gasto = 0
massa_inicial = 0 

massa_inicial = float(input("Informe a massa do material radiotivo: "))
massa_final = massa_inicial
while massa_final >= 0.5:
    massa_final = massa_final/2
    tempo_gasto += 60


    

print(f"A massa inicial foi {massa_inicial}")
print(f"A massa final foi {massa_final}")
print(f"O tempo gasto foi { tempo_gasto} s")
