

def tbb(sayi):
    tam_bol = []
    for i in range(1,sayi+1):
        if (sayi % i == 0):
            tam_bol.append(i)
    return tam_bol


while True:
    sayi = int(input("bir sayi gir : "))
    if (sayi==0):
        print("Çıkış  ")
        break
    else:
    
        print("tam bolenler ", tbb(sayi))
        