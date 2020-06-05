rus_en = {"а": 'a', "б": 'b', "в": 'v', "г": 'g', "д": 'd', "е": 'e', "ё": 'e',
          "ж": 'zh', "з": 'z', "и": 'i', "й": 'y', "к": 'k', "л": 'l', "м": 'm',
          "н": 'n', "о": 'o', "п": 'p', "р": 'r', "с": 's', "т": 't', "у": 'u',
          "ф": 'f', "х": 'kh', "ц": 'ts', "ч": 'ch', "ш": 'sh', "щ": 'shch',
          "ы": 'y', "э": 'e', "ю": 'yu', "я": 'ya'}

en_rus = {'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д', 'ye': 'е', 'zh': 'ж',
          'z': 'з', 'i': 'и', 'y': 'ы', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н',
          'o': 'о', 'p': 'п', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'f': 'ф',
          'kh': 'х', 'ts': 'ц', 'ch': 'ч', 'sh': 'ш', 'shch': 'щ', 'yu': 'ю',
          'ya': 'я', 'yo': 'ё'}

consonant = 'bcdfghjklmnpqrstvw'

rus_vowels = 'еуыаоэюияъь'

def rus(sentence):
    words = [word.lower() for word in sentence.split()]
    ling = rus_en.copy()
    result_word = []
    result = []
    for word in words:
        for i, letter in enumerate(word):
            if letter == 'е' or letter == 'ё':
                if i == 0 or (i - 1) > 0 and word[i-1] in rus_vowels:
                    result_word += 'ye'
                else:
                    result_word += 'e'
            elif letter == 'ъ' or letter == 'ь':
                continue
            elif letter in '=-/.?>,!@#$@#$%^&*()':
                result_word += letter
            else:
                result_word += ling[letter]
        result.append(''.join(result_word))
        result_word = []   
    
    return ' '.join(result)


def eng(sentence):
    words = [word.lower() for word in sentence.split()]
    ling = en_rus.copy()
    result = ''
    for word in words:
        pas = False
        for index, letter in enumerate(word):
            if not pas:
                if len(word) >= index + 2:
                    if letter == 'z' and word[index + 1] == 'h':
                        result += ling.get('zh')
                        pas = True
                    elif letter == 'k' and word[index + 1] == 'h':
                        result += ling.get('kh')
                        pas = True
                    elif letter == 't' and word[index+1] == 's':
                        result += ling.get('ts')
                        pas = True
                    elif letter == 'c' and word[index + 1] == 'h':
                        result += ling.get('ch')
                        pas = True
                    elif letter == 's' and word[index + 1] == 'h':
                        if len(word) >= index + 3 and word[index:index+3] == 'shch':
                            result += ling.get('shch')
                        else:
                            result += ling.get('sh')
                        pas = True
                    elif letter == 'y' and word[index + 1] == 'u':
                        if len(word) >= index - 2 and word[index - 1] in consonant:
                            result += 'ь'
                        result += ling.get('yu')
                        pas = True
                    elif letter == 'y' and word[index + 1] == 'a':
                        if len(word) >= index - 2 and word[index - 1] in consonant:
                            result += 'ь'
                        result += ling.get('ya')
                        pas = True
                    elif letter == 'y' and word[index + 1] == 'e':
                        if len(word) >= index - 2 and word[index - 1] in consonant:
                            result += 'ь'
                        result += ling.get('ye')
                        pas = True
                    elif letter == 'y' and word[index + 1] == 'o':
                        if len(word) >= index - 2 and word[index - 1] in consonant:
                            result += 'ь'
                        result += ling.get('yo')
                        pas = True
                    else:
                        result += ling.get(letter, letter)
                        pas = False
                else:
                    result += ling.get(letter, letter)
                    pas = False
            else:
                pas = False
        result += ' '
    return result

def trans():
    sentence = input('Введите слово или предложение, которое нужно транслитерировать\n')
    if sentence[0] in rus_en.keys():
        result = rus(sentence)
    else:
        result = eng(sentence)
    print(result)

trans()
