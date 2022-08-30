import os

def linha(valor):
    print("-="*valor)

def interface_binpye():
    os.system("cls")
    linha(30)
    print("Escolha sua alternativa")
    print("1) converter binario para decimal")
    print("2) converter decimal para binario")
    linha(30)
    bim = input(":>")
    if bim == "2":
        os.system("cls")
        linha(30)
        print("digite um valor")
        decimal = int(input(":>"))
        linha(30)
        os.system("cls")
        print(f"o valor decimal em binario e: {decimal:b}")
    elif bim == "1":
        os.system("cls")
        linha(30)
        print("digite um valor")
        binario = int(input(":>"))
        linha(30)
        os.system("cls")
        n = len(str(binario))
        demy = 0
        i = 0
        while n >= 0:
            resto = binario % 10
            demy = demy + (resto * (2**i))
            n -= 1
            i += 1
            binario = binario // 10
        os.system("cls")
        print(f"o valor binario convertido para decimal e {demy}")

if __name__ == "__main__":
    interface_binpye()



#   try:
#       print(f"{a:b}")
#   except NameError:
#       print("da nao meu parcero")