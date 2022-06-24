"""-------------KOŞUL Durumları------------------"""


a = 55
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
else:
    print("a is greater than b ")
    
    
    
    
    
a = 2
b = 330
print("A") if a > b else print("B")


a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
    
"""--------------While loops---------------"""   

sums = 0; 
toplam = []
i = 0
while i < 10:
  print(i)
  i += 1
  sums=i+sums
  toplam.append(sums)  
print(sums)
print(toplam)


  
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1    
  
    
i = 0
while i < 6:
  i += 1
  if i == 3: # 3 ü atla devam et
    continue
  print(i)
    
  
"""--------------For Loops------------""" 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
# 2 si arasında print in kullanım yerinden dolayı fark var
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)    
  
    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 
    
  
    
for x in range(6): #0 1 2 3 4 5
  print(x)  
    
for x in range(2, 30, 3):
  print(x)
  
  
  
for x in range(6):
  if x == 2: break # 6'dan küçük değerlerde else e geçmez
  print(x)
else:
  print("Finally finished!")
  
  
  
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 
  
 
























