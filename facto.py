num = int(input("Ingrese un número: "))
if num < 0:
    print("el número no posee factorial.")
else:
    factorial = 1
    x = 1
    while True:
        if num > 0:
            factorial = factorial * x
            x = x + 1
        if x > num:
            break
    print("El factorial de", num, "es:", factorial)
