def age(year_of_birth, current_year=2023):
    return int(current_year) - int(year_of_birth)


user_input = input("What is your year of birth? ")
user_age = age(user_input)
if user_age > 120:
    print("You old fuck")
else:
    print(user_age)

