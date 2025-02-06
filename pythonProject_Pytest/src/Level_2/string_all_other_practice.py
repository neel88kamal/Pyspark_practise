'''

Here is a comprehensive list of questions covering various string operations, lists, tuples, regular expressions, `*args` and `**kwargs`, and other functions in Python:

### String Operations (40 Questions)
1. **Write a function to reverse a given string.**
2. **How can you find the length of a string without using the `len()` function?**
3. **Write a function that converts all characters in a string to uppercase.**
4. **How can you check if a string is a palindrome (reads the same forward and backward)?**
5. **Use the `split()` method to split a string on spaces and print the resulting list.**
6. **How can you join a list of words into a single string, separated by commas?**
7. **Write a function that counts the number of vowels in a given string.**
8. **Use the `find()` method to locate the first occurrence of the letter 'a' in a string.**
9. **How do you replace all occurrences of the substring 'dog' with 'cat' in a given string?**
10. **Write a function to remove all leading and trailing whitespace from a string.**
11. **Use the `index()` method to find the position of the first occurrence of a given substring. What happens if the substring is not found?**
12. **How can you count the number of times a specific character appears in a string using the `count()` method?**
13. **Write a function to capitalize the first character of each word in a given string.**
14. **Use the `startswith()` method to check if a string starts with a specified prefix.**
15. **Write a function to check if a string ends with a specific suffix.**
16. **How do you convert a string representation of a number to an integer?**
17. **Use the `join()` method to reverse the order of words in a sentence.**
18. **Write a function to check if a given string contains only alphanumeric characters.**
19. **How can you remove all occurrences of a specific character from a string?**
--done till ehere
20. **Write a function to sort the characters of a string in alphabetical order.**
21. **Use the `rfind()` method to find the last occurrence of a substring.**
22. **Write a function that finds all the words in a string that are longer than a specified length.**
23. **Use the `strip()` method to remove a specific character from the start and end of a string.**
24. **How can you count the number of words in a string using `split()`?** -> split -> list-> len
25. **Write a function to check if a string contains only uppercase letters.**
26. **How can you remove duplicate characters from a string?**
27. **Use the `format()` method to construct a string with dynamic values.**
28. **Write a function that repeats a string a specified number of times.**
29. **How do you convert a string to a list of characters?**

30. **Use the `zfill()` method to pad a string with leading zeros until it reaches a specified length.**
31. **Write a function to check if two strings are anagrams of each other.**
32. **Use the `partition()` method to split a string at the first occurrence of a specified separator.**
33. **Write a function that replaces the nth occurrence of a character in a string.**
34. **How do you find the longest word in a sentence?**
35. **Write a function to check if a string is a valid email address using string methods.**
36. **How can you reverse the order of words in a string?**
37. **Use the `maketrans()` and `translate()` methods to perform character replacements in a string.**
38. **Write a function that compresses a string by replacing consecutive duplicate characters with their count.**
39. **How can you check if a string contains any digits?**
40. **Use string slicing to extract every second character from a string.**
------------all done-----except few functions like format, maketrans, zfill
--rest is list, tuple, args, RE, dictionary

### List and Tuple Mixed (10 Questions)
1. **Create a list of tuples where each tuple contains a word and its length from a given list of words.**
2. **Write a function that converts a list of tuples into two separate lists (one for each element in the tuples).**
3. **How can you sort a list of tuples based on the second element of each tuple?**
4. **Write a function that zips two lists of equal length into a list of tuples.**
5. **Use list comprehension to filter out all tuples from a list of tuples where the first element is less than 10.**
6. **How can you find the index of a tuple in a list of tuples?**
7. **Write a function that converts a list of tuples into a dictionary where the first element of each tuple is the key and the second element is the value.**
8. **How can you merge two tuples to form a single tuple?**
9. **Write a function that finds the tuple with the maximum sum of elements in a list of tuples.**
10. **How can you flatten a list of tuples into a single list?**


### `*args` and `**kwargs` (10 Real-World Examples)
1. **Write a function that sums all given positional arguments using `*args`.**
2. **Create a function that accepts any number of named arguments (`**kwargs`) and prints out the key-value pairs.**
3. **Write a function to calculate the total cost of items with dynamic prices using `*args`.**
5. **Write a function to merge multiple dictionaries passed as keyword arguments.**
4. **Create a function that takes any number of student names as `*args` and their corresponding grades as `**kwargs` to calculate the average grade.**
6. **Create a function to format a string based on multiple user inputs using `*args` and `**kwargs`.**
7. **Write a function to filter out specific keys from a dictionary passed as keyword arguments.**
8. **Use `*args` in a function to accept any number of file paths and read them all.**
9. **Create a function that calculates the discount based on different criteria passed as `*args` and `**kwargs`.**
10. **Write a function to perform arithmetic operations based on multiple user inputs using `*args` for operands and `**kwargs` for operators.**

### `enumerate()` and `iter()` (Explanation and Questions)

#### Explanation of `enumerate()`
- `enumerate()` adds a counter to an iterable and returns it as an enumerated object. It is commonly used for obtaining an index and the corresponding value while looping through a list.

#### `enumerate()` Questions
1. **Write a function that uses `enumerate()` to print the index and the corresponding element of a list.**
2. **How can you start the counter at a value other than zero using `enumerate()`? Write an example that demonstrates this.**

#### Explanation of `iter()`
- `iter()` returns an iterator object. It can be used to convert an iterable (e.g., list, tuple, or string) into an iterator. It also allows custom iteration behavior by defining a sentinel value.

#### `iter()` Questions
1. **Write a function that uses `iter()` to iterate over a list and print each element.**
2. **Demonstrate the use of `iter()` with a sentinel value by reading a file line by line until an empty line is found.**

These questions cover various Python concepts and functions, offering a comprehensive practice set for different levels of programming skills.
'''
