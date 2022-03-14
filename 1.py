tipe_str = input("Выберите сценарий, 1 или 2:")
tipe = int(tipe_str)

if tipe == 1:
    name_str = input("Моё имя: ")
    age = input("Мой возраст: ")
    i = int
    ending = str
    age_int = int(age)
    if age_int % 10 == 1:
        ending = "год"
    elif age_int % 10 == 2 or 3 or 4:
        ending = "года"
    elif age_int % 10 == 5 or 6 or 7 or 8 or 9 or 0:
        ending = "лет"
    elif age_int == 11 or 12 or 13 or 14:
        ending = "лет"
    print("Меня зовут ", name_str, ", мне ", age_int, ending)
    print((name_str + " ")*5)
if tipe == 2:
    user_name_str = input("Введите ваше имя: ")
    user_age = input("Введите ваш возраст: ")
    user_age_int = int(user_age)

    if user_age_int < 30:
        print("Привет, ", user_name_str, ", qwerty")
    else:
        print("Здарова, ", user_name_str, ", старый, но не бесполезный))")


