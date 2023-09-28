word_inside_list = [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]]
only_word = word_inside_list[6][3][0]
print(f'Take out the word {only_word} from list')

word_again_list = only_word.split()
print(f'Taking the word "{only_word}" into the list {word_again_list}')
