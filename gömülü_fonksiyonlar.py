"""-------------Gömülü Fonksiyonlar-----------"""

# kare alan map 

def kare_al(sayi):
    return sayi**2


kare = list(map(kare_al,[1,2,3,4,5])) # yapılan işlemi tüm elemanlara uyguluyor
print(kare)

#alınan sayıların küpünü alıp listede saklıyor.
liste =[]
while True:
    sayi = int(input("sayi gir : "))
    
    
    if sayi !=0:
        liste.append(sayi)
        kup = list(map(lambda x:x**3 ,(liste))) # yapılan işlemi tüm elemanlara uyguluyor
        print(kup)
        
    else :
        kup = list(map(lambda x:x**3 ,(liste))) # yapılan işlemi tüm elemanlara uyguluyor
        print(kup)
        
        break
    
    
#1 ile 50 arasındaki sayıların asallıkllrı. Geliştirilebilir !!!
    
a  = list(filter(lambda x : x %2 == 0, range(1,50)))    

print (a)    


def asal_mi(x,i=2):
    
    if(x == 2):
        return True # Asal sayı
    else:
        while(x>i):
            if (x % i == 0):
                return False # Asal Değil
            i += 1
    return True
    
    
    
a  = list(filter(asal_mi, range(1,50)))    
print(a)  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    