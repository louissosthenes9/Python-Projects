import time
import re

score = 0
start_time = 0
questions_with_options = [
    ("What is the capital of Japan?", ["A. Tokyo", "B. Beijing", "C. Seoul", "D. Bangkok"], "A"),
    ("Who is the author of 'To Kill a Mockingbird'?",
     ["A. J.K. Rowling", "B. Harper Lee", "C. George Orwell", "D. Ernest Hemingway"], "B"),
    ("What is the largest ocean on Earth?",
     ["A. Atlantic Ocean", "B. Indian Ocean", "C. Southern Ocean", "D. Pacific Ocean"], "D"),
    ("Which element has the chemical symbol 'O'?", ["A. Oxygen", "B. Gold", "C. Iron", "D. Uranium"], "A"),
    ("Who painted the Mona Lisa?",
     ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"], "C"),
    ("In which year did the Titanic sink?", ["A. 1912", "B. 1920", "C. 1905", "D. 1931"], "A"),
    ("What is the largest planet in our solar system?", ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"], "B"),
    ("Who developed the theory of relativity?",
     ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Stephen Hawking"], "B"),
    ("Which country is known as the Land of the Rising Sun?", ["A. China", "B. South Korea", "C. Japan", "D. Vietnam"],
     "C"),
    ("What is the capital of Australia?", ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"], "C"),
]


def displayQns():
    for qns, options, correct_answer in questions_with_options:
        print("------------------------*****--------------------\n")
        print(qns)
        for option in options:
            print(option)
        user_answer = input("Your answer: ").upper()
        checkAns(user_answer, correct_answer)


def checkAns(user_answer, correct_answer):
    global score
    valid_option_pattern = re.compile(r'^[A-D]$')
    if user_answer.strip() == "":
        print("Please answer the question!")
        user_answer = input("Your answer: ").upper()
        checkAns(user_answer, correct_answer)
    elif not valid_option_pattern.match(user_answer):
        print("Invalid choice! Please enter a valid option (A, B, C, or D).")
        user_answer = input("Your answer: ").upper()
        checkAns(user_answer, correct_answer)
    elif user_answer == correct_answer:
        print("Correct!")
        score += 1

    else:
        print(f"Wrong! The correct answer is {correct_answer}")

def report():
    global start_time
    print(f"Quiz completed! Your score is {score}/{len(questions_with_options)}")
    elapsed_time = (time.time() - start_time) // 60  # Divide by 60 to get minutes
    user_minutes = round(elapsed_time)
    user_seconds = round((elapsed_time - user_minutes)%60)


    if user_minutes < 1:
        print(f"You have spent {user_minutes}:{user_seconds} during the quiz.\n you are blazing fast")
    else:
        print(f"You have spent {user_minutes}:{user_seconds}")

def displayScore():
    for _ in range(3):
        print("------------------------*****--------------------\n")
    print("Thanks for attempting the quiz and here is your report")

    if score >= 8:
        print("Congratulations! you are a certified genius")
        report()
    elif 5 <= score < 8:
        print("Great effort,you are spectacular")
        report()
    else:
        print("Sorry better luck next time")
        report()


def startTimer():
    start_time = time.time()



def startGame():
    startTimer()
    displayQns()
    displayScore()


startGame()
