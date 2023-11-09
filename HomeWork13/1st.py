import re
from examples import text_to_search, urls

abc = re.compile(r'abc')
phone_numbers = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
phone_numbers_800_900 = re.compile(r'[89]00-\d{3}-\d{4}')
mr_name = re.compile(r'Mr\.?\s[A-Z]\w*')
emails = re.compile(r'\w+@\w+\.\w+')
url = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')


matchers = abc.finditer(text_to_search)
for match in matchers:
    print(match)

matchers2 = phone_numbers.findall(text_to_search)
print(matchers2)

with open('data.txt', 'r') as file:
    content = file.read()
    matchers3 = phone_numbers.findall(content)
    print(matchers3)

with open('data.txt', 'r') as file:
    content = file.read()
    matchers4 = phone_numbers_800_900.findall(content)
    print(matchers4)

matchers5 = mr_name.findall(text_to_search)
print(matchers5)

with open('data.txt', 'r') as file:
    content = file.read()
    matchers6 = emails.findall(content)
    print(matchers6)

matchers7 = url.finditer(urls)
for el in matchers7:
    print(el.group())
