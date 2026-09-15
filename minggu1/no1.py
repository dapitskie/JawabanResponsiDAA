def kupon(emas=0,perak=0,perunggu=0):
    if emas < 4:
        return emas
    if perak < 3:
        return perunggu
    if perunggu < 2:
        return perunggu
    emas-=4
    perak-=3
    perunggu-=2
    
    emasB=1+kupon(emas+2)
    perakB=1+kupon(perak+1)
    perungguB=1+kupon(perunggu+1)

    return f"Emas: {emasB}, Perak: {perakB}, Perunggu: {perungguB}"

print(kupon(40,30,20))
