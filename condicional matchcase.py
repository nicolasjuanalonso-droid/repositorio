#demonstração do uso da condicional match/case...
print("Digite o numero referente ao estado da moeda:")
print("1. flor de cunho")
print("2. Soberba")
print("3. muito bem conservada")
print("4. bem conservada")
print("5. outros estados")
estado=int(input())

match estado:
    case 1:
        print("perfeita! vou pagar R$1.000.000,00")
    case 2:
        print("quase perfeita! Ofereço R$ 250.000,00")
    case 3:
        print("que otimo! posso dar uns R$ 100.000,00")
    case 4:
        print("que bom. aceitaria R$ 30.000,00?")
    case 5:
        print ("Desculpe, não aceito neste estado:")
    case _:
        print("opção não conehecida")
        