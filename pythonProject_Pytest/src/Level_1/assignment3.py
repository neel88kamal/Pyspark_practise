#Basic Lambda Function:
# Write a lambda function that takes a number and returns its square. Test it with a number of your choice
#list comprehension
list_1=[x**3 for x in range(0,4)]
print(list_1)

def square_num(num):
    return num**2
x=[2,4,6,9,12]
exam_ple1= list(map(square_num,x))
print(exam_ple1)

#filter
exam_ple2= list(filter(square_num,x))
print(exam_ple2)

#lambda
exam_ple3 = list(filter(lambda x: (x%3==0), x))
print(exam_ple3)

#filter, lambda & map
exam_ple4 = list(map(square_num,
                   filter(lambda x: (x%3==0), x)))
print(exam_ple4)

#map & lambda
exam_ple5=list(map(lambda x:x**2, x))
print(exam_ple5)


#extract first name and last name and concotenate them and match them with email
import re
filepath="C:\\Neel\\sample_data.txt"
with open(filepath,'r') as f:
    content = f.read()

name_email=[]
valid_name_email=[]

pattern_n=re.compile(r'\b[A-Z][a-z]+\s[A-Z][a-z]+\s')
pattern_e = re.compile(r'[a-zA-Z]+@[a-z]+\.[a-z]{3}')
matches_n = pattern_n.finditer(content)
matches_e =pattern_e.finditer(content)
for match_n,match_email in zip(matches_n,matches_e):
    f_name,l_name=(match_n.group(0).strip().split())
    email=(match_email.group(0).strip())
    name_email.append((f_name,l_name,email))
    # print(match_n.group().strip())
    # print(match_email.group().strip())
    if(f_name.lower()+l_name.lower()== email.split('@')[0]):
        valid_name_email.append((f_name,l_name,email))
print('name_email',len(name_email))
print(len(valid_name_email))