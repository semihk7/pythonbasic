""" ---------------Nesne Tabanlı Programlama------------------""" 


class Ogrenci():
    
    
    def __init__(self,isim,soyisim,yas,not_ort):
        self.isim = isim
        self.soyisim=soyisim
        self.yas = yas
        self.not_ort = not_ort
        
    

    def info(self):
        print("{} {} {} {}".format(self.isim,self.soyisim,self.yas,self.not_ort))
    def change(self):
        self.not_ort=self.not_ort+5
        return self.not_ort

bir = Ogrenci("Semih","Kuşcu",27,95)
iki = Ogrenci("Ali","Kuşcu",22,74)


"""Encapsulation"""

class Ogrenci():
    
    
    def __init__(self,isim,soyisim,yas,not_ort):
        self.isim = isim
        self.soyisim=soyisim
        self.yas = yas
        self.__not_ort = not_ort
        
    

    def info(self):
        print("{} {} {} {}".format(self.isim,self.soyisim,self.yas,self.not_ort))
    
    def change(self):
        self.not_ort=self.not_ort+5
        return self.not_ort
    
    def getNot_ort(self):
        return self.__not_ort
    
    def setNot_ort(self,yeni):
        self.__not_ort=yeni
      

        
        
bir = Ogrenci("Semih","Kuşcu",27,95)
iki = Ogrenci("Ali","Kuşcu",22,74)


"""-------------Inheritiance Kalıtım----------------"""

class Okul :
    def __init__(self,isim,soyisim,yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        print("---")
        
        

class Ogretmen(Okul):
    
    def __init__(self,isim,soyisim,yas,maas,uzmanlık):
        
        super().__init__(isim,soyisim,yas)
        self.maas=maas
        self.uzmanlık = uzmanlık
        print("----")
        
        
    def info(self):
        
        print("{} {} {} {} {}".format(self.isim,self.soyisim,self.yas,self.maas,self.uzmanlık))
        
            
bir = Ogretmen("Semih","Kuşcu",27,5000,"mühendis")
iki = Ogretmen("Ali","Kuşcu",22,7000,"öğretmen")
       
        

"""----------Abstract Class ( Soyut Sınıflar)------------"""

from abc import ABC,abstractmethod


class Hayvan(ABC):
    @abstractmethod
    def yürü(self):
        print("hayvan yürüyor")
        
    @abstractmethod
    def koş(self):
        print("hayvan koşuyor")
        
    
class Aslan(Hayvan):
    def yürü(self):
        print("aslan yürüyor")
        
    def koş(self):
        print("aslan koşuyor")
        
                 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        





































