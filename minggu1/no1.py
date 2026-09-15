emasB=0
perakB=0
perungguB=0
def kupon(emas,perak,perunggu):
    global emasB,perakB,perungguB
    if emas >=4:
        emasB+=1
    if perak >=3:
        perakB+=1
    if perunggu >=2:
        perungguB+=1
    if emas < 4:
        return 
    if perak < 3:
        return 
    if perunggu < 2:
        return 
    
    emas-=4
    perak-=3
    perunggu-=2

    return  kupon(emas+2,perak+1,perunggu+1)

print(kupon(40,30,20))
print(emasB,perakB,perungguB)
