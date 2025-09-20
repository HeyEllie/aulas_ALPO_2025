'''
Um trabalhador recebeu o seu salário e o depositou em sua conta corrente bancária.
Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual.
Sabe-se que cada operação bancária de retirada paga um imposto de 0.38% sobre o valor retirado e o saldo inicial da conta está zerado.
Desenvolva um algoritmo que receba o salário do trabalhador, o valor do primeiro cheque, o valor do segundo cheque e mostre ao final quanto sobrou na conta do trabalhador '''

#variaveis
salario = 0.0
cheque1 = 0.0
cheque2 = 0.0
valor_conta = 0.0
imposto = 0.0


#programa
salario = float(input("Informe o valor do salário depositado: "))
cheque1 = float(input("Informe o valor do cheque emitido: "))
cheque2 = float(input("informe o valor do cheque emitido:  "))

imposto = ((cheque1 + cheque2) *0.38 /100)
valor_conta = salario - imposto - cheque1 - cheque2

print(f"O valor restante em sua conta bancária é: R${valor_conta}")