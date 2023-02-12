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


def addition():
    num1 = random_number()
    num2 = random_number()
    operation = f"{num1} + {num2}"
    print(operation)
    return num1 + num2


def multiplication():
    num1 = random.randint(2, 10)
    num2 = random.randint(1, 20)
    operation = f"{num1} * {num2}"
    print(operation)
    return num1 * num2


def subtraction():
    num1 = random_number()
    num2 = random_number()
    operation = f"{num1} - {num2}"
    print(operation)
    return num1 - num2
