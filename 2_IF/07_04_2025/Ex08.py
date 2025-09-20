'''
Voc~e está fazendo um trabalho de classificação de solo. Após colher uma amostra e verificar a quantidade de pontos de água presente nela, classificando em:
rochosa: se menos ou igual a 10 pontos de água;
firme: se + do 10 e _ ou = a 40 pontos;
pantanosa: se + do 40 e - ou = 80 pontos;
quantidade inválida: se + do que 80 pontos
'''

a = 0.0

a = float(input("Informe a quantidade de pontos de água presente na amostra: "))

if a <= 10:
    print("O seu solo é ROCHOSO!!!")
else:
    if a > 10 and a <= 40:
        print("O seu solo é FIRME!!!")
    else:
        if a < 40 and a <= 80:
            print("O seu solo é PATANOSO!!!")
        else:
            print("QUANTIDADE INVÁLIDA!!!")
