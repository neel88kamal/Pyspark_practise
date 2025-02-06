#Python program to count the frequency of each element in a list.
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
#count how many times each number is repeated, output seems like a dict i.e 1:2, 2:3

sorted_nums = sorted(nums)
print("sorted given list looks like: ",sorted_nums)
dict1={}
key=0
for i in range(len(sorted_nums)):
    if sorted_nums[i]==key:
        pass
    else:
        dict1[sorted_nums[i]]=sorted_nums.count(sorted_nums[i])
        key=sorted_nums[i]
print(f"element and their count are: ",dict1)
