list1 = [1,3,3,1,4,5,6,7,5,6,7]

set1 = set()


for item in list1:
    if item in set1:
        set1.remove(item)
    else:
        set1.add(item)

print(list(set1)[0])