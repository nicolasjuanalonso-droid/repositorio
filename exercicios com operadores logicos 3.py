#ver se um triangulo é equilátero, isósceles ou escaleno
print("digite o comprimento do lado a de um triangulo")
a = float(input())
print("digite o comprimento do lado b de um triangulo")
b = float(input())
print("digite o comprimento do lado c de um triangulo")
c = float(input())
if a == b == c:
    print("é um triangulo equilátero")
elif a == b or b == c or a == c:
    print("é um triangulo isósceles")
else:
    print("é um triangulo escaleno")