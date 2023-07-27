class Translater:
    def __init__(self, language):
        self.language = language
    
    def translate(self, text):
        translate_letters_from_us = {
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
                    letter_in_list.append(translate_letters_from_us[i.lower()].upper())
                else:
                    letter_in_list.append(translate_letters_from_us[i])
            ans = ''.join(letter_in_list)
        return ans