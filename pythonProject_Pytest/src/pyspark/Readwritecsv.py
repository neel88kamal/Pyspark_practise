import re

email = ''' 
hello@gmail.com,
hellowhow123-5@caastle.com
neelKAMAL_123@internet.in.com
'''

pattern = re.compile(r'[a-zA-Z0-9_-]+@[a-zA-z]+(\.[a-zA-Z]+)+')
# pattern = re.compile(r'[a-zA-Z0-9._-]+@[a-zA-Z]+(\.[a-zA-Z]+)+')

matches = pattern.finditer(email)
for match in matches:
    print(match.group(0))