"""-------------- String--------------"""

a = "Hello"
print(a)



a = "Hello, World!"
print(a[0] + a[7])

a = "Hello World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt) # boolean döndürüyor

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes. Free is in txt")
  
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# String işlemleri

b = "Hello, World!"
print(b[2:5]) # 2 den 5.karaktere kadar alıyor 5 dahil değil

b = "Hello, World!"
print(b[:5]) # en baştan 5.karaktere kadar 5 dahil değil 


b = "Hello, World!"
print(b[2:]) # 2. karakterden 2 dahil


b = "Hello, World!"
print(b[-5:-2])  # -5 dahil ,-2 dahil değil


# Modify String

a = "Hello, World!"
print(a.upper()) # tüm harfler büyük

a = "Hello, World!"
print(a.lower()) # tüm harfler küçük

a = "    Hello,World "
print(a.strip()) # The strip() method removes any whitespace from the beginning or the end:


a = "Hello, Horld!"
print(a.replace("H", "J")) # h rep j bütün h için

a = "Hello, World!"
print(a.split(","))


a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 27
txt = "My name is Semih, and I am {}"
print(txt.format(age))

print("My name is Semih, and I am {}".format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) # index atayıp cümle yapısını değiştirdi


# Escape Chr
txt = "We are the so-called \"Vikings\" from the north." # tırnak işaretine almak için
txt = "Semih \nKuşcu"
print(txt)

txt = "Semih \r Kuşcu"
print(txt) # ifadeden sonrasını almak için

txt = "Semih \tKuşcu"
print(txt)




"""---- String Metodları"""

#Python String capitalize() Method 
#The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
txt = "hello and welcome to my world."
x = txt.capitalize()
print (x)

alf = "semih kuşcu Lüleburgaz"
print(alf.capitalize())

#Python String casefold() Method
#The casefold() method returns a string where all the characters are lower case.
txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

alf = "semih kuşcu Lüleburgaz"
print(alf.casefold())

#Python String center() Method
#the center() method will center align the string, using a specified character (space is default) as the fill character.
txt = "banana"

x = txt.center(20,'1')

print(x)



#Python String count() Method

#The count() method returns the number of times a specified value appears in the string.

txt = "I love apples, apple are my favorite fruit"

y = txt.count("a")
x = txt.count("apple",5,13)

#string.count(value, start, end)
print(x)
print(y)


#Python String encode() Method
#The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
txt = "My name is Semih"

x = txt.encode()
print(x)


#Python String endswith() Method
#The endswith() method returns True if the string ends with the specified value, otherwise False.
#string.endswith(value, start, end)
txt = "Hello, welcome to my world."

x = txt.endswith("d",3,-1)

print(x)


#Python String expandtabs() Method
#The expandtabs() method sets the tab size to the specified number of whitespaces.
txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)

txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))



#Python String find() Method
"""
Definition and Usage
The find() method finds the first occurrence of the specified value.

The find() method returns -1 if the value is not found.

The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)
Syntax
string.find(value, start, end)
"""

txt = "Hello, welcome to my world."

x = txt.find("e",7,-1)

print(x)

txt = "Hello, welcome to my world."

print(txt.find("q")) # hata olarak -1 dönüyor
print(txt.index("e")) # hata olarak console da veriyor

#Python String format() Method
"""Definition and Usage
The format() method formats the specified value(s) and insert them inside the string's placeholder.

The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

The format() method returns the formatted string."""

txt = "For only {} dollars!"
print(txt.format(49))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)



"""Python String index() Method
The index() method finds the first occurrence of the specified value.

The index() method raises an exception if the value is not found.

The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found. (See example below)
string.index(value, start, end)
"""
txt = "Hello, welcome to my world."

x = txt.index("w")

print(x)

txt = "Hello, welcome to my world."

x = txt.index("e", 5, 10)

print(x)

"""Python String isalnum() Method
The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).

Example of characters that are not alphanumeric: (space)!#%&? etc.

"""

txt = "Company a12"

x = txt.isalnum()

print(x)

#Python String isalpha() Method
#The isalpha() method returns True if all the characters are alphabet letters (a-z).
#Example of characters that are not alphabet letters: (space)!#%&? etc.

txt = "CompanyX1"

x = txt.isalpha()

print(x)


#Python String isdecimal() Method
#The isdecimal() method returns True if all the characters are decimals (0-9).

txt = "\u0033" #unicode for 3

x = txt.isdecimal()

print(x)

#Python String isdigit() Method
#The isdigit() method returns True if all the characters are digits, otherwise False.
txt = "50800"

x = txt.isdigit()

print(x)

"""Python String isidentifier() Method
Definition and Usage
The isidentifier() method returns True if the string is a valid identifier, otherwise False.

A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
"""
txt = "Demo2.22_"

x = txt.isidentifier()

print(x)

#Python String islower() Method
#The islower() method returns True if all the characters are in lower case, otherwise False.

#Numbers, symbols and spaces are not checked, only alphabet characters.

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())


#Python String isnumeric() Method
#The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
txt = "22222"

x = txt.isnumeric()

print(x)


#Python String isprintable() Method
#The isprintable() method returns True if all the characters are printable, otherwise False.

txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)

#Python String isspace() Method
#The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
txt = "      "

x = txt.isspace()

print(x)

txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)

#Python String isupper() Method
#The isupper() method returns True if all the characters are in upper case, otherwise False
txt = "THIS IS NOW!"

x = txt.isupper()

print(x)

#python String join() Method

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

my= "Semih Kuşcu"
x = '-'.join(my)
print(x)

#Python String lower() Method
#The lower() method returns a string where all characters are lower case.

txt = "Hello my FRIENDS"

x = txt.lower()

print(x)

#Python String replace() Method
#The replace() method replaces a specified phrase with another specified phrase.
#string.replace(oldvalue, newvalue, count)

txt = "I like bananas"

x = txt.replace("a", "*")

print(x)

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 1)

print(x)

#Python String split() Method
#The split() method splits a string into a list.

#You can specify the separator, default separator is any whitespace

txt = "welcome to the jungle"

x = txt.split()

print(x)

txt = "hello, my name is Peter, I am 26 years old"

x = txt.split("e")

print(x)

txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)


#Python String splitlines() Method


txt = "Thank you for the music\nWelcome to the jungle\n Hello"

x = txt.splitlines()

print(x)

#Python String startswith() Method
#The startswith() method returns True if the string starts with the specified value, otherwise False
#string.startswith(value, start, end)
txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)


#Python String strip() Method
#Remove spaces at the beginning and at the end of the string:
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")


#Python String swapcase() Method
#e swapcase() method returns a string where all the upper case letters are lower case and vice versa.
txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)

#Python String title() Method
#The title() method returns a string where the first character in every word is upper case. Like a header, or a title

txt = "Welcome to my world"

x = txt.title()

print(x)


#Python String upper() Method
#The upper() method returns a string where all characters are in upper case.
txt = "Hello my friends"

x = txt.upper()

print(x)