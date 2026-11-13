questions = [
    {
        "question": "What is the capital of Ethiopia?",
        "options": ["A. Nairobi", "B. Addis Ababa", "C. Cairo", "D. Kampala"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web page structure?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "answer": "C"
    },
    {
        "question": "How many days are there in a week?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Boolean", "C. Integer", "D. List"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    }
]


# Display a question and its options
def display_question(question, number):
    print(f"\nQuestion {number}: {question['question']}")

    for option in question["options"]:
        print(option)


# Check whether the answer is a valid option
def validate_answer(answer):
    return answer.upper() in ["A", "B", "C", "D"]


# Check whether the answer is correct
def check_answer(user_answer, correct_answer):
    return user_answer.upper() == correct_answer


# Update the score
def update_score(score, is_correct):
    if is_correct:
        score += 1
    return score


# Display the final results
def display_results(score, total):
    incorrect = total - score
    percentage = (score / total) * 100

    print("\n========== QUIZ RESULTS ==========")
    print("Total questions:", total)
    print("Correct answers:", score)
    print("Incorrect answers:", incorrect)
    print("Final score:", str(score) + "/" + str(total))
    print(f"Percentage: {percentage:.2f}%")

    # Result category
    if percentage >= 80:
        print("Category: Excellent!")
    elif percentage >= 60:
        print("Category: Good!")
    elif percentage >= 40:
        print("Category: Average!")
    else:
        print("Category: Needs Improvement")

    print("==================================")


# Main quiz function
def play_quiz():
    score = 0

    for i in range(len(questions)):
        question = questions[i]

        display_question(question, i + 1)

        while True:
            answer = input("Your answer (A/B/C/D): ").strip()

            if validate_answer(answer):
                break
            else:
                print("Invalid option! Please enter A, B, C, or D.")

        if check_answer(answer, question["answer"]):
            print("Correct!")
            score = update_score(score, True)
        else:
            print("Incorrect!")
            print("Correct answer:", question["answer"])

    display_results(score, len(questions))


# Allow the user to play again
while True:
    print("\n========== QUIZ GAME ==========")
    play_quiz()

    again = input("\nDo you want to play again? (yes/no): ").strip().lower()

    if again != "yes":
        print("Thank you for playing!")
        break