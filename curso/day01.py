def calculate_years_until_40(age):
    years_until_40 = 40 - age
    return years_until_40

name = input("What is your name? ")
age = int(input("What is your age? "))
if age >= 40:
    print(f"Hello, {name}! You are already 40 or older.")
elif age < 0:
    print(f"Hello, {name}! Please enter a valid age.")
else:
    years_left = calculate_years_until_40(age)
    print(f"Hello, {name}! You have {years_left} years left until you are 40.")
