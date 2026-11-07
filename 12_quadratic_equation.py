import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Шексіз көп шешім")
        else:
            print("Шешімі жоқ")
    else:
        print("x =", -c / b)
else:
    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("x1 =", x1)
        print("x2 =", x2)
    elif D == 0:
        print("x =", -b / (2 * a))
    else:
        print("Нақты түбір жоқ")
