#Demonstração do uso das funções
def adição(x, y):
    w=x+y
    return w
def subtração(x, y):
    return x-y
def multiplicação(x, y):
    return x*y
def divisão(x, y):
    return x/y
print("digite dois valores inteiros...")
n1=int(input("x: "))
n2=int(input("y: "))
op=input("qual operação você deseja fazer? (+,*, /ou -)")

if op=="+":
    z=adição(n1, n2)
    print("resultado da soma:", z)
elif op=="-":
    z=subtração(n1, n2)
    print("resultado da subtração:", z)
elif op=="*":
    z=multiplicação(n1, n2)
    print("resultado da multiplicação:", z)
elif op=="/":
    z=divisão(n1, n2)
    print("resultado da divisão:", z)
else:
    print("operação inválida, tente novamente.")