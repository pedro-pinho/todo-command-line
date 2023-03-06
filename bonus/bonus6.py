password = input("Enter new password: ")
result = {}
# Check for length
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False
# Check for digits
number_exists = any(i.isdigit() for i in password)
result["digits"] = number_exists
# Check for uppercase
uppercase_exists = any(i.isupper() for i in password)
result["uppercase"] = uppercase_exists

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")
