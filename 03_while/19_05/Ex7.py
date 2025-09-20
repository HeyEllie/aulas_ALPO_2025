'''
a prefeitura de uma city fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e numero de filhos
algoritmo apresentar: 
a-média do salário da população
b-'' do num. de filhos
c-maior  salario
d-percentual de pessoas com salário ate r$100,00
o sist. deve ficar solicitando novos dados até o usuario mandar parar usando o menu:
- escolha uma opção:
1 - para cadastrar
2 - para sair
'''
dados = 1
total_sal = 0.0
total_filhos = 0.0
percentual = 0.0
media_sal = 0.0
media_filhos = 0
somasal = 0.0
qtdcad = 0
qtd100 = 0.0
sal = 0.0
filhos = 0
maiorsal  = 0.0 

while dados == 1:
    dados = int(input("Informe 2 para parar ou 1 para cadastrar: "))
    if dados == 1:
        sal = float(input("Informe o valor do salário: "))
        filhos = int(input("Informe o número de filhos: "))
    somasal += sal
    total_filhos += filhos
    qtdcad += 1

    if(sal > maiorsal):
        maiorsal = sal  

    if sal <= 100:
        qtd100 += 1
    
if qtdcad >= 1:
    media_sal = somasal/qtdcad
    media_filhos = total_filhos/qtdcad
    perc100 = qtd100/qtdcad * 100

print(f"A média do salário foi de: {media_sal:,.2f}")
print(f"O percentual de pessoas com salário de até R$100,00 foi de: {percentual:,.2f}%")
print(f"A média do número de filhos foi de: {media_filhos:,.2f}")
print(f" O maior salário foi de: {maiorsal:,.2f}")