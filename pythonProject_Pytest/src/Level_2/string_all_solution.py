#q1 Write a function to reverse a given string
str_1 = "Hello"
str_2=list(reversed(str_1))
print("".join(str_2))

#2nd method
reverse_str_1= str_1[-1::-1]
print(reverse_str_1)

#3rd method
for i in range(len(str_1)-1,-1,-1):
    print(str_1[i], end="")
print("\n")

#q2. **How can you find the length of a string without using the `len()` function?**
length_of_string=0
for i in str_1:
    length_of_string+=1
print(f"length of string is {length_of_string}")

#3. **Write a function that converts all characters in a string to uppercase.**
print(str_1.upper())

#q5. **Use the `split()` method to split a string on spaces and print the resulting list.**
str_3 = "hello how are you doing"
print(str_3.split(" "))

#q6. **How can you join a list of words into a single string, separated by commas?**
list_of_words = ["list","of","words"]
print(",".join(list_of_words))

#q7. **Write a function that counts the number of vowels in a given string.**
def vowel_count(st):
    count_to=0
    for char in st:
        if char.lower() in 'aeiou':
            count_to+=1
    return(count_to)

print(vowel_count("helloIndia"))

#q10. **Write a function to remove all leading and trailing whitespace from a string.**
str_trim=" hello how "
print(str_trim.strip())

#q40. **Use string slicing to extract every second character from a string.**
str_trim="hello how"
print(str_trim[1::2])

#q8. **Use the `find()` method to locate the first occurrence of the letter 'a' in a string.**
str_find_a = "tahis is first athen what"
print(str_find_a.find('a'))

#q9. **How do you replace all occurrences of the substring 'dog' with 'cat' in a given string?**
str_dog_replace = "Which breed of dog is best dog in world"
print(str_dog_replace.replace("dog","cat"))

#q11. **Use the `index()` method to find the position of the first occurrence of a given substring. What happens if the substring is not found?**
str_substring="hello i am to be found, am i?"
if str_substring.index("am")!=-1:
    print(f"first occur of am is there in string at {str_substring.index("am")}")
else:
    print(f"am is missing from this string {str_substring}")

#q12. **How can you count the number of times a specific character appears in a string using the `count()` method?**
str_count_times_chr = "str has many ssstringchar"
print(f"s appears {str_count_times_chr.count("s")} times in string {str_count_times_chr}")

#q13. **Write a function to capitalize the first character of each word in a given string.**
#q14. **Write a function to sort the characters of a string in alphabetical order.**
str_alpha="who is this alpha"
print("".join(sorted(set(str_alpha.replace(" ","")))))
#we had to remove blank spaces

# 14. **Use the `startswith()` method to check if a string starts with a specified prefix.**
# 15. **Write a function to check if a string ends with a specific suffix.**
print(str_alpha.startswith('w'))
print(str_alpha.endswith('a'))

#17. **Use the `join()` method to reverse the order of words in a sentence.**
print(" ".join(list(reversed(str_alpha.split()))))

print(str_alpha.isalnum()) #its bcoz string has space as well, that is why its returning false
print(str_alpha.replace(" ","").isalnum())

#19. **How can you remove all occurrences of a specific character from a string?**
#there could be multiple ways
print(str_alpha) #now task is to remove h from this string, simple replace can do this
print(str_alpha.replace("h",""))

#m-2, there can be a function, which will convert string to list by splitting. then traverse and remove character from each word and then join back
#m-3 or just a list comprehension
new_list_1= [word.replace("h","") for word in str_alpha.split(" ")]
print(" ".join(new_list_1))

#25. **Write a function to check if a string contains only uppercase letters.**
print(str_alpha.isupper())

#26. **How can you remove duplicate characters from a string?**
#in this if you have to maintain the order of the string then it becomes little difficult. #good question
print(set(str_alpha))
#29. **How do you convert a string to a list of characters?**
print(list(str_alpha.replace(" ",""))) #if not needed, dont do replace.

#33. **Write a function that replaces the nth occurrence of a character in a string.**
#good question

#35. **Write a function to check if a string is a valid email address using string methods.**
#sample email - neelsingh123@gmail.com
import re
print(f"enter a valid emailid:")
input_email=input()
pattern_email= re.compile(r'[a-zA-Z0-9_-]+@')
matches = pattern_email.finditer(input_email)
is_valid_email=False

for match in matches:
    if match.span():
        is_valid_email=True
print(f"entered email address {input_email} is a valid email :{is_valid_email}")

#but is there a string method which can identify valid email address, not really. we can write a function with lot of if and else

#39. **How can you check if a string contains any digits?**
contain_digit=False
str_to_check="do i have a digit 1"
for i in str_to_check:
    if i.isnumeric():
        contain_digit=True
print(f"string '{str_alpha}' contains a digit: {contain_digit}")

#40. **Use string slicing to extract every second character from a string.**
str_to_check="do i have a digit 1"
print(str_to_check[::2])