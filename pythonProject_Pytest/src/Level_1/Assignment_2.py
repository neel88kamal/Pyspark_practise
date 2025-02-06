#from xlwings.mac_dict import enums

subjects = ['SOM', 'C programming', 'Algoriths', 'System Design',
            'Python Programming', 'Logic Gate', 'DBMS', 'Computer Networks',
            'Data Structures', 'Unix', 'Distributed Computing', 'Signal and Systems', 'Ethics']

print(list(enumerate(subjects)))
y=[(x,subjects[x]) for x in range(len(subjects))]
print(y)

# a,b= y[0]
# print(a,b)

for m,n in enumerate(subjects):
    print(m,n)

print(subjects.index("DBMS"))

my_tuple=(1,[2,3])
print(my_tuple)
my_tuple[1].append(4)
print(my_tuple)


#find 2nd largest number of a list
list_1 = [20,44,59,40,99,151, 199, 199]
#first remove duplicate, sort it and then find -2 element
print(list(sorted(set(list_1))))
print(f"second largest number of list_1 is: {list(sorted(set(list_1)))[-2]}")

#print numbers which has 3 in them between 1 to 20
for i in range(1, 20):
    if '3' in str(i):
        print(i,end=",")

print()
#example of args, kwargs and dictionary, tuple, set
#exercises on these is pending


#list comprehension complex question
tup12 = [(x1,y1) for x1 in range(0,4) for y1 in range(0,4)]
print(tup12,'\n', len(tup12))

#dictionary comprehension

#sort dictionary by key
dict_12 ={"key1":12,"name":92,"akey1":112}
print("keys are: ",dict_12.keys())
print("items are: ",dict_12.items())
print("values are: ",dict_12.values())
print(sorted(dict_12))
mykeys=list(dict_12.keys())
print(mykeys)
mykeys.sort()
print(mykeys)
sd = {i: dict_12[i] for i in mykeys}
print(sd)

d = {2: 56, 100: 2, 3: 323}
print("Dictionary", d)

# Sorting key-value pairs by value, and by key if values are the same
sorted_items = sorted(d.items(), key=lambda kv: (kv[1], kv[0]))
print(sorted_items)

list_r= [2,3,4,5,6,7,2,3,4]
list_r.remove(2)
print(list_r)

#sort a dictionary without using sorted function



