from pyarrow import dictionary

print(list('hello'))

d = {}
d[1] = 1
d['1'] = 2
d[1] +=1

sum = 0
for k in d:
    sum +=d[k]

print(sum)


dictionary={'one':'two', 'three':'one', 'two':'three'}
v = dictionary['one']
print(v)

for k in range(len(dictionary)):
    v = dictionary[v]

print(v)

str1= 'Peter'
str2 = str1[:]
print(str2)