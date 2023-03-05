import random


def generate_rolls():
    rolls = []
    for i in range(0, 4):  # 4 digits to guess
        rolls.append(random.randint(1, 6))
    print(rolls)
    return rolls


def compare_guess(guess, roll_to_guess):  # returns if all 4 digits are found or not
    numbers = [int(i) for i in guess]
    correct_numbers = [0] * 4
    counter = 0  # counts how many matches there are
    for i in range(0, 4):  # 4 digits to guess
        if numbers[i] == roll_to_guess[i]:
            correct_numbers[i] = numbers[i]
            counter += 1
    print("You currently have ", counter, "correct")
    print(correct_numbers)
    return counter == 4


guesses = 12
random_rolls = generate_rolls()
print("Roll generated: ")
while guesses > 0:
    print("you have ", guesses, " guesses left!")
    user_guess = input("type in a four digit number guess.\n")
    if compare_guess(user_guess, random_rolls):
        print("all 4 digits found!")
        guesses = 0
    else:
        guesses -= 1
