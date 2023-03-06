
def parse(feet_inches):
    values = feet_inches.split(" ")
    feet_local = float(values[0])
    inches_local = float(values[1])
    return {"feet": feet_local, "inches": inches_local}


def convert(feet_local, inches_local):
    meters = feet_local * 0.3048 + inches_local * 0.0254
    return meters


user_input = input("Enter feet and inches: ")

parsed_input = parse(user_input)
feet = parsed_input["feet"]
inches = parsed_input["inches"]

converted_value = convert(feet, inches)
print(f"{feet} feet and {inches} inches is {converted_value} meters")

if converted_value < 1:
    print("Kid is too small.")
else:
    print("Kid is high enough to have fun.")
