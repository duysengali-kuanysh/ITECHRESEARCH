price = float(input("Тауар бағасы: "))
age = int(input("Жасыңыз: "))

if age < 0 or price < 0:
    print("Қате мәлімет")
else:
    if age < 7:
        price *= 0.5
    elif age <= 17:
        price *= 0.8
    elif age >= 60:
        price *= 0.7

    # Жас бойынша жеңілдіктен кейінгі баға 100 000 теңгеден асса,
    # оған қосымша 10% жеңілдік беріледі.
    if price > 100000:
        price *= 0.9

    print("Соңғы баға:", price, "теңге")
