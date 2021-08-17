questions = {
    "Who created Python? ": "A",
    "What year was Python created? ": "B",
    "Python is tributed in which comedy group? ": "C",
    "What is the best anime in the world rn?": "D"
}

options = [ ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
            ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
            ["A. something", "B. Something", "C. Mothy Python", "D. Someone"],
            ["A. Demon Slayer", "B. HxH", "C. Rent a Girlfriend", "D. JJBA"]
]

def newGame():
    guesses = []
    correct_guesses = 0
    questions_num = 0

    for key in questions:
        print("-------------------")
        print(key)
        for i in options[questions_num]:
            print(i)

        guess = input("Your answer (a/b/c/d) is?: ").upper()
        guesses.append(guess)
        correct_guesses += checkAnswer(questions.get(key), guess)
        questions_num += 1
    displayScore(correct_guesses, guesses)

#----------------------------------
def checkAnswer(answer, guess):
    if answer == guess:
        print("Correct! ")
        return 1
    else:
        print("Wrong! ")
        return 0


# ----------------------------------

def checkScore():
    pass

# ----------------------------------

def displayScore(correct_guesses, guesses):
    print("-------------------")
    print("RESULTS")
    print("-------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: " + str(score) + "%")



# ----------------------------------
def playAgain():

        responce = input("Do you want to try again? (yes or no): ").lower()
        if responce == "yes":
            return True
        else:
            return False

newGame()
while playAgain():
    newGame()
print("Bye, have a great day!")