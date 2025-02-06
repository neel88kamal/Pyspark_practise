#how will you swap two letters of a string, for ex s="abcd" , swaping s[0] with s[2] will form cbad
s="abcd"
#swapplace= input("enter two places to swap ex: 12")
#for now hardcode and replace s[0] withs[2]

def swap(string, index1, index2):
    list1 = list(string)
    list1[0],list1[2] = list1[2],list1[0]
    return "".join(list1)


s1= swap(s, 0,2)
print(s1)