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


# User answer
def user_answer():
    return prompt.string("")


def random_number():
    return random.randint(1, 10)


# Check, is even number or not
def check_number(number):
    if number % 2 == 0:
        return "yes"
    else:
        return "no"


def random_question_calc():
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


# Search greatest common divisor
def gcd(a, b):
    while True:
        if a % b == 0:
            return b
        else:
            new = a % b
            a = b
            b = new
