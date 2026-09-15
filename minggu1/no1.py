emasB=0
perakB=0
perungguB=0

sisa_emas=0
sisa_perak=0
sisa_perunggu=0
def kupon(emas,perak,perunggu):
    global emasB,perakB,perungguB,sisa_emas,sisa_perak,sisa_perunggu
    if emas >=4:
        emasB+=1
    if perak >=3:
        perakB+=1
    if perunggu >=2:
        perungguB+=1
        
    if emas < 4:
        sisa_emas+=emas
        return
    if perak < 3:
        sisa_perak+=perak
        return 
    if perunggu < 2:
        sisa_perunggu+=perunggu
        return
    
    emas-=4
    perak-=3
    perunggu-=2

    return kupon(emas+2,perak+1,perunggu+1)

kupon(40,30,20)
print(emasB,perakB,perungguB)
print(sisa_emas,sisa_perak,sisa_perunggu)
