# Creation of Array 
# importing "array" for array creations
import array as arr
 
# creating an array with integer type
a = arr.array('i', [1, 2, 3])
  
# creating an array with double type
b = arr.array('d', [2.5, 3.2, 3.3])

a.append(6)
# a.clear()
# print(a.__len__())
# c =a.count(6)
# print(c)
a.insert(2, 6)
# print(a.index(6))
a.reverse()
a.remove(1)
a.pop()
print(type(a))
print(a.buffer_info())



# for i in a:
#     print(i)

# for i in b:
#     print(i)





 




