'''
Here are 30 questions that cover various Python dictionary concepts, including dictionary functions like `items()`, `values()`, `get()`, `update()`, `pop()`, and dictionary comprehension:

### Basic Operations
1. **Create a dictionary that contains the following key-value pairs: `'name': 'Alice'`, `'age': 25`, and `'city': 'New York'`. Print the dictionary.**

2. **How do you access the value associated with the key `'age'` in the dictionary? What will happen if the key does not exist?**

3. **Add a new key-value pair `'country': 'USA'` to the existing dictionary and print the updated dictionary.**

4. **Update the value of the key `'city'` to `'Los Angeles'` and print the dictionary.**

### Dictionary Methods
5. **Write a function to check if a key exists in a dictionary. Test it with a key that is present and one that is not.**

6. **Use the `get()` method to safely access a key that may or may not be in the dictionary. Show how you can provide a default value if the key is not found.**

7. **Write a function that removes a key-value pair from a dictionary using the `pop()` method and returns the removed value. Test it with a key that is in the dictionary and one that is not.**

8. **Use the `popitem()` method to remove the last key-value pair from a dictionary. What does this method return?**

9. **Use the `items()` method to iterate through all key-value pairs in a dictionary and print them.**

10. **Write a function that counts how many keys are in a dictionary by using the `len()` function.**

### Merging and Updating Dictionaries
11. **Create two dictionaries: `dict1 = {'a': 1, 'b': 2}` and `dict2 = {'b': 3, 'c': 4}`. Merge them using the `update()` method and explain how conflicts are handled.**

12. **Merge two dictionaries using dictionary unpacking (`{**dict1, **dict2}`). How is it different from using the `update()` method?**

### Iterating Over Dictionaries
13. **Write a function to find the sum of all values in a dictionary where the values are numbers. Use the `values()` method.**

14. **Use the `keys()` method to iterate over all the keys in a dictionary and print them in uppercase.**

15. **Create a dictionary of student names and their scores, then write a function that finds the student with the highest score.**

### Dictionary Comprehensions
16. **Create a dictionary comprehension that maps each number from 1 to 5 to its square (e.g., `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}`).**

17. **Given a list of words, create a dictionary comprehension that maps each word to its length.**

18. **Use a dictionary comprehension to invert the keys and values of a dictionary (i.e., make the original values the keys and the original keys the values).**

19. **Create a dictionary comprehension that filters out all key-value pairs where the value is not divisible by 2 from a given dictionary.**

20. **Write a dictionary comprehension to create a dictionary of squares only for even numbers between 1 and 10.**

### Advanced Operations
21. **Write a function to combine two dictionaries. If they have common keys, the values should be summed.**

22. **Given a dictionary where the values are lists, write a function to flatten the dictionary into a list of all the values.**

23. **Write a function that takes a dictionary and returns a new dictionary with the keys sorted alphabetically.**

24. **How can you use the `setdefault()` method to add a key-value pair only if the key does not already exist in the dictionary? Provide an example.**

25. **Use the `fromkeys()` method to create a dictionary with keys from a list, all having the same initial value.**

### Deleting and Clearing Dictionaries
26. **Write a function to clear all items from a dictionary using the `clear()` method. What does the dictionary look like afterward?**

27. **Write a function that removes multiple keys from a dictionary. Accept the dictionary and a list of keys to remove as arguments.**

### Nested Dictionaries
28. **Create a nested dictionary to represent a phone book, where the keys are names and the values are dictionaries containing 'phone' and 'email' information.**

29. **Write a function to add a new contact to the nested phone book dictionary.**

30. **Given a nested dictionary, write a function to flatten it into a single-level dictionary using a custom separator for nested keys. For example, `{'name': 'Alice', 'contact.phone': '123-456-7890'}`.**

These questions should cover a wide range of dictionary-related concepts, from basic operations to more advanced manipulations, including dictionary comprehensions and nested structures.
'''

