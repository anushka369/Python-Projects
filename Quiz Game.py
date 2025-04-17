import time
import random

# Get all types of Python quiz questions
def get_python_questions():
    return [
        {
            "type": "MCQ",
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A) func", "B) define", "C) def", "D) function"],
            "answer": "C"
        },
        {
            "type": "MCQ",
            "question": "What is the output of print(2 ** 3) in Python?",
            "options": ["A) 6", "B) 8", "C) 9", "D) 10"],
            "answer": "B"
        },
        {
            "type": "MCQ",
            "question": "Which data type is mutable in Python?",
            "options": ["A) Tuple", "B) String", "C) List", "D) Integer"],
            "answer": "C"
        },
        {
            "type": "MCQ",
            "question": "Which of the following is used to take input from the user?",
            "options": ["A) input()", "B) print()", "C) scan()", "D) read()"],
            "answer": "A"
        },
        {
            "type": "MCQ",
            "question": "What will be the output of len('Python')?",
            "options": ["A) 5", "B) 6", "C) 7", "D) Error"],
            "answer": "B"
        },
        {
            "type": "TF",
            "question": "Python supports multiple inheritance.",
            "answer": "True"
        },
        {
            "type": "TF",
            "question": "In Python, indentation is not necessary.",
            "answer": "False"
        },
        {
            "type": "FILL",
            "question": "Fill in the blank: The ______ keyword is used to handle exceptions in Python.",
            "answer": "try"
        },
        {
            "type": "FILL",
            "question": "Fill in the blank: In Python, dictionaries are enclosed in ______ braces.",
            "answer": "curly"
        },
    ]


# Countdown timer with a warning in the last 3 seconds
def countdown_timer():
    print("\nYou have 10 seconds to answer. Type 'S' to skip.")
    for i in range(10, 0, -1):
        if i <= 3:
            print(f"\r⚠️ Hurry up! Time left: {i} seconds ", end="")
          
        else:
            print(f"\rTime left: {i} seconds ", end="")
        time.sleep(1)
    print("\n")


# Display question with or without options depending on the type
def display_question(question_data, question_number):
    print("\n====================")
    print(f"Question {question_number}: {question_data['question']}")
    
    if question_data["type"] == "MCQ":
        for option in question_data["options"]:
            print(option)


# Get user input and allow skipping
def get_user_answer(q_type):
    if q_type == "MCQ":
        user_answer = input("Enter your answer (A, B, C, D or S to skip): ").strip().upper()
        if user_answer in ["A", "B", "C", "D", "S"]:
            return user_answer
          
    elif q_type == "TF":
        user_answer = input("Enter True or False (or S to skip): ").strip().capitalize()
        if user_answer in ["True", "False", "S"]:
            return user_answer
          
    elif q_type == "FILL":
        user_answer = input("Type your answer (or S to skip): ").strip().lower()
        if user_answer:
            return user_answer
          
    return None


# Check if the answer is correct
def check_answer(user_answer, correct_answer):
    if user_answer == "S":
        print("You skipped this question.\n")
        return None  # No effect on score
      
    if user_answer.lower() == correct_answer.lower():
        print("✅ Answer is correct!\n")
        return 1
      
    else:
        print(f"❌ Wrong answer! The correct answer is: {correct_answer}\n")
        return 0


# Update the score
def update_score(score, result):
    if result == 1:
        score += 1
    return score


# Start the quiz
def play_quiz():
    print("🎯 Welcome to the Python Quiz!")
    questions = get_python_questions()
    random.shuffle(questions)
    score = 0
    i = 1

    for question in questions:
        display_question(question, i)
        countdown_timer()
        user_answer = get_user_answer(question["type"])
        result = check_answer(user_answer, question["answer"])
      
        if result is not None:
            score = update_score(score, result)
        i += 1

    print(f"\n🏁 Your final score is: {score} / {len(questions)}")
    print("🎉 Thanks for playing!")


# Entry point
if __name__ == "__main__":
    play_quiz()
