import glob

myfiles = glob.glob("../files/*.txt")

for filepaths in myfiles:
    with open(filepaths, "r") as file:
        print(file.read())
    print("EOF")
