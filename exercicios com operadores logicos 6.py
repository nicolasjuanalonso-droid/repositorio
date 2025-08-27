#pedra,papel e tesoura.
x=input("escolha pedra,papel ou tesoura:")
if x == "pedra":
        print("você escolheu pedra,que vence tesoura e perde para papel.")
elif x == "papel":
        print("você escolheu papel,que vence pedra e perde para tesoura.")
elif x == "tesoura":
        print("você escolheu tesoura,que vence papel e perde para pedra.")
else:
    print("invalido")