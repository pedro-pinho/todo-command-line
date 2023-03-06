import parsers
from bonus.converters import convert

user_input = input("Enter feet and inches: ")

parsed_input = parsers.parse(user_input)
feet = parsed_input["feet"]
inches = parsed_input["inches"]

converted_value = convert(feet, inches)
print(f"{feet} feet and {inches} inches is {converted_value} meters")

if converted_value < 1:
    print("Kid is too small.")
else:
    print("Kid is high enough to have fun.")
