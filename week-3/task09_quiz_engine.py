questions = [
    {"id": 1, "question": "What is the data type of 3.14 in Python?",
     "choices": ["str", "float", "bool", "int"], "answer": "float"},

    {"id": 2, "question": "What is printed by print(10//30)?",
     "choices": ["0", "3", "0.33", "1"], "answer": "0"},

    {"id": 3, "question": "Which keyword defines a function in Python?",
     "choices": ["func", "define", "def", "function"], "answer": "def"},

    {"id": 4, "question": "What is printed by print(i, end='') for i in range(3)?",
     "choices": ["3", "0123", "123", "012"], "answer": "012"},

    {"id": 5, "question": "What does return do inside a function?",
     "choices": ["define a variable", "prints a value automatically",
                 "ends the function and optionally provides a result",
                 "repeats the function"],
     "answer": "ends the function and optionally provides a result"}
]


def validateAnswer(question, answer):
    if answer.lower() in [choice.lower() for choice in question["choices"]]:
        return True
    else:
        return False


def checkAnswer(question, answer):
    if answer.lower() == question["answer"].lower():
        print("Correct answer!")
        return True
    else:
        print("Incorrect answer!")
        print("The correct answer is:", question["answer"])
        return False


def updateScore(score):
    return score + 1


def calculatePercentage(score, questions):
    return (score / len(questions)) * 100


def displayResults(score, incorrect, questions):
    average = calculatePercentage(score, questions)

    print("\nFinal score:", score, "/", len(questions))
    print("Correct answers:", score)
    print("Incorrect answers:", incorrect)
    print(f"Percentage: {average:.1f}%")

    if average >= 80:
        print("Excellent!")
    elif average >= 60:
        print("Good job!")
    elif average >= 40:
        print("Keep practicing!")
    else:
        print("Keep learning!")


def displayQuestion(questions):
    score = 0
    incorrect = 0

    for question in questions:
        print(f"\n{question['id']}. {question['question']}")

        for i, choice in enumerate(question["choices"], start=1):
            print(f"{i}. {choice}")

        while True:
            answer = input("Enter your answer: ").strip()

            if validateAnswer(question, answer):
                break
            else:
                print("Invalid answer! Please choose one of the given options.")

        if checkAnswer(question, answer):
            score = updateScore(score)
        else:
            incorrect += 1

        print(f"Current score: {score}/{len(questions)}")

    displayResults(score, incorrect, questions)


while True:
    displayQuestion(questions)

    play_again = input("\nWould you like to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thank you for playing!")
        break
