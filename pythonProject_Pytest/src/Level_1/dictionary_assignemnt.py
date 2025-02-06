
#use of sorted function on dictionary

#use of sorted with list
#use of sorted on list of list
#on list of dictionary
#idea is how to sort them
#how to sort dictionary by key and by value

# dict1={{'city':'Bangalore', 'per_capita_income':70730}, {'city':'Mumbai', 'per_capita_income':72730}}

dict_student={'Ram':50, 'Abhishek':100, 'Zia':45}
#sort this student dictionary, using key
print(sorted(dict_student.items()))

#sort this student dictionary, using value
print(sorted(dict_student.items(),key=lambda i:i[1]))


li = [{'city':'Bangalore', 'per_capita_income':70730},
      {'city':'Mumbai', 'per_capita_income':72730},
      {'city':'Chennai', 'per_capita_income':69730},
      {'city':'Hyderabad', 'per_capita_income':71444}
     ]
#sort this list of dictionary based on city and
# sort it on basis on per_capita
print(sorted(li, key=lambda i:i['city']))

print(sorted(li, key=lambda i:i['per_capita_income']))