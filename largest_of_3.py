a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))

if a == b and b == c:
    print("The numbers are equal")
elif a >= b:
    print("A is the winner")
elif b >= c:
    print("B is the winner")
else:
    print("C is the winner")