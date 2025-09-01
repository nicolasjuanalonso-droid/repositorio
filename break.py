#demonstração de estrutura repetitiva...
contador= 0; senha=""
while senha != "s3nh4":
    print("digite a senha:")
    senha=input()
    if senha == "s3nh4":
        print("acesso permitido")
        break
    else:
        print("senha incorreta, tente novamente")
        contador+= 1
        if contador == 3:
            print("3 tentativas excedidas!!!")
            break