x = float(input("Enter temperature : "))
u = input("Enter Unit (c/f) : ")
if u == "c":
    temp = float((9 * x / 5) + 32)
    print("Temperature is ", str(temp), "F")
elif u == "f":
    temp = 5 * (x - 32) / 9
    print("Temperature is ", str(temp), "C")
else:
    print("Wrong unit")