print("Ingrese la cantidad de números:")
while True:
    cantidadNumeros = int(input())
    if cantidadNumeros >= 0:
        break

num = 1
while True:
    if num <= cantidadNumeros:
        print(num, " ", num * num, " ", nume + num * num, sep="")
        numero = num + 1
    if num > cantidadNumeros:
        break
