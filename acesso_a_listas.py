#demonstração de acesso a listas.
print("vou montar a marmita com 5 alimentos")
marmita=["feijão", "arroz", "legumes", "salada", "carnes"]
print("eis, a mossa recomendação:", marmita)
resposta=input("quer montar uma marmita diferent (s/n)?")
if resposta=="s":
    for x in range(len(marmita)):
        print(f'digite o {x+1}o. item do cardapio:')
        marmita[x]=input()
    print("a marmita foi:", marmita)
    print("o três primeiros itens foram:", marmita [0:3])
    print("o ultimo item da marmita foi", marmita [-1])
else:
    print("ok.você decide...")

print(marmita[:])
print(marmita[2:3])
print(marmita[0:4:2])
print(marmita[-3:-1])
