'''
faça um  programa que receba o código correpondente ao cargo de um funcionário e seu salario atual e mostre o cargo, o valor do aumento e seu novo salario .
 Os cargos estáo na tabela a segur
codigo     cargo            aumento
1          escriturário    40%
2           ecretáia   35%
3        caixa            20%
4         gerente         10%
5        diretor          0%
obs: caso seja digitado um código que não está na lista, deve ser mostrado a mensagem código invalido
'''

c = 0
s = 0.0
cargo = ""

c = int(input("Informe o seu código: "))
s = float(input("Informe o valor do seu salário: "))

a1 = ( s *  40) / 100
a2 = ( s * 35) / 100
a3 = ( s * 20) / 100
a4 = ( s * 10) / 100
a5 = ( s * 0) / 100


if c == 1:
    print(f"Escriturário, se aumento é de {a1}")
else:
    if c == 2:
        print(f"Secretário, seu aumento é de {a2} ")    
    else: 
        if c == 3:
            print(f"Caixa, seu aumento é de {a3}")
        else:
            if c == 4:
                print(f"Gerente, seu aumento é de {a4}")
            else:
                if c == 5:
                    print(f"Diretor, seu aumento é de {a5}")
                else:
                    if c != 1 and 2 and 3 and 4 and 5:
                        print(f"O código não está na lista!!!")




