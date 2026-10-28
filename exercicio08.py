print("menu: ")
print("1 - par ou impar")
print("2 - compare o numero")
print(" 3 - calcule o dobro")
resposta = "sim"
while resposta == "sim" :
    opcao = int(input("escolha uma opção: "))
    match opcao:
        case 1:
            print("pae ou impar")
            numero = int(input("numero "))
            if numero %2 == 0:
                print(f"{numero} é par. ")
            else:
                print(f"{numero} é impar.")
        case 2:
            print("compare os numeros")
            n1 = int(input("1 numero: "))            
            n2 = int(input("2 numero: "))
            if n1 > n2:
                print(f"{n1} é maior que {n2}")
            elif n1 < n2:
                print(f"{n1} é menor que {n2}")
            else:
                print(f"{n1} é igual a {n2}")
        case 3:
            print("dobro")
            num = int(input("escolha um numero:"))
            dobro = num * 2 
            print(f"o dobro de {num} é {dobro}")
        case _:
            print("opção inválida")
    resposta = input("deseja continuar? (sim ou não)")
    if resposta != "sim":
        print("programa encerrado")
        break         
            
                           
                    