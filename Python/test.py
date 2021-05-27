import copy

a = {1:[1,3], 2:[2], 3:[1,2]}
a2 = copy.copy(a)

for i in a:
    values = a[i]
    for val in values:
        values2 = a[val]
        for val2 in values2:
            if val2 not in values:
                a2[i].append(val2)
