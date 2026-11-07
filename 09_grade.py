score = int(input("Ұпай енгізіңіз: "))

if score < 0 or score > 100:
    print("Қате ұпай")
elif score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
elif score >= 50:
    print("D")
else:
    print("F")
