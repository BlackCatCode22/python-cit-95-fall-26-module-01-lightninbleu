num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))

def detailed(num1, num2, num3, largest, winner):
    print("You enter three numbers", num1, num2, "and", num3)
    print("Your input was processed and the largest number you entered was", largest," which belonged to an integer variable named",winner)

if num1 == num2 and num2 == num3:
    print("all numbers are equal")
elif num1 >= num2:
   largest = num1
   winner =  "num1"

elif num2 >= num3:
   largest = num2
   winner = "num2"
else:
    largest = num3
    winner = "num3"

detailed(num1, num2, num3, largest, winner)
