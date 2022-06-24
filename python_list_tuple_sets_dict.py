


"""
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.


"""



mylist = ["apple", "banana", "cherry"]

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(len(mylist))
print(type(mylist))

print(mylist[0]) 
print(mylist[-1])

print(mylist[0:3])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:3])

print(thislist[2:])

 
  
if "apple" in thislist:  
  print("yes")
  
if "potato" in thislist:
    print("yes")
    
else :
    print("no")
  
  
thislist[1] = "muz"   
print(thislist) 
  
thislist[5:6] = ["muz" , "elma"]  

thislist = ["apple", "banana", "cherry"]
thislist.insert(-1, "potato") # index kaybı olmadan eleman ekleme
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # son indexe ekliyor.
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)   # listeleri birleştiriyor.
 
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
thislist.remove([0]) # çalışmıyor başka kodu var
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # indexteki elemanı silmek için
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop(-1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i+=1

bitki = ["elma","muz","patates","domates"]
new =[]

for x in bitki:
    if "ma" in x:  # ma ile biten kelimeleri alıyor.
        new.append(x)
print(new)        


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


newlist = [x for x in bitki if x == "elma"] # sadece elmayı alır
newlist = [x for x in bitki if x != "elma"] #elma dışında kalanları alır


newlist = [x for x in range(10) if x < 5]

newlist = [x.upper() for x in bitki] # alttaki döngünün kısa hali

a = []
for x in bitki:    # listeyi değil de listedeki elemaları tek tek alıp döngüye sokuyoruz
    x = x.upper()
    a.append(x)
print(a)


newlist = [x if x != "muz" else "orange" for x in bitki]

#"Return the item if it is not banana, if it is banana return orange".

bitki = ["elma","muz","patates","domates"]


new = []
for x in bitki:
    if x!= "muz"  :
       new.insert(3,x)
    
    else : 
        new.insert(1,"orange")

print(new)



thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # alfabetik sıraya göre

thislist = [100, 50, 65, 82, 23]
thislist.sort()
thislist.sort(reverse = True)
print(thislist)


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)



list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)



"""---------------------TUPLE--------------------"""


thistuple = ("apple", "banana", "cherry")
print(thistuple)


tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")


thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #index bakılırken kalın parantez yine de


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
# listeye çevirip değişim yapabilirim
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
# 2 tuple birleştirme
print(thistuple)
 

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

fruits = ("apple", "banana", "cherry")
(a, b, c) = fruits
#unpacking
print(green)
print(yellow)
print(red)




fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(*green,yellow, red) = fruits

print(green)
print(yellow)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])




thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


tuple1 = ("a", "b" , "c")
tuple2 = (1,)

tuple3 = tuple1 + tuple2
print(tuple3)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)



"""-----------Python Sets----------------"""


myset = {"apple", "banana", "cherry"}

#A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry", "apple"}
#iki eleman alamaz, index yok
print(thisset)
print(len(thisset))


thisset = {"apple", "banana", "cherry"}

print(len(thisset))


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


thisset = {"apple", "banana", "cherry","orange"}

for x in thisset:
  print(x)


#Once a set is created, you cannot change its items, but you can add new items.

thisset = {"apple", "banana", "cherry"}

thisset.add("orange") # append olmuyor

print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
# rastgele yeni bir set oluşuyor index yok
print(thisset)


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


thisset = {"apple", "banana", "cherry"}

x = thisset.pop()
#son elemanı kaldırmak için
print(x)

print(thisset)



thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) # update ile aynı
print(set3)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
#ortak elemanı alıyor sete özgü
print(x)  


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
#z  diye yeni set oluşur
print(z)



x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
#aynı olanları çıkaeıyor
print(x)

"""---------------Python Dictionary-----------------"""


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

x = thisdict.keys()
y = thisdict.values()
z = thisdict.items() #The items() method will return each item in a dictionary, as tuples in a list.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) 

car["color"] = "white"

print(x) 


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #

car["year"] = 2020

print(x) 



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
thisdict.update({"color": "red"})
x = thisdict.items()

print(thisdict)
print(x)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}  # son itemi
thisdict.popitem()
print(thisdict)


for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])
#aynı outputu veriyor.
for x in thisdict.values():
  print(x)

for x, y in thisdict.items():
  print(x, y)



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
#aynı
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)



myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}









