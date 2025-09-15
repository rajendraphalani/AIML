name = input("Enter your name: ")
age = int(input("Enter your age: "))
fav_number = float(input("Enter your favorite number: "))

print(f"Hello, {name}!")

current_year = 2025
years_to_100 = 100 - age
year_100 = current_year + years_to_100
print(f"You will turn 100 in the year {year_100}.")

doubled_number = fav_number * 2
print(f"Your favorite number doubled is {doubled_number}.")