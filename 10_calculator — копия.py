a = float(input("a = "))
b = float(input("b = "))
op = input("Операция (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Нөлге бөлуге болмайды")
else:
    print("Қате операция")
