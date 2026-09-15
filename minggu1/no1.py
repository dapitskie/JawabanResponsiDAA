emasB=0
perakB=0
perungguB=0

sisa_emas=0
sisa_perak=0
sisa_perunggu=0

def kupon(emas,perak,perunggu):
    global emasB,perakB,perungguB,sisa_emas,sisa_perak,sisa_perunggu
    
    if emas < 4 and perak < 3 and perunggu < 2:
        sisa_emas = emas
        sisa_perak = perak
        sisa_perunggu = perunggu
        return

    if emas >= 4:
        emasB += 1
        return kupon(emas - 4 + 2, perak, perunggu)
    
    if perak >= 3:
        perakB += 1
        return kupon(emas, perak - 3 + 1, perunggu)
    
    if perunggu >= 2:
        perungguB += 1
        return kupon(emas, perak, perunggu - 2 + 1)

kupon(40,30,20)

total_emas = 40 + emasB * 2
total_perak = 30 + perakB * 1
total_perunggu = 20 + perungguB * 1

print(f"Emas     : Total={total_emas} | a. Penukaran={emasB}x | b. Sisa={sisa_emas}")
print(f"Perak    : Total={total_perak} | a. Penukaran={perakB}x | b. Sisa={sisa_perak}")
print(f"Perunggu : Total={total_perunggu} | a. Penukaran={perungguB}x | b. Sisa={sisa_perunggu}")