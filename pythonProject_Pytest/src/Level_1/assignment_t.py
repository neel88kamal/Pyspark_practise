from nltk.translate.ribes_score import find_increasing_sequences

# Example 2 >
nums = [3,2,4,9,10]
target = 13
# Output: [1,2]

# nums = [2,7,11,15]
# target = 9
output = []
def find_indices(list1,sum1):
    for i in range(len(list1)-1):
        if list1[i]+list1[i+1] == sum1:
           output.append(i)
           output.append(i+1)
find_indices(nums,target)
print(output)