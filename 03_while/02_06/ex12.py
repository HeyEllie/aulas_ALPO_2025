'''
escreva um algoritmo que solicita ao usuário para digitar um número int positivo, e mostre-o por extenso. Este núemro deverá variar entre 1 e 5. 
Se o user introduzir um num que não pertence a este intervalo, mostre a frase "número inválido''.
 O programa deve ficar executando até que o usuário digite 0 
 '''



n = 1
while n != 0:
    n = int(input("Informe um número inteiro positivo: "))
    if n == 1:
        print("Um")
    else:
        if n == 2:
            print("Dois")
        else:
            if n == 3:
                print("Três")
            else:
                if n == 4:
                    print("Quatro")
                else:
                    if n == 5:
                        print("Cinco")
                    else:
                        if n < 0:
                            print("Informe um número inteiro positivo!!")
                        else:
                            if n != 0:
                                print("Código inválido!!")
                            


