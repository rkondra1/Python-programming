import re

string = "kjsnfwjkfnjksdv  Rajesh njknkjn Rajesh"

# check if 'Python' is at the beginning
match = re.search('Rajesh', string)

if match:
    print(match.group())
