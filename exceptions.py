try:
    print(x)
except:
    print("exception occured")
#using else
try:
    print("hello")
except:
    print("exception occured")
else:
    print("nothing went wrong")
#alternative
try:
    print("str")
except Exception as e:
    print(f"error is occured:{e}")
#finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
#raise exception
x=-1
if x<0:
   raise Exception("errorr occured")
