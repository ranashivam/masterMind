import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generateCode():
    code = []
    for _ in range(CODE_LENGTH):
        value = random.choice(COLORS)
        code.append(value)

    # print(code)
    return code


def guessCode():
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid Color: {COLORS}")
                break
        else:
            break

    return guess

def checkCode(guess, realCode):
    colorCount = {}
    correctPos = 0
    inCorrectPos = 0

    for color in realCode:
        if color not in colorCount:
            colorCount[color] = 0
        colorCount[color] += 1

    for guessColor, realColor in zip(guess, realCode):
        if guessColor == realColor:
            correctPos += 1
            colorCount[guessColor] -= 1

    for guessColor, realColor in zip(guess, realCode):
        if guessColor in colorCount and colorCount[guessColor] > 0:
            inCorrectPos += 1
            colorCount[guessColor] -= 1

    return correctPos, inCorrectPos


def game():
    print(f"Welcome to mastermind, you have {TRIES} to guess the code...")
    print(f"The valid colors are: {COLORS}")

    code = generateCode()
    for attempts in range(1, TRIES + 1):
        guess = guessCode()
        correctPos, inCorrectPos = checkCode(guess, code)

        if correctPos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break

        print(f"Correct Positions: {correctPos} | Incorrect Positions: {inCorrectPos}")

    else:
        print(f"You ran out of tries, the code was:" , *code)

if __name__ == "__main__":
    game()