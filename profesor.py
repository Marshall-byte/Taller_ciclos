x = 0
suma = 0
aprobado = 0
reprobado = 0
numSt = int(input("Digite el numero de estudiantes a evaluar: "))
while x < numSt:
    nota = float(input("Digite la nota del estudiante: "))
    if nota < 0 or nota > 5.0:
        print("Nota no valida")
    else:
        if nota >= 3.0:
            print("Aprobado")
            aprobado = aprobado + 1
        else:
            print("Reprobado")
            reprobado = reprobado + 1
    x = x + 1
    suma = suma + nota
promedio = suma / numSt
print("El numero de estudiantes evaluados fueron:", numSt)
print("Aprobados:", aprobado)
print("Reprobados:", reprobado)
print("Promedio:", promedio)
