'''
### Regular Expression (15 Intermediate-Level Questions)
1. **Write a regular expression to validate an email address.** ---already done in stringsolution.py
2. **How can you use regular expressions to find all the words that start with a capital letter in a string?**
3. **Write a regex pattern to match all dates in the format `dd/mm/yyyy`.**
4. **Use regular expressions to remove all non-alphanumeric characters from a string.**
5. **Write a function to find all the phone numbers in a given text using regex.**
6. **How can you split a string based on multiple delimiters using regular expressions?**
7. **Write a regex pattern to match a URL in a text.**
8. **How do you use regular expressions to replace all occurrences of a pattern in a string with another string?**
9. **Write a function to extract the domain name from a URL using regex.**
10. **How can you use regular expressions to validate a password that must contain at least one uppercase letter, one lowercase letter, one digit, and one special character?**
11. **Write a regular expression to find all the hexadecimal numbers in a string.**
12. **Use regex to extract all the hashtags from a given string.**
13. **Write a regex pattern that matches all sequences of digits followed by letters (e.g., "123abc").**
14. **How can you use regular expressions to find repeated words in a string?**
15. **Write a regex pattern to match a string that contains only uppercase letters, numbers, and underscores.**
'''

#2. **How can you use regular expressions to find all the words that start with a capital letter in a string?**
import re
string_to_check="hello Are you Doing"
string_list= string_to_check.split(" ")
output_list_caps=[]
pattern=re.compile(r'^[A-Z]')
for word in string_list:
    if pattern.findall(word):
        output_list_caps.append(word)
if len(output_list_caps)>0:
    print(output_list_caps)
else:
    print(f"No words starting from caps letter")

#one method could be without using re, just check if it is isCap
string_to_check="hello How Are you Doing"
string_list= string_to_check.split(" ")
output_list_caps=[]
for words in string_list:
    if words.istitle():
        output_list_caps.append(words)
print(output_list_caps)


#4. **Use regular expressions to remove all non-alphanumeric characters from a string.**
string_to_update = "hello@#are "
new_String=""
for i in string_to_update:
    if i in list(re.compile(r'[a-z0-9A-Z]').finditer(string_to_update)):
        new_String=new_String+i
print(new_String)
#this code is not working in exact manner


import re
def remove_non_alphanumeric(input_string):
    # Use re.sub() to replace all non-alphanumeric characters with an empty string
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', input_string)
    return cleaned_string

# Example usage
string_to_update = "hello@#are "
new_string = remove_non_alphanumeric(string_to_update)
print(new_string)


#8. **How do you use regular expressions to replace all occurrences of a pattern in a string with another string?**
input_string_1="hello i am again hello"
changed_string_1=re.sub("hello","how",input_string_1)
print(changed_string_1)


