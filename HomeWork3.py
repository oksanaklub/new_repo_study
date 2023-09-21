# 1. Написати програму, в якій необхідно видалити всі вказані літери з стрінги(string)
# Стрінгу(string) і літеру ввести з клавіатури.
basic_text = 'One two or something else'
replaced_char_text = basic_text.replace('o', '', 3)
print(replaced_char_text)

# 2. Написати програму, яка візьме string і в кожному слові замінить першу літеру на велику.
# string ввести з клавіатури
# Приклад: "This is some test STRING"
# Відповідь: "This Is Some Test String"
some_text_before_changes = 'This text is awesome.'
updated_text_with_upper_case = some_text_before_changes.title()
print(updated_text_with_upper_case)

# 3. Напишіть програму яка перевертає стрінгу
reversed_string = 'one two three'
print(reversed_string[::-1])

# 4. Напишіть програму яка приймає на вхід 2 стрінги та порівнює їх
word1 = 'cat'
word2 = 'dog'
print(word1 == word2, word1 != word2)

# 5.Напишіть програму яка візьме стрінг та повторить її задану кількість раз.
# До прикладу ми маємо стрінгу 'abc' та число 3. Результатом роботи програми має бути "abcabcabc"
random_text = 'This text is random. '
repeat_number = 3
repeated_random_text = random_text * repeat_number
print(repeated_random_text)

# 6. Написати програму для підрахунку конвертації валюти:
# UAH --> USD
# доларів США --> грн
# UAH --> EUR
# євро --> грн

USD = float('37.82')
EUR = float('40.70')
UAH_cash_amount = 345
USD_cash_amount = 15
EUR_cash_amount = 10
USD_result = round(UAH_cash_amount/USD)
EUR_result = round(UAH_cash_amount/EUR)
UAH_result_usd = USD_cash_amount * USD
UAH_result_eur = EUR_cash_amount * EUR
from_currency = 'UAH'
to_currency = 'USD'
print(USD_result, EUR_result, UAH_result_usd, UAH_result_eur)
