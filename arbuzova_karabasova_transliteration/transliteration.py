rus_en = {"а": 'a', "б": 'b', "в": 'v', "г": 'g', "д": 'd', "е": 'e', "ё": 'e',
          "ж": 'zh', "з": 'z', "и": 'i', "й": 'y', "к": 'k', "л": 'l', "м": 'm',
          "н": 'n', "о": 'o', "п": 'p', "р": 'r', "с": 's', "т": 't', "у": 'u',
          "ф": 'f', "х": 'kh', "ц": 'ts', "ч": 'ch', "ш": 'sh', "щ": 'shch',
          "ы": 'y', "э": 'e', "ю": 'yu', "я": 'ya'}
en_rus = {'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д', 'e': 'э', 'zh': 'ж',
          'z': 'з', 'i': 'и', 'y': 'ы', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н',
          'o': 'о', 'p': 'п', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'f': 'ф',
          'kh': 'х', 'ts': 'ц', 'ch': 'ч', 'sh': 'ш', 'shch': 'щ', 'yu': 'ю',
          'ya': 'я'}

def rus(word):
    word = word.lower()
    ling = rus_en.copy()
    if 'е' in word:
        ind = word.find('е')
    result = [rus_en.get(i, '') for i in word]
    print(''.join(result))

word = input('Введите слово, которое нужно транслитерировать\n')
if word[0] in rus_en.keys():
    rus(word)
else:
    en(word)
        
