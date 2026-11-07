year = int(input("Жылды енгізіңіз: "))

if year % 400 == 0:
    print("Кібісе жыл")
elif year % 100 == 0:
    print("Кібісе жыл емес")
elif year % 4 == 0:
    print("Кібісе жыл")
else:
    print("Кібісе жыл емес")
