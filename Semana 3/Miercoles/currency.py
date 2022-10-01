currency_dict = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency_input = input("Please enter a currency, eg: Euro, Dollar or Yen: ")
print(currency_dict.get(currency_input.title(), "Currency not Found"))