number = int(input("Enter a number"))
condition = 0
iteration = 2
while iteration <= number/2:
    if number % iteration == 0:
        condition = 1
        break
    iteration += 1
if condition == 0:
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")