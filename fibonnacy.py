#codigo de calculo para fibonnacy
f1=0; f2=1; x=0
while x<=2000:
    x= f1 + f2
    f1=f2
    f2=x
    if x>2000:
        break;
    print(x, end=" ")