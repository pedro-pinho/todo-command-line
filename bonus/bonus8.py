def get_average():
    try:
        with open("data.txt", "r") as file:
            content = file.readlines()
        values = content[1:]
        total_sum = sum(float(value) for value in values)
        result = total_sum/len(values)
        return result
    except ValueError:
        return 0


average = get_average()
print(f"The average of all temperatures is: {average}")
