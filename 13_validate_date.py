day = int(input("Күн: "))
month = int(input("Ай: "))
year = int(input("Жыл: "))

if year <= 0 or month < 1 or month > 12:
    print("Қате күн")
else:
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False

    if month == 2:
        max_day = 29 if leap else 28
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 31

    if 1 <= day <= max_day:
        print("Дұрыс күн")
    else:
        print("Қате күн")
