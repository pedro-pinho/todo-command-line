try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percentage = (value/total_value)*100
    print(f"That is {percentage}%")
except ValueError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Your total value cannot be zero.")


try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    if width == length:
        exit("That looks like a square")

    area = width*length
    print(f"Area is {area}")
except ValueError:
    print("Invalid number")
