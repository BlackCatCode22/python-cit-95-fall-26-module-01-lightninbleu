numbers = []

while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input == "done":
        break
    try:
        value = float(user_input)
    except ValueError:
        print("Invalid input")
        continue
    numbers.append(value)

if numbers:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
else:
    print("No numbers entered")
