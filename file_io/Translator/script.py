from translate import Translator
translator = Translator(to_lang="ja")

try:
    with open('test.txt', 'r') as my_file:
        translation = translator.translate(my_file.read())
        print(translation)
except:
    print('Error!')