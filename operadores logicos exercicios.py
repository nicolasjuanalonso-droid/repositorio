#demonstração de operadores logicos em condicionais
print("o que você vai fazer amanhã de manhhã?")
print("dormir/estudar/planejar")
manha=input()
print("o que você vai fazer amanhã a tarde?")
print("dormir/estudar/trabalhar")
tarde=input()
if not manha or not tarde:
    print("você precisa me dizer o que vai fazer")
else:
    if manha == "dormir" or tarde == "jogar":
        print("você não vai fazer nada produtivo")
    elif manha ==estudar or tarde == "trabalhar":
        print("você vai ter um dia produtivo")
    elif manha == "planejar" and tarde == "trabalhar":
        print("para trabalhar melhor, devo planejar")
    else:
        print('não planejamos essas ações')

        print("tenha um bom dia!")
