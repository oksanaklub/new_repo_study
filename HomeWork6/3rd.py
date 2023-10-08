phrases = ("not at all", "madly", "passionately", "a lot", "a little", "I love you")
num_petals = int(input("Enter number of petals: "))
phrase_index = (num_petals - 1) % len(phrases)
if num_petals > 0:
    print(f'Your phrase is "{phrases[phrase_index]}"')
else:
    print("Number of petals should be more than 0")
