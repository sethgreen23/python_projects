import string

name = "chaith"
"""
message = f'Hello {name.title():s}, would you like to learn some Python today?'
print(message)
name = 'maria'
l_name = 'dridi'
full_name = f'{name:s} {l_name:s}'
print(full_name.lower())
print(full_name.upper())
print(full_name.title())

"""
quote_author = '        "eminem"               '.lstrip().rstrip().title()
quote = "the truth is you don\'t know what is going to happen tomorow. life is a crasy ride, and nothing is guaranteed."
# uppercase the message in begining or after a '.'
quote_uppercase = ""
index = 0
while (index < len(quote)):
    c = quote[index]
    flag = 0
    if index == 0:
        quote_uppercase += c.upper()
    elif c == '.':
        while (index < len(quote)):
            c = quote[index]
            alphbet = string.ascii_letters
            if c in alphbet:
                quote_uppercase += c.upper()
                break
            quote_uppercase += c.lower()
            index += 1
    else:
        quote_uppercase += c.lower()
    index += 1
# print message
quote_format = f'{quote_author:s} once said, "{quote_uppercase:s}"'
print(quote_format)
