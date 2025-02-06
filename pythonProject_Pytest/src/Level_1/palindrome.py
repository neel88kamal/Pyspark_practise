#Write a Python program to check if a string is a palindrome.

def check_palindram(string1):
    revers_st=[]
    lenth=len(string1)
    while(lenth>=1):
        #print(string1[lenth-1])
        revers_st.append(string1[lenth-1])
        lenth-=1
    return "".join(revers_st)

in_string="teet"
st=check_palindram(in_string)
if st ==in_string:
    print(f"string entered {in_string} is a palindrome")
else:
    print(f"{in_string} is not a palindrome")

def check_palindram_1(str):
    rev_str= "".join(list(reversed(str)))
    if str == rev_str:
        print(f"{str} is a palindrome")
    else:
        print("not a palindrome")

str="aaa"
check_palindram_1(str)