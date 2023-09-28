random_list = ['Tst', 'aBc', 'TEST', 'Hello', 'neW']
everything_in_upper_case = ' '.join(random_list).upper()
transfered_string_to_list = everything_in_upper_case.split()
print(f'Here is example of the sorted list {sorted(transfered_string_to_list)}')
