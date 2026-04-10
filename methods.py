l=["apple","banana","mango"]
print(l[0])
l[0]="coconut"
print(l)
l[0:2]=["nuts","fruits"]
print(l)
l.insert(2,"apple")#insertion at particular place 
print(l)
l.append("brownie")
print(l)
l2=[2,3,"happy"]
l.extend(l2)#extends
print(l)
tuple=("pen","pencil")
l.extend(tuple)
print(l)
l.remove("mango")
print(l)
l.pop(1)#removing element by index
print(l)
#can use del to delete list complteley
l3=["mmjdvhc"]
del l3
#print(l3)#deleted 
l4=["jbjbdkjcbjbdj"]
l4.clear()
print(l4)#list items will be deleted list will be present
#looping
for i in range(len(l)):
    print(l[i])
#whileloop
k=["happy","sad"]
i=0
while i<len(k):
    print(k[i])
    i=i+1
#list comprehens
fruits=["banana","mango","apple","cherry","berry"]
new=[x for x in fruits if "b" in x]
print(new)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
#copy
j=l2.copy()
print(j)
i=list(l2)
print(i)
u=l2[:]
print(u)
#tuple
t=("hi",2,3)
print(t)
#set
s={1,2,"hiiii"}
for x in s:
    print(x)

print(type(s))
s.add("hlo")
print(s)
y={"yamuna"}
s.update(y)
print(s)
#dictionary
dict={
    "veh":"car",
    "year":2004
}
print(type(dict))
print(dict.values())
print(dict.keys())
print(dict.items())
#shorthand if
x=10
if x>0:print(x)
#shorthand if...else
m=20
print("bdhdbjjkj") if m>100 else print("m is lessthan 100")
#assigning values with if..else
a=30
b=20
big= a if a>b else b
print("bigger =",big)
#match
day = 8
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case _:
    print("Looking forward to the Weekend")
#while
i=1
while(i<5):
   print(i)
   i+=2