num = int(input("digite un numero: "))

if num > 0:
    copiaNumero = num
    cifras = 0
    suma = 0
    contadorCifras = 0
    while copiaNumero > 0:
        cifras = copiaNumero % 10
        copiaNumero = copiaNumero // 10
        suma = suma + cifras
        contadorCifras = contadorCifras + 1
    print("La cantidad de cifras de:", num, "son", contadorCifras)
    print("La sumatoria es:", suma)
else:
    print("El numero no es positivo")
