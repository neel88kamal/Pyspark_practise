list1 = [60, 70, 45, 90, 3, 100]
sorted_list = []
# first_element = 0
for i in range(len(list1)):
    for j in range(0, len(list1)-1):
        if list1[j]> list1[j+1]:
            list1[j],list1[j+1] = list1[j+1], list1[j]
print(list1)


# Dictionary to sort
my_dict = {'b': 3, 'a': 101, 'c': 2}

# Sorting by values
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print("Sorted by values:", sorted_by_values)

# Sorting by keys
sorted_by_key = dict(sorted(my_dict.items()))

print("Sorted by key:", sorted_by_key)


