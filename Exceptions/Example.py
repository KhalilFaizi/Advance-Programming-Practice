import sys


a=2
b=0

try:
    print(a/b)
except:
    print("Oops !" , sys.exc_info()[0])
finally:
    print("Always executed")





# User define exception handling 

class NetworkError(RuntimeError):
   def __init__(self, arg):
      self.args = arg


try:
   raise NetworkError("Bad hostname")
except NetworkError :
   print (NetworkError.args)



