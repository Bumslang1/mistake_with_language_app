import Translater  as t
lang = input('Write to lang to which you want to translate(ru/eng): ')
text_for_test = input('Write the text which need to change: ')

translate = t.Translater(lang)
ans = translate.translate(text_for_test)
print(f'We change your text. Your new text: {ans}')