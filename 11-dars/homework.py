"""
Dict misollar
"""
#1
my_dict = {}
print(my_dict)

#2
my_dict['ism'] = 'Ali'
print(my_dict)

#3
my_dict = {'ism': 'Ali', 'yosh': 25}
print(my_dict)

#4
yosh = my_dict['yosh']
print(yosh)

#5
keys = my_dict.keys()
print(keys)

#6
values = my_dict.values()
print(values)

#7
my_dict.clear()
print(my_dict)

#8
my_dict = {'ism': 'Ali', 'yosh': 25}
my_dict.pop('ism')
print(my_dict)

#9
print('ism' in my_dict)

#10
my_dict = {'ism': 'Ali', 'yosh': 25}
for k, v in my_dict.items():
    print(k, v)

"""
Set misollar
"""

#1
my_set = set()
print(my_set)

#2
my_set = {1, 2, 3, 4}
print(my_set)

#3
my_set.add(5)
print(my_set)

#4
my_set.remove(2)
print(my_set)

#5
print(3 in my_set)

#6
union_set = my_set.union({6, 7})
print(union_set)

#7
inter_set = my_set.intersection({3, 4, 5})
print(inter_set)

#8
diff_set = my_set.difference({3, 4})
print(diff_set)

#9
my_set.clear()
print(my_set)

#10
my_set = {1, 2, 3}
for a in my_set:
    print(a)

"""
List misollar
"""

#1
lst = [10, 20, 30]
lst.append(40)
print(lst)

#2
lst = [10, 20, 30]
lst.extend([40])
print(lst)

#3
lst = [10, 20, 30]
lst.insert(2, 40)
print(lst)

#4
lst = [10, 20, 30, 20]
print(lst.count(20))

#5
lst = [10, 20, 30]
lst.clear()
print(lst)

#6
lst = [10, 20, 30, 40]
print(lst.index(40))

#7
lst = [10, 20, 30, 40]
lst.remove(10)
print(lst)

#8
lst = [10, 20, 30, 40]
lst.pop(2)
print(lst)

#9
lst = [30, 20, 10]
lst.reverse()
print(lst)

#10
lst = [30, 10, 40, 20]
lst.sort()
print(lst)
