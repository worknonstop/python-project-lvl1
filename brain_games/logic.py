import random

import prompt


# Welcome user
def welcome():
    print("Welcome to the Brain Games!")
    print("May I have your name? ", end="")


# Prompt username
def user_name():
    name = prompt.string("")
    print(f"Hello {name}")
    return name


def welcome_user():
    welcome()
    user_name()


def random_number():
    return random.randint(1, 100)


def random_question():
    num1 = random_number()
    num2 = random_number()

    operators = ["+", "*", "-"]
    random_operator = random.choice(operators)
    if random_operator == "+":
        return f"{num1} + {num2}"
    elif random_operator == "*":
        return f"{num1} * {num2}"
    else:
        return f"{num1} - {num2}"
