#creating variables
v=20
y="yamuna"
print(v)
print(y)
#casting
x=str(3)#now 3 is string '3'
u=int(3)#here 3 is int 3
z=float(3)#now it is float 3.0
print(type(x),type(u),type(z))
#assigning multiple variables
g,h,j,t="yamuna",20,3.0,2+3j
print(type(g),h,j,type(t),t.real,t.imag)
#multiple variables single value
q=w=e="yaaaaa"
print(q,w,e)
#unpack a collection
fruits=["apple","orange","mango"]
a,b,c=fruits
print(a,b,c)
#global variable
i="john"
def myfunc():
    print("hey,how are "+i)
myfunc()
#declaring same variable out and inside the function.
p = "awesome"
def myfunc():
  p = "fantastic"
  print("Python is " + p)#we get variable which is declared inside func 
myfunc()
print("Python is " + p)#outside function variable is printed
#global keyword
def myfun():
   global K
   K ="sony"
   print("happy birthday "+ K)
myfun()
print(K)
#to change a variable value and make it global 
n = "awesome"
def myfunc():
  global n
  n = "fantastic"
myfunc()
print("Python is " + n)
#random numbres
import random
print(random.randrange(1000,9000))
