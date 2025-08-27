serviço=input("o serviço foi prestado? (sim/não) ")
if serviço == "não":
    print("Serviço não prestado.")
elif serviço == "sim":
        print("qual nota daria ao serviço? (1-5) ")
        nota = int(input())
        if nota ==1:
            print("péssimo")
        elif nota == 2:
            print("ruim")
        elif nota == 3:   
            print("razoável")
        elif nota == 4:
            print("bom")
        elif nota == 5:
            print("otimo")
        elif nota == 0:
            print("poderia escrever sua reclamação?")
        else:
            print("nota invalida")
else:
   print("invalido")

        
