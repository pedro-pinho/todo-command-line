def parse(feet_inches):
    values = feet_inches.split(" ")
    feet_local = float(values[0])
    inches_local = float(values[1])
    return {"feet": feet_local, "inches": inches_local}


