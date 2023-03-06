contents = ["Lorem "
            "Ipsum",
            "Lero Lero",
            "Random content"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

a = "I am a string " \
    "on my " \
    "own"

for content, filename in zip(contents, filenames):
    file = open(f"../files/bonus/{filename}", "w")
    file.write(content)

file = open('../files/bonus/logs.txt', 'w')
file.write('101.102.103.222 GET 01.988')
file.close()

file = open('../files/bonus/logs.txt', 'w')
file.write('171.131.104.108 POST 2.143')
file.close()
