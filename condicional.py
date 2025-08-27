#demonstração do uso do if 
print('Digite a sua idade:')
idade=int(input())
if idade<18:
    print("você não é maior de idade!")
    print("não poderá realizar operações bancárias!")
elif idade>=65:
    print("você está aposentado")
    print("poderemos ofereçer suporte técnico...")
else:
    print('você é maior de idade.')
    print("portanto, poderá realizar a operação.")

print("obrigado por escolher nossos serviços!")

    