#prograna "par ou impar"
import random

def parimpar(x, y):
    resultado = (x + y) % 2
    if resultado == 0:
        print("É par! Ser humano venceu!")
    else:
        print("É impar! Computador venceu!")

N1 = random.randint(1, 1000)
N2 = int(input("usuario-digite um numero: "))
parimpar(N1, N2)
print("computador gerou um numero", N1)
print("você digitou:", N2)