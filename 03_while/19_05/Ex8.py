p = 1
p1 =0
p2 = 0
p3 = 0
p4 = 0


while p != 0:
    print("Informe a preferência do produto:")
    print("1 - gostou do primeiro produto; 2 - gostou do segundo; 3 - gostou do terceiro; 0 - para finalizar")
    p = int(input(f"-->: "))
    if ((p >= 1) and (p <= 3)):
        if p == 1:
            p1 +=1
        else:
            if p == 2:
                p2 += 1
            else:
                if p == 3:
                    p3 += 1
    else:
        if (p != 0):
            print("Produto inválido")

print(f"A quantidade de pessoas que gostaram do 1° produto foi: {p1}, que gostaram do 2°: {p2} e que gostaram do 3°: {p3}")

