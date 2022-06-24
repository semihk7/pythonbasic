

def my_function():
  print("This is a function")
  
my_function()  



def my_function(name):
  print(name + " Kuşcu")

my_function("Semih")
my_function("Ali")
my_function("Umut")

def selam():
    print("selam nasılsın")
    
    
def topla(x,y):
    print("toplam : ",x+y)
    
def fact (sayi):
    f=1
    for i in range(1,sayi+1): # range de son sayıyı almıyor diye +1
        f =  f*i
    return f
 

    
def fac(sayi):
    f = 1
    if (sayi == 0 or sayi ==1):
        print("factoriyel 1'e eşittir")
    else:
        while (sayi >=1):
            f=f*sayi
            sayi=sayi-1
        print("F  = ",f)
"""            
      f   sayi
      1    5
      5    4
      20   3
      60   2
      120  1
      120                 """


def selamla(isim = " None"): # eğer selamla fonk bir değer atanmazsa none yazacak
    print("selam",isim)

def bilgi(isim ="none", soyisim = "none", numara ="none"): # varsayılan none dönyüor

    print("isim","soyisim","numara",isim,soyisim,numara)
    
def topla(*a):
    toplam= 0
    for i in a:
        toplam+=i
    return toplam

def isim(*args):
    print("İsim :  {} \nSoyisim: {} \nOkul Numarası:  {} ".format(args[0],args[1],args[2]))

def new(*args ,**kwargs):
    print("args : ",args, "kwargs",kwargs)
    
renkler = ["sarı","kırmızı","yeşil","beyaz","siyah"]


for index,deger in enumerate(renkler):
    print(index,deger)
    












