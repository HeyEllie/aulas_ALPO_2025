nome = ""
sexo = "" #M/F"
idade = 0
sa = "" #B/R
contador = "S"
mo = 0
tapto = 0
tnapto = 0

while contador == "S":
    nome = input("Informe o nome: ")
    sexo = input("Informe o sexo M - nasculino | F - feminino: ").upper()
    idade = int(input("Informe a idade: "))
    sa = input("Informe a saúde B - bom | R - ruim: ").upper()

    if (sexo == "M") and (idade >= 18) and (sa == "B"):
        print(f"O candito(a) {nome} está apto(a) para cumprir o serviço militar!")
        tapto += 1
    else:
        if sexo == "F":
            print(f"O candito(a) {nome} não está apto(a) para cumprir o serviço militar pois é do sexo feminino!")
            tnapto += 1
        else:
            if idade <= 18:
                print(f"O candito(a) {nome} não está apto(a) para cumprir o serviço militar pois é menor de idade!")
                tnapto += 1
            else:
                if sa == "R":
                    print(f"O candito(a) {nome} não está apto(a) para cumprir o serviço militar pois tem saúde ruim!")
                    tnapto += 1
    contador = input("Deseja informar os dados de outro usuário? S-sim | N - não: ").upper()

print(f"O total de aptos é: {tapto}")
print(f"O total de não aptos é: {tnapto}")


