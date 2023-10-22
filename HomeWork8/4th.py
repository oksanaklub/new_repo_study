result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'

char_count = {}

for char in result_link:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)
