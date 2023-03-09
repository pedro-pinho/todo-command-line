import json

with open("../files/questions.json", "r") as file:
    content = file.read()

if not content:
    exit("No questions found!")

data = json.loads(content)
score = 0
for question in data:
    print(question["question_text"])
    for index, item in enumerate(question["alternatives"]):
        alternative = f"{index + 1}.{item.capitalize()}"
        print(alternative)
    user_answer = int(input("Type your answer: ")) - 1
    question["user_answer"] = user_answer

print("\nDone! Let's see your results...\n")

for index, question in enumerate(data):
    user_correct = "Incorrect"
    if question["user_answer"] == question["correct_answer"]:
        user_correct = "Correct"
        score = score + 1
    print(f"For question {index+1} answer was... {user_correct}!")
    if user_correct == "Incorrect":
        print(f"  Right answer: {question['alternatives'][question['correct_answer']]}")
print(f"\nTotal Score: {score}/{len(data)}")
