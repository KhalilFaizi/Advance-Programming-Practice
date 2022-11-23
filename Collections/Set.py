set1 = {1,3,5,7,7,9,11,13}
set2 = {2,4,6,8,7,10,"khalil",12,14}


print(set1)
set1.add("khalil")
print(set1)
# set1.clear()
# print(set1)
print(set1.difference(set2))
# set1.difference_update(set2)
# print(set1)
print(set1.issubset(set2))


print(set1.issuperset(set2))


# print(set1.intersection(set2))
# set1.intersection_update(set2)
# print(set1)


print(set1.isdisjoint(set2))

# set1.remove("khalil")
# print(set1)


set1.pop()
print(set1)
print(set2)


# print(set1.symmetric_difference(set2))

set1.update({"khan"})
print(set1)



set1.union(set2)
print(set1)
