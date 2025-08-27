#boletim calcular media do aluno:
a=int(input("nota em portugues"))
b=int(input("nota em matematica"))
c=int(input("nota em historia"))
e=int(input("nota em geografia"))
x=(a+b+c+e)/4
if x>7:
   print("você está aprovado")
elif x>=5:
    print("está de recuperação")
else:
    ("está reprovado.")

