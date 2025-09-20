'''
Faça u mprograma que mostre até a do 15 resolvida. OBS: para mostrar a deve ser utilizado o comando for
ob.: o comando for pode ser utilizado no máximo 2 vezes
'''
n = 0

for i in range(1, 16,1):
    print(f"****Tabuada do {i}")
    for cont in range(1, 11,1):
        print(f"{i} X {cont} = {i * cont}")