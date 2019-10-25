str_ = input("Введите текст:")
str_ = list(str_)

if str_.count('f') > 1:
    lastf = str_[::-1].index('f')
    first = str_.index('f')
    print(f"First in {first}.Last in {(len(str_).lastf)}")
elif str_.count('f') == 1:
    print("Индекс буквы 'f' равен: ",str_.index('f') )