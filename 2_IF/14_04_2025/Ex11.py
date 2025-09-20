'''
 solicite o nome e a idade de um nadador e  imprima na tela o seu nome, a sua idade e em qual categoria ele está
 idade      catgoria
 5 a 7      infantil A
 8 a 11         '' B
 12 a 13    juvenil A
 14 a 17       '' B
 18 a >      adulto
 caso seja digitado uma idade fora das classes acima, informar que o nadador não possui uma categoria válida
'''

n = ""
i = 0

n = input("Informe o seu nome: ")
i = int(input("Informe a sua idade: "))


if i >= 5 and i <= 7:
    print(f"{n}, {i} anos, sua categoria é Infantil A")
else:
    if i >= 8 and i <=11:
        print(f"{n}, {i} anos, sua categoria é Infantil B")
    else:
        if i == 12 and i  == 13:
            print(f"{n}, {i} anos, sua categoria é Juvenil A")
        else:
            if i >= 14 and i <=17:
                print(f"{n}, {i} anos, sua categoria é Juvenil B") 
            else:
                if i >= 18:
                    print(f"{n}, {i} anos, sua categoria é Adulto")
                else:
                    print(f"{n}, categoria inválida!!!")



