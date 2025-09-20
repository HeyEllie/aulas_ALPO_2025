'''
dados 3 valores lado1, 2 e 3. Estes valores repesentam lados de um triãngulo
com base nisso verificar:
a) se podem ser valores dos lados formam um tra
b) se formar um tria, determine qual:
equilátero, isósceles ou escaleno
'''

l1 = 0.0
l2 = 0.0
l3 = 0.0

l1 = float(input("Informe o valor do lado um: "))
l2 = float(input("Informe o valor do lado dois: "))
l3 = float(input("Informe o valor do lado três: "))

if (l1 + l2 > l3) and (l2 + l3 > l1) and ( l1 + l3 > l2):
    if (l1 == l2) or ( l2 == l3) or ( l1 == l3):
        print("O triângulo é isósceles!!!")
    else:
        if (l1 == l2) and ( l2 == l3) and ( l1 == l3):
                print("O triângulo é equilátero!!!")
        else:
            if (l1 != l2) and ( l2 != l3) and ( l1 != l3):
                print("O triângulo é escaleno!!!")
        

else:
    print("Os valores não formam um triângulo!!!")


