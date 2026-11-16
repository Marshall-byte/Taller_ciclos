hora = 0
while True:
    minuto = 0
    while True:
        seg = 0
        while True:
            print(hora, ":", minuto, ":", seg, sep="")
            seg = seg + 1
            if segundo > 59:
                break
        minuto = minuto + 1
        if minuto > 59:
            break
    hora = hora + 1
    if hora > 23:
        break
