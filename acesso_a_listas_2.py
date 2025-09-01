#Demonstração de funções en listas...
sonhos= ["1. me divertir na Disney",
         "2. me banhar na praia de sepetiba",
         "3. tirar as férias em Paris", 
         "4. fazer compras no WestShopping", 
         "5. ver as pirâmides do Egito"]
for x in sonhos:
    print(x)
print("ops, não quero Sepetiba!")
del(sonhos[1])
print("E nem westshopping")
del(sonhos[2])

print("conferindo os sonhos")
for x in sonhos:
    print(x)
