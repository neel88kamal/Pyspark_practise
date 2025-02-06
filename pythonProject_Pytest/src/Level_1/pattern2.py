# print this pattern below:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1


# or rather
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print(j, end=" ")
    print()

print("------------------")

for i in range(5,0,-1):
    for j in range(5,0,-1):
        if i>=j:
            print(j, end=" ")
    print()

print("------------------")
print("------------------")


for i in range(1,6):
    for j in range(5,0,-1):
        if i<=j:
            print(j, end=" ")
    print()
