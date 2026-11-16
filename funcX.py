print("Ingrese el máximo valor para x:")
while True:
    valorX = int(input())
    if valorX >= 0:
        break

x = 0
while True:
    if x <= valorX:
        fx = x ** 3 + x ** 2 - 5
        print("Para x =", x, "f(x) =", fx)
        x = x + 2
    if x > valorX:
        break
