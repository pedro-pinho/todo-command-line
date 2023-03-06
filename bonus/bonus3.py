filenames = ["1.doc", "1.report", "1.presentation"]

filenames = [filename.replace(".", "-") + ".txt" for filename in filenames]

print(filenames)

usernames = ["john 1990", "alberta1970", "magnola2000"]
chars = [len(item) for item in usernames]
print(chars)

user_entries = ['10', '19.1', '20']
user_numbers = [float(item) for item in user_entries]
print(user_numbers)
print(sum(user_numbers))
