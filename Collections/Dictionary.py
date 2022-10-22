my_Str ={
    1:"khalil",
    2:"ahmad",
    3:"Faizi"
}

my_Num = { 'a':1 , 'b':2 , 'c': [5,6,7,8] ,'d': ('a','b','c')}


# print(my_Str[2])
# print(my_Num['a'])
# print(my_Num['d'])

# for i in my_Num.items():
#     print(i)

print(my_Num.values())


# my_Str.update({5:"jan"})
# print(my_Str)

# my_Num.popitem()
# print(my_Num)


# my_Num.pop('a')
# print(my_Num)



# print(my_Num.keys())
# print(my_Num.items())


print(my_Num.fromkeys('c'))

new_dict = my_Num.copy()
print(new_dict)

my_Num.clear()
print(my_Num)