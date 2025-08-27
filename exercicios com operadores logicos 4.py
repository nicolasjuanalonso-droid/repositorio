jogo=input("qual função deseja exercer?")
if jogo == "goleiro" or jogo == "zagueiro" or jogo == "lateral":
    print("Defesa!")
elif jogo == "ala" or jogo == "volante" or jogo == "Meia":
    print("meio campo!")
elif jogo == "ponta" or jogo == "atacante" or jogo == "Centravante":
    print("ataque!")
else:
    print("TEIMOSO!")
