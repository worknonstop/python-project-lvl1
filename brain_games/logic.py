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


def lst_progression(step):
    begin = random.randint(1, 50)
    length = random.randint(5, 10)

    numbers = []
    i = 0
    while i < length:
        numbers.append(begin)
        begin += step
        i += 1

    return numbers
