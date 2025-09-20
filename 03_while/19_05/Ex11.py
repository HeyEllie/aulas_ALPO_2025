nu = "S"

while nu != "N":
    n = int(input("Informe um número: "))
    if n < 0:
        print("O número é negativo!!")
        nu = input("Deseja informar mais um número? S - sim; N - não: ") .upper()
    else:
        if n > 0:
            print("O número é positivo!!")
            nu = input("Deseja informar mais um número? S - sim; N - não: ") .upper()
        else:
            if n == 0:
                print("O número é zero!!")
                nu = input("Deseja informar mais um número? S - sim; N - não: ") .upper()

