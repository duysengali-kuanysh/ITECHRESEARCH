a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a <= 0 or b <= 0 or c <= 0:
    print("Қате қабырға ұзындығы")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Үшбұрыш құрылмайды")
elif a == b == c:
    print("Теңқабырғалы")
elif a == b or a == c or b == c:
    print("Теңбүйірлі")
else:
    print("Әртүрлі қабырғалы")
