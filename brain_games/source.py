import random

import prompt


def welcome():
    print("Welcome to the Brain Games!")
    print("May I have your name? ", end="")


def user_name():
    name = prompt.string("")
    return name


def is_even():
    welcome()
    name = user_name()
    print(f"Hello {name}")
    print('Answer "yes" if the number is even, otherwise answer "no"')
    wrong_no = "'no' is wrong answer ;/(. Correct answer was 'yes"
    wrong_yes = "'yes' is wrong answer ;/(. Correct answer was 'no'"
    try_again = f"Let's try again, {name}"

    i = 0
    while i < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = prompt.string("")
        no_answer = user_answer == "no"
        yes_answer = user_answer == "yes"
        even_number = number % 2 == 0
        uneven_number = number % 2 != 0
        print(f"Answer: {user_answer}")

        if even_number and no_answer:
            print(wrong_no)
            break
        elif uneven_number and yes_answer:
            print(wrong_yes)
            break
        elif even_number and yes_answer:
            print("Correct!")
            i += 1
        elif uneven_number and no_answer:
            print("Correct!")
            i += 1
        else:
            print(f"Let's try again, {name}")
            break

    if i == 3:
        print(f"Congratulations, {name}!")
    else:
        print(try_again)
