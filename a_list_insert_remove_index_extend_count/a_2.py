
langs = ['Python', 'Java', 'JS', 'SQL']
user_lang = input('После какого языка вставляем: ')
i_lang = langs.index(user_lang)

langs.insert(i_lang + 1, 'C++')

print(langs)