votosAndroid = 0
votosIOS = 0
votosInvalidos = 0
while True:
    print("Ingrese su código:")
    codigo = int(input())
    if codigo != 0:
        print("Ingrese su elección (Android / iOS):")
        eleccion = input()
        eleccion = eleccion
        if eleccion == "android":
            votosAndroid = votosAndroid + 1
        else:
            if eleccion == "ios":
                votosIOS = votosIOS + 1
            else:
                print("el voto no se tendrá en cuenta.")
                votosInvalidos = votosInvalidos + 1
    if codigo == 0:
        break

print("Votos Android:", votosAndroid)
print("Votos iOS:", votosIOS)
print("Votos no válidos (no contados):", votosInvalidos)

if votosAndroid > votosIOS:
    print("La plataforma elegida es: Android")
else:
    if votosIOS > votosAndroid:
        print("La plataforma elegida es: iOS")
    else:
        print("Hay empate: se debe usar otro mecanismo de elección.")
