s= 'siemeslesss'
dict_2= dict()
#make a set which will contain distinct set of characters
set_1= set(s)
#now iterate through set_1 each character
for i in set_1:
    dict_2[i]=s.count(i)

print(dict_2)

