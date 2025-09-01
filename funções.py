#demonstração de uso de funções
def apresentar():
    print(f"meu nome è{myName}.")
    print(f"minhaaltura è{myHeight}metros.")
    print(f"minha idade è{myAge}anos.")
    return
def conferir(x):
    if x>=18:
        print("você é maior de idade.")
    else:
        print("ops,você é menor de idade não pode.")
    return
myName=str(input("qual seu nome?"))
myHeight=float(input("qual sua altura?"))
myAge=int(input("qual sua idade?")) 
apresentar()
conferir(myAge)