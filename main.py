import Translater  as t
lang = input('Write to lang to which you want to translate(ru/eng): ')
text_for_test = input('Write the text which need to change: ')

translate = t.Translater(lang)
ans = translate.translate(text_for_test)
<<<<<<< HEAD
print(f'We change your text. Your new text: {ans}')
=======
print(f'We change your text. Your new text: {ans}')
>>>>>>> 5f39cf92d31aca37c5955ba97b3196930f329756
