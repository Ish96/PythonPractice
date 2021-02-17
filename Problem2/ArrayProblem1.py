n = int(input("Enter the number:"))
ls = []
mul = 1
if n < 4:
    print("Invalid Input")
else:
    print("Enter" + str(n) + "numbers:")
    for i in range(n):
        ls.append(int(input()))
    ls.sort()
    for i in range(4):
        mul = mul * ls[i]
    print(mul)
print("Are you hungry?")
