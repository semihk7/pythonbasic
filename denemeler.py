# 2 sayinin ortalaması
while True:
    
    sayi1 =float(input('1. Sayı : '))
    sayi2 =float(input('2. Sayı : '))
    
    ortalama=(sayi1+sayi2)/2
    print("\nOrtalama :%.4f "%(ortalama))
    
# Kullanıcıdan alınan 2 sayiyi toplayan fonk    
def topla(s1,s2):
    return s1+s2
    

while True:
    
    sayi1 =float(input('1. Sayı : '))
    sayi2 =float(input('2. Sayı : '))
    
    if sayi1==0 and sayi2==0:
        print("çıkış yapıldı")
        break
    else:
        
        print("\ntoplam ",topla(sayi1,sayi2))

# Kullanıcıdan alınan sayıya kadar olan sayıları toplayan fonksiyon
def topla(a):
    toplam= 0
    
    for i in range(1,a+1):
        toplam+=i
    
    return toplam    


while True:
    
    sayi1 =int(input('1. Sayı : '))
        
    if sayi1==0:
        print("çıkış yapıldı")
        break
    else:
        
        print("\ntoplam ",topla(sayi1))

 


# klasik ortalama
while True:
    vize = (input('Vize Notunuz : '))
    final =(input('Final Notunuz : '))
    
    if(vize =='q' or final == 'q' ):
        print("çıkış yapıldı")
        break
    else:
        ortalama=(float(vize)*0.35)+(float(final)*0.65)
        print("\nOrtalama :{} ".format(ortalama))

        
#final ve vize notlarını hesaplayan fonksiyon
def ort(vize, final):
   
    ortalama=(float(vize)*0.35)+(float(final)*0.65)
    
    return ortalama 


while True:
    
    vize = (input('Vize Notunuz : '))
    final =(input('Final Notunuz : '))
    
    if(vize =='q' or final == 'q' ):
        print("çıkış yapıldı")
        break
    else:
        
        print("\nOrtalama : ",ort(vize,final))



#basit asallık

while True:
    i=0
    sayi=int(input('Sayı: '))
    for i in range(2,sayi):
      if sayi%i==0:
        i+=1
      
    if(i!=0):
      print("Sayı Asal Değil")
    else:
      print("Sayı Asal")

 

# tek ve çift sayıları toplayan
sayi = int(input('Sayıyı Girin : '))
tek_Toplam=0
cift_Toplam=0
for i in range(1,sayi+1):
  if(i%2==0):
    cift_Toplam+=i
  else:
    tek_Toplam+=i
print("Tek Sayıların Toplamı : {}".format(tek_Toplam))
print("Çift Sayıların Toplamı : {}".format(cift_Toplam))

# dairenin alanı fonksiyon ile

def daireAlan(yaricap,pi =3.14):
    alan = pi*float(yaricap) * float(yaricap)
    
    return alan

    
while True:
    
    r = input("Yarıçapı Gir : ")
    if r =='q':
        print("çıkış yapıldı...")
        break
    else:
        print("dairenin alanı: ",daireAlan(r))
     
# dikdortgen alan cevre
def dikdortgenAlan(genislik, yukseklik):
    alan = float(genislik) * float(yukseklik)
    
    return alan

def dikdortgenCevre(genislik,yukseklik):
    cevre =2*(float(genislik) + float(yukseklik))
    return cevre

while True:
    gen = input("Genişlik :")
     
    yuk = input("Yükseklik : ")
     
    print ("Alan :",dikdortgenAlan(gen, yuk))
    print ("Çevre :",dikdortgenCevre(gen, yuk))



#Kullanıcının tuttuğu sayıyı tahmin eden python örneği (HAZIR KOD)
 
from random import randint
 
rand=randint(1, 50)
sayac=0
 
while True:
    
    sayi=int(input("1 ile 50 arasında değer girin (0 Çıkış):"))
    sayac+=1
    if(sayi==0):
        print("Oyunu İptal Ettiniz")
        break
    elif sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Rastele seçilen sayı {}!".format(rand))
        print("Tahmin sayınız {}".format(sayac)) 
    
    
# sayının rakamm toplamı
sayi=input("Bir sayı girin: ")
toplam=0

for i in sayi: # sayıyı string olarak parçalıyor ilk olarak
  toplam += int(i)
 
print("sayının rakamlar toplamı:",toplam)   
    
  
toplam=0
while True:
  sayi = float(input("Bir sayı girin: "))
  if sayi ==0:
    break
  toplam+=sayi
print("Girdiğiniz sayıları toplamı: ",toplam)
    
    
# girilen sayıyı zaman cinsinden yazma 
saniye=int(input("Saniye Giriniz:"))
saat=saniye//3600 
saniye=saniye%3600
dakika=saniye//60
saniye=saniye%60
print("Girdiğiniz Saniyenin Saat Dönüşümü:",saat,"sa",dakika,"dk",saniye,"sn")
    

#girilien değere kadar olan sayıların 2ve3 bölenleri

sayi =int(input("sayi : "))
a = 0
while(a<sayi):
  a=a+1
  if (a%2==0):
    print(a, "2'ye bölünür")
  if (a%3==0):
    print(a, "3'e bölünür")
  
    
for i in range(1,sayi+1):
    if (i%2==0):
        print(i, "2'ye bölünür")
    if (i%3==0):
        print(i, "3'e bölünür")
  
        
  
a=int(input("Birinci sayıyı giriniz:"))
b=int(input("İkinci sayıyı giriniz:"))
c=int(input("Üçüncü sayıyı giriniz:"))
d=int(input("Dördüncü sayıyı giriniz:"))
e=int(input("Beşinci sayıyı giriniz:"))


liste =[a,b,c,d,e]
print(liste)

print(max(liste))
print(sum(liste))



#girilen sayılardan bir liste oluşturup listenin toplamının dinamik olarak alma
liste= []
while True:
    a=int(input("Birinci sayıyı giriniz:"))
    
     
    if a ==0:
        liste.append(a)
        print("sonuc",liste)
        print("sonuc",sum(liste))    
        break
    else:
            
        liste.append(a)
        print("sonuc: ",liste)
        print("sonuc",sum(liste))    

# 2 .dereceden denklem çözümü

a=int(input("a sayısını giriniz:"))
b=int(input("b sayısını giriniz:"))
c=int(input("c sayısını giriniz:"))
delta=b**2-4*a*c
x1 = (-b - delta ** 0.5)/ (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)
if delta<0: 
    print("Reel kök yoktur.delta : ",delta) 
if delta==0: 
  print("Çakışık 2 kök vardır.") 
  print("Denkleminizin birinci kökü:{}\n Denkleminizin ikinci kökü:{}\n".format(x1,x2)) 
if delta>0:
    print("\nGerçek 2 kök vardır.")
    print("Denkleminizin birinci kökü:{}\nDenkleminizin ikinci kökü:{}\n".format(x1,x2))    
 
    
 
    
# Hazır kod ileride lazım olur
print("Oluşturmak istediğiniz yılı ve kaçıncı ayı olduğunu giriniz")
yil = int(input("Seneyi Giriniz: "))
ay = int(input("Ayı Giriniz: "))
 
#Takvim modülünü ekliyoruz.
import calendar
#Son olarak da buraya takvim görüntüleme kodunu ekliyoruz.
print(calendar.month(yil, ay)) 

# Hazır kod ileride lazım olur  
sayi = int(input("Bir sayı giriniz: "))
#Ardından bin,oct ve hex kodlarımızla kolaylıkla sayımızı 2'lik, 8'lik ve 16'lık tabanlara çevirebiliyoruz.
print(sayi,"sayısının 2'lik, 8'lik ve 16'lık tabana çevrilmiş halleri:")
print("2'lik tabanda:",bin(sayi))
print("8'lik tabanda:",oct(sayi))
print("16'lık tabanda:",hex(sayi))
 





# sayinin faktöriyeli fonksiyon ile

def	faktöriyel(sayi):
			f=1
			for	i	in	range(1,sayi+1):
				f=f*i
			return	f
            
            
while True:
    a = int(input("sayi: "))
    if a>=1:
        print("Sayinin Faktöriyeli : ",faktöriyel(a))
    
    else:
        print("çıkış...")
        break
    
    
print("faktöriyeli",faktöriyel(5)   ) 




# hazır kod lazım olur  
liste = [1,1,1,1,1,2,2,3,2,4,4,54,5,6,7]
 
liste2=[]
listeTekrar =[]
for deger in liste:
    if deger not in liste2:
        liste2.append(deger)
        a=sorted(liste2)
    else:
      listeTekrar.append(deger)
 
print(a)
print(listeTekrar)



# hazır kod İsim oluşturucu
import random

def generate_name():
    first_names = ["Albert", "Charles", "Nicolas", "Michael", "Anders", "Isaac", "Stephen", "Marie", "Richard"]
    last_names = ["Einstein", "Darwin", "Copernicus", "Faraday", "Celsius", "Newton", "Hawking", "Curie","Dawkins"]
    return "{} {}".format(random.choice(first_names), random.choice(last_names))

for i in range(5):
    print(generate_name())


#  Sıcaklık çevirici hazır kod

print("-" * 30)
print("1- Celsius to fahrenheit")
print("2- Fahrenheit to celsius")
print("-" * 30)

choice = input("Your choice (1/2): ")

if choice == "1":
    print("\n# Celsius to Fahrenheit")
    celsius = float(input("Degree to convert: "))
    fahrenheit = (celsius * 1.8) + 32
    print("{} degree celsius is equal to {} degree fahrenheit.".format(celsius, fahrenheit))
elif choice == "2":
    print("\n# Fahrenheit to Celsius")
    fahrenheit = float(input("Degree to convert: "))
    celsius = (fahrenheit - 32) / 1.8
    print("{} degree fahrenheit is equal to {} degree celsius.".format(fahrenheit, celsius))
else:
    print("Congratulations! You hacked the super-program.")




# hazır kod değiştirdim lazım olur
import random


sentences = " Mustafa Kemal Atatürk(1881[d] - 10 Kasım 1938), Türk asker ve devlet adamıdır. Türk Kurtuluş Savaşı'nın başkomutanı ve Türkiye Cumhuriyeti'nin kurucusudur.I. Dünya Savaşı sırasında Osmanlı ordusunda görev yapan Atatürk, Çanakkale Cephesi'nde miralaylığa, Sina ve Filistin Cephesi'nde ise Yıldırım Orduları komutanlığına atandı. Savaşın sonunda, Osmanlı İmparatorluğu'nun yenilgisini takiben Kurtuluş Savaşı ile simgelenen Türk Ulusal Hareketi'ne öncülük ve önderlik etti. Türk Kurtuluş Savaşı sürecinde Ankara Hükûmeti'ni kurdu, Türk Orduları Başkomutanı olarak Sakarya Meydan Muharebesi'ndeki başarısından dolayı 19 Eylül 1921 tarihinde Gazi unvanını aldı ve mareşallik rütbesine yükseldi. Askerî ve siyasi eylemleriyle İtilaf Devletleri ve destekçilerine karşı zafer kazandı. Savaşın ardından Cumhuriyet Halk Partisi'ni Halk Fırkası adıyla kurdu ve ilk genel başkanı oldu. 29 Ekim 1923'te Cumhuriyetin İlanı akabinde Cumhurbaşkanı seçildi. 1938'deki ölümüne dek dört dönem bu görevi yürüterek Türkiye'de en uzun süre cumhurbaşkanlığı yapmış kişi oldu.".split(".")

print(("-" * 30) + "\nCümle Oluşturucu\n" + ("-" * 30))

n = int(input("Number of sentences: "))

liste = []

for i in range(n):
    liste.append(random.choice(sentences))

print("Cümleler: {}.".format(".".join(liste)))



# hazır kod yazılanı tersine çevriyor
def reverse(value, output=[]):
    #range(start, stop, step)
    for i in range(len(value) - 1, -1, -1):
        output.append(value[i])
    
    return "".join(output)

text = input("What's up: ")
print("Your reversed text is: {}".format(reverse(text)))




#sesli harfleri bulan kod
def vowels_count(text, output=0):
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            output += 1
    return output

text = input("Type some text: ")
print("Vowels in text: {}".format(vowels_count(text)))



#hazır kod düzenlenebilir.!!!
height = int(input("Height of Christmas Tree: "))

for i in range(int(height * 0.7)):
    print( (" " * (height - ( i // 2))) + ("*" * i))

for i in range(int(height * 0.7), height):
    print((" " * (height - 1)) + "||")


def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)