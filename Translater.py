class Translater:
    def __init__(self, language):
        self.language = language
    
    def translate(self, text):
        translate_letters = {
        'q':'й',
        'w':'ц',
        'e':'у',
        'r':'к',
        't':'е',
        'y':'н',
        'u':'г',
        'i':'ш',
        'o':'щ',
        'p':'з',
        '[':'х',
        ']':'ъ',
        'a':'ф',
        's':'ы',
        'd':'в',
        'f':'а',
        'g':'п',
        'h':'р',
        'j':'о',
        'k':'л',
        'l':'д',
        ';':'ж',
        'z':'я',
        'x':'ч',
        'c':'с',
        'v':'м',
        'b':'и',
        'n':'т',
        'm':'ь',
        ',':'б',
        '.':'ю',
        ' ':' '
    }
        
        if self.language == 'ru':
            letter_in_list = []
            for i in list(text):
                if i.isupper():
                    letter_in_list.append(translate_letters[i.lower()].upper())
                else:
                    letter_in_list.append(translate_letters[i])
            ans = ''.join(letter_in_list)
        else:
            letter_in_list = []
            for i in list(text):
                for key, value in translate_letters.items():
                    if i.lower() == value and i.isupper():
                        letter_in_list.append(key.upper())
                    elif i == value and not i.isupper():
                        letter_in_list.append(key)
            ans = ''.join(letter_in_list)

        return ans