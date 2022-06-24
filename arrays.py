import numpy as np

data_list = [1,2,3,4,5]

array = np.array(data_list)

data_list2 = [[10,20,30],[40,50,60],[70,80,90]]

array2 = np.array(data_list2)


a = np.arange(10,20)
b = np.arange(0,100,3)
c = np.zeros(10)
d = np.ones(10)
e = np.zeros((3,3)) #tuple olmak zorunda
e = np.zeros((3,3,3))
f = np.ones((3,3,3))
g = np.ones((2,3))
h = np.linspace(0,100,11) # 11 tane yazmak gerekiyor 
ı = np.linspace(0,1,6)
j = np.eye(6) 
k = np.random.randint(0,10) # 0(dahil) ile 10(hariç) arasında random int oluşturur.
l = np.random.randint(10) # 0(dahil) ile 10(hariç) arasında random int oluşturur.
m = np.random.randint(1,10,5) # 1(dahil) ile 10(hariç) arasında 5 değer oluşturarak 5 değer saklayan array oluşturur.
n = np.random.rand(5) # 0 ile 1 arasında 5 float değerler oluşturur.
o = np.random.randn(10) # 0 etrafında - ve + değerlerle Gaussian Distribution'a göre değerler oluşturur.
aa = np.empty((2, 3)) 

arr = np.arange(25)

p = arr.reshape(5,5) # 5 x 5 =  25 tek boyutlu matrisi 2 boyuta çevirir.

r = np.random.random((3, 3))
s = np.random.randint(5,10,size=(3, 3))
t = np.random.randint(1,100,10)
u = t.max()
v = t.min()
y = t.sum()
z = t.mean()
w = t.argmin()
x = t.argmax()

detArray =  np.random.randint(1,100,25)

detArray = detArray.reshape(5,5)
det = np.linalg.det(detArray)
det_1 = round(np.linalg.det(detArray))


arr1 = np.array([10,20,30,40,50])
arr2 = np.array([2,3,4,5,6])

ar = np.sqrt(arr1)


a = np.arange(15).reshape(3, 5)
b = a.shape
#c = ndim
d = a.dtype.name
e = a.itemsize
f = a.size
g = a.dtype

h= np.array([1.2, 3.5, 5.1])
ı =h.dtype

j = np.array([[1, 2], [3, 4]], dtype=complex)

from numpy import pi
np.linspace(0, 2, 9)                 
x = np.linspace(0, 2 * pi, 10)        # useful to evaluate function at lots of points
f = np.sin(x)


c = np.arange(24).reshape(2, 3, 4)
a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)
c = a + b
d = np.exp(c * 1j)
a.ravel()  # returns the array, flattened

b = np.arange(12).reshape(3, 4)

c = b.sum(axis=0) # sütunlar toplamı
b.min(axis=1)     # min of each row

np.exp(b)

a = np.arange(10)**3
b = a[::-1] # ters çevirmek için
for i in a:
    print(round(i**(1 / 3.)))



def f(x, y):
    return 10 * x + y

b = np.fromfunction(f, (5, 4), dtype=int)

b[0:5, 1]  # each row in the second column of b
b[:, 1]    # equivalent to the previous example
b[1:3, :]  # each column in the second and third row of b


c = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
               [ 10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])

c.shape

c[1, ...]  # same as c[1, :, :] or c[1]
c[..., 2]  # same as c[:, :, 2]

for row in b:
    print(row)

for element in b.flat:
    print(element)

b = a.T #transpoze almak için

a =np.array([[3., 7., 3., 4.],
       [1., 4., 2., 2.],
       [7., 2., 4., 9.]]) 
b = a.T #transpoze almak için

from numpy import newaxis
np.column_stack((a, b))  # with 2D arrays
a = np.array([4., 2.])
b = np.array([3., 8.])
np.column_stack((a, b)) 
np.hstack((a, b)) 
a[:, newaxis]  
np.column_stack((a[:, newaxis], b[:, newaxis]))





"""Pandas Seriler......"""
import numpy as np
import pandas as pd 

x = [1,2,3,4,5]
pd.Series(x)

ülke = ["abd","çin","italya","Türkiye"]
pd.Series(ülke)

labels = ["Semih","Ali","Umut"]
data_list = [27,22,25]
new_seri = pd.Series(data_list,labels)

arr = np.array([27,22,25])
seri = pd.Series(arr,labels)
new_seri=pd.Series(data = arr,index=["A","B","C"])

dict_d = {"Semih":27,
         "Ali":22,
         "Umut":25}

dic = pd.Series(dict_d)

sene_2017 = pd.Series([5,10,15,20],["Buğday","Mısır","Arpa","Ayçiçeği"])
sene_2018 = pd.Series([15,12,18,22],["Buğday","Mısır","Kiraz","Ayçiçeği"])

#2 seriyi toplayabilmemiz için index değerleri aynı olmalı.
    

















