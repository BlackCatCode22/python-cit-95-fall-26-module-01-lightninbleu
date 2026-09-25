total = 0
count = 0

while True:
    user_input = input("Enter an integer (or 'done' to finish): ")
    if user_input == "done":
        break
    try:
        value = int(user_input)
    except ValueError:
        print("Invalid input")
        continue
    total += value
    count += 1

if count > 0:
    average = total / count
else:
    average = 0

print("Total:", total)
print("Count:", count)
print("Average:", average)
