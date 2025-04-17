import csv
import random
import time
import os
import sys

def readBank():
    """
    Reads the quiz questions from a CSV file and returns them as a list of rows.
    """
    path = "C:\\Users\\Logan\\OneDrive\\Desktop\\CPSC 236 Final\\CPSC 236 TestBank.csv"
    with open(path, newline="") as file:
        reader = csv.reader(file)
        next(reader)
        return list(reader)

def tenQuiz(allRows):
    """
    Administers a 20-question quiz and returns the score, elapsed time, and response details.
    """
    startTime = time.time()
    score = 0
    answers = []
    randomRows = random.sample(allRows, 10)
    labels = ["A", "B", "C"]

    for i, row in enumerate(randomRows, start=1):
        elapsed = time.time() - startTime
        if elapsed > 600:
            print("\nTime is up quiz ending.\n")
            break

        print(f"\nQuestion {i}: {row[0]}")
        choices = row[1:4]
        for label, choice in zip(labels, choices):
            if choice.strip():
                print(f"{label}. {choice}")

        correct = row[4].strip().upper()  # fix here

        while True:
            userAnswer = input("Your answer (A/B/C): ").strip().upper()
            if userAnswer in labels[:len(choices)]:
                break
            print("Invalid input. Try A, B, or C.")

        if userAnswer == correct:
            score += 1

        answers.append({
            "question": row[0],
            "correct": correct,
            "student": userAnswer
        })

    endTime = time.time()
    return score, endTime - startTime, answers


def twentyQuiz(allRows):
    """
    Administers a 20-question quiz and returns the score, elapsed time, and response details.
    """
    startTime = time.time()
    score = 0
    answers = []
    randomRows = random.sample(allRows, 20)
    labels = ["A", "B", "C"]

    for i, row in enumerate(randomRows, start=1):
        elapsed = time.time() - startTime
        if elapsed > 600:
            print("\nTime is up quiz ending.\n")
            break

        print(f"\nQuestion {i}: {row[0]}")
        choices = row[1:4]
        for label, choice in zip(labels, choices):
            if choice.strip():
                print(f"{label}. {choice}")

        correct = row[4].strip().upper()  # fix here

        while True:
            userAnswer = input("Your answer (A/B/C): ").strip().upper()
            if userAnswer in labels[:len(choices)]:
                break
            print("Invalid input. Try A, B, or C.")

        if userAnswer == correct:
            score += 0.5

        answers.append({
            "question": row[0],
            "correct": correct,
            "student": userAnswer
        })

    endTime = time.time()
    return score, endTime - startTime, answers

def authenticate(id):
    """
    Validates that the ID starts with 'A' and is followed by five digits between 1 and 9.
    """
    if len(id) != 6:
        return False
    if id[0] != "A":
        return False
    for digit in id[1:]:
        if not digit.isdigit() or int(digit) not in range(1, 10):
            return False
    return True

def writeResult(studentId, first, last, score, timeElapsed, results):
    """
    Writes the quiz results to a text file named using the student's ID and name.
    """
    fileName = f"{studentId}_{first}_{last}.txt"
    with open(fileName, "w") as file:
        file.write(f"ID: {studentId}\n")
        file.write(f"name: {first} {last}\n")
        file.write(f"score: {score}\n")
        file.write(f"elapsed time: {timeElapsed:.2f} seconds\n\n")
        for i, result in enumerate(results, start=1):
            file.write(f"question {i}: {result['question']}\n")
            file.write(f"correct: {result['correct']}, Your Answer: {result['student']}\n\n")

def main():
    """
    The main control function for starting, running, and looping quizzes for students.
    """
    while True:
        first = input("Enter your first name: ")
        last = input("Enter your last name: ")

        attempts = 0
        while attempts < 3:
            studentId = input("Enter your student ID: ").strip()
            if authenticate(studentId):
                break
            print("Invalid ID. Format: A12345 (A followed by five digits 1-9)")
            attempts += 1
        else:
            print("Too many invalid attempts. Exiting.")
            sys.exit()

        questions = readBank()

        while True:
            numQuestions = input("Would you like to take a 10 or 20 question quiz? ").strip()
            if numQuestions == "10" or numQuestions.lower() == "ten":
                score, timeTaken, answers = tenQuiz(questions)
                count = 10
                break
            elif numQuestions == "20" or numQuestions.lower() == "twenty":
                score, timeTaken, answers = twentyQuiz(questions)
                count = 20
                break
            print("Please enter 10 or 20.")

        print(f"\nFinal Score: {score} / {count}")
        print(f"Time Taken: {timeTaken:.2f} seconds")

        writeResult(studentId, first, last, score, timeTaken, answers)

        nextAction = input('\nEnter "S" to start a new quiz or "Q" to quit: ').strip().upper()
        if nextAction == "Q":
            break
        elif nextAction == "S":
            os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()
