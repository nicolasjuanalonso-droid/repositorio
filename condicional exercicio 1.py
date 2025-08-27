#verificar saldo do cliente para que ele possa efeituar a compra
saldo=int(input("digite seu saldo para verificar condições de compra"))
if saldo>3000:
    print("você pode efetuar a compra desse computador")
else:
    print("vc não pode efetuar essa compra")
