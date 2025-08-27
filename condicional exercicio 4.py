#avaliação de filmes e series
input("digite um filme ou série que você assistiu")
nota=int(input("de 1 5 qual a nota você daria?"))
match nota:
    case 1:
        print("péssimo")
    case 2:
        print("ruim")
    case 3:
        print("razoavel")
    case 4:
        print("bom")
    case 5:
        print("ótimo")
    case _:
        print("nota inválida")