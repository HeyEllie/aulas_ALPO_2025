'''
'' que solicite a resposta e x pessoas sobre a preferencia do produto. Esta pessoa deverá responder 1 se gosotu do primeiro produto ou 2 se fosotu do segundo ou 3para quem
gosotu do terceiro. Ao final deve serimpresso na tela a quanyidade de pessoas que gostaram do produto 1, do 2 e do3


'''

x = 0
x1 = 0
p1 = 0
p2 = 0
p3 = 0

x = int(input("Informe a quantidade de pessoas: "))

for i in range(1, x+1, 1):
    x1 = int(input(f"Informe o que a {i}° pessoa gostou: "))
    if ((x1 < 1) or (x1 > 3)):
        print("Produto inválido!!!")
    if (x1 == 1):
        p1 += 1
    else:
        if (x1 == 2):
            p2 += 1
        else:
            if (x1 == 3):
                p3 += 1

print(f"A quantidade de pessoas que gostaram do 1° produto foi: {p1}, que gostaram do 2°: {p2} e que gostaram do p3: {p3}")
