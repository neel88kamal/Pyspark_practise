import re
def validate(str):
    pat= r'^[a-z]+[@!#$%]+\d+'
    matches = re.search(pat, str)
    print(matches)
    if matches:
        return True
    else:
        return False


print(validate('bcd#@345AS'))
