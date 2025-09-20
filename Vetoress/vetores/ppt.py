import random
t=0
p=0
pa=0
part=0
part=int(input(" quantas partidas serao jogadas "))

for i in range (1,part,1):

    j="papel","tesoura","pedra"
    e=random.choices(j)
    j2="papel","tesoura","pedra"
    e2=random.choices(j2)
    print(f"eu escolhi {e}")
    print(f"eu escolhi {e2}")

    if e=="papel" and e2=="tesoura" or e2=="papel" and e=="tesoura":
        print("a tesoura ganhou")
        t+=1
    if e=="papel" and e2=="pedra" or e2=="papel" and e=="pedra":
        print("a papel ganhou")
        pa+=1
    if e=="tesoura" and e2=="pedra" or e2=="pedra" and e=="tesoura":
        print("a pedra ganhou")
        p+=1