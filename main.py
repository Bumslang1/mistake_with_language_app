import Translater  as t

text_for_test = 'dkfl yt pyftn ybxtuj'

translate = t.Translater('ru')
ans = translate.translate(text_for_test)
print(ans)
