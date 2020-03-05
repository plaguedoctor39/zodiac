def zodiac(month, day):
    if (month.lower() == "декабрь" and day >= 22) or (month.lower() == "январь" and day <= 19):
        print("Козерог")
    elif (month.lower() == "январь" and day >= 20) or (month.lower() == "февраль" and day <= 18):
        print("Водолей")
    elif (month.lower() == "февраль" and day >= 19) or (month.lower() == "март" and day <= 20):
        print("Рыбы")
    elif (month.lower() == "март" and day >= 21) or (month.lower() == "апрель" and day <= 19):
        print("Овен")
    elif (month.lower() == "апрель" and day >= 20) or (month.lower() == "май" and day <= 20):
        print("Телец")
    elif (month.lower() == "май" and day >= 21) or (month.lower() == "июнь" and day <= 20):
        print("Близнецы")
    elif (month.lower() == "июнь" and day >= 21) or (month.lower() == "июль" and day <= 22):
        print("Рак")
    elif (month.lower() == "июль" and day >= 23) or (month.lower() == "август" and day <= 22):
        print("Лев")
    elif (month.lower() == "август" and day >= 23) or (month.lower() == "сентябрь" and day <= 22):
        print("Дева")
    elif (month.lower() == "сентябрь" and day >= 23) or (month.lower() == "октябрь" and day <= 22):
        print("Весы")
    elif (month.lower() == "октябрь" and day >= 23) or (month.lower() == "ноябрь" and day <= 21):
        print("Скорпион")
    elif (month.lower() == "ноябрь" and day >= 22) or (month.lower() == "декабрь" and day <= 21):
        print("Стрелец")

month = input("Введите месяц: ")
day = int(input("Введите число: "))
zodiac(month, day)