text = "hello 1 one two three 15 world"
words = text.split()

for i in range(len(words) - 2):
    if words[i].isalpha() and words[i + 1].isalpha() and words[i + 2].isalpha():
        break
print(f"This '{text}'  has 3 words in line")
