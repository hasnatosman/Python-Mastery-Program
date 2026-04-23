# String Manipulation
# Strings are essential for text processing.
# String indexing
# String slicing
# String methods:lower(),upper(),strip(),replace(),split(),join()
# Searching within strings
# String formatting

# Practice:
# Email parser
# Text cleaner
# Password validator


# String manipulation
# string indexing: access individual characters using index

text = 'Python'
print(text[0])
print(text[1])
print(text[-1])

# string slicing: get a sub string

text = 'Python Programming'

print(text[0:6])          # format: string[start:end:step]
print(text[7:])
print(text[:6])
print(text[::2])

# String methods

text = 'Hello Python'

print(text.lower())
print(text.upper())

text = ' Bangladesh      '

print(text.strip())    # remove spaces from both side

text = 'I love java'
new_text = text.replace('java','python')
print(text)
print(new_text)

text = 'Apple,Banana, Mango'
fruits = text.split(',')
print(fruits)

word = ['Python', 'is', 'Fun.']
sentence = ' '.join(word)
print(sentence)

# Searching in string

text = 'Python programming'

print('Python' in text)
print(text.find('programming'))
print(text.count('m'))

# in: check existence
# find(): returns index(-1 if not found)
# count(): number of matches


# string formating

name = 'Hasnat'
age = 25

message = f'My name is {name} and I am {age} years old.'
print(message)

# Practice
# Email parser

def parse_email(email_address: str) -> dict:
    username, domain = email_address.split('@')

    return{
        'username': username,
        'domain': domain
    }

# test
result = parse_email('user123@gmail.com')
print(result)

# text cleaner
def clean_text(raw_text: str) -> str:
    cleaned_text = raw_text.strip().lower()
    cleaned_text = cleaned_text.replace(',', '')

    return cleaned_text

text = '  Hello, World, Python  '
print(clean_text(text))
