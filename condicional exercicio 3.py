#calcular imc do usuario:
peso=float(input("Digite seu peso em kg: "))
altura=float(input("Digite sua altura em metros: "))
imc=peso/(altura**2)
if imc>25:
    print("está no peso ideal")
elif imc<18:
    print("está abaixo do peso ideal")
else: 
    print("seu peso está ideal")