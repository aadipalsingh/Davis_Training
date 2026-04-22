'''Quiz System

Features:

Load questions from file
Ask user
Score calculation
Handle invalid input'''
import csv   # used to read CSV file


# ---------------- LOAD QUESTIONS ----------------
def load_questions(filename):
    questions = []

    try:
        # open file in read mode
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)

            # read each row and store as dictionary
            for row in reader:
                questions.append(row)

    except FileNotFoundError:
        print("Question file not found!")

    return questions


# ---------------- QUIZ FUNCTION ----------------
def run_quiz(questions):
    score = 0   # initialize score

    # loop through each question
    for i, q in enumerate(questions, start=1):

        print(f"\nQ{i}: {q['question']}")

        # display options
        print("1.", q['option1'])
        print("2.", q['option2'])
        print("3.", q['option3'])
        print("4.", q['option4'])

        # ----------- HANDLE USER INPUT -----------
        while True:
            try:
                user_ans = int(input("Enter your answer (1-4): "))

                # check valid range
                if user_ans < 1 or user_ans > 4:
                    print("Please enter a number between 1 and 4.")
                    continue

                break   # valid input → exit loop

            except ValueError:
                print("Invalid input! Enter a number.")

        # ----------- CHECK ANSWER -----------
        if user_ans == int(q['answer']):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is option {q['answer']}")

    # ----------- FINAL SCORE -----------
    print("\n--- Quiz Finished ---")
    print(f"Your Score: {score}/{len(questions)}")


# ---------------- MAIN PROGRAM ----------------
def main():
    filename = "questions.csv"

    questions = load_questions(filename)

    if questions:   # only run quiz if file loaded
        run_quiz(questions)


# run program
main()