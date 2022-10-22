number = list()
letters =["a","b","a",4,"a","f"]
new_letters = letters[1:4]
new_letters_with_double_colon =letters[1::4]
number.append("khalil")
number.insert(1,4)
number.append("Faizi")
number.append(1)



print(new_letters)
print(new_letters_with_double_colon)
print(number[2])
print(number)
new_list =letters.copy() 
letters.clear()
print(letters)
print(new_list)
print(new_list.count("a"))
new_list.extend(number)
print(new_list)
print(new_list.index(4))
new_list.pop(5)
print(new_list)
new_list.remove(4)
print(new_list)
new_list.reverse()
print(new_list)
new_list.remove("khalil")
print(new_list)


