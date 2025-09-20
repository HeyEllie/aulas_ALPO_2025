'''
Receba um salário de um funcionáro, calcule e mostre o novo salário desse funcionário, acrescido de bonificação e de auxílio escola
salario                          bonificação
até r$ 500,00                      5%
entre r$ 500,00 e R$ 1200,00        12%
acima de R$ 1200,00                 0%

salário                         auxílio escola
até R$ 600,0 0                 150,00
mais que R$ 600,00            R$ 100,00
'''

sal = 0.0
n_sal = 0.0


sal = float(input("Informe o salário do funcionário: "))

if sal < 500:
    bo = (sal * (5 / 100)) 
else:
    if sal >= 500 and sal <= 1200:
        bo = (sal * (12 / 100)) 
    else:
        if sal > 1200:
            bo = 0


if sal <= 600:
    aux = sal + 150
else:
    aux = sal + 100

print(f"O novo salário é {bo + aux}")

