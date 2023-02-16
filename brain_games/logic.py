import random

import prompt


# Welcome user
def welcome():
    print("Welcome to the Brain Games!")
    print("May I have your name? ", end="")


# Prompt username
def user_name():
    name = prompt.string("")
    print(f"Hello, {name}!")
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


def is_more(num1, num2):
    if num1 > num2:
        return gcd(num1, num2)
    else:
        return gcd(num2, num1)


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


def mod_list(lst):
    index = random.randint(0, len(lst) - 1)
    number = lst[index]
    lst[index] = ".."
    number_and_list = (lst, number)
    return number_and_list


def list_to_string(lst):
    string = ""

    for el in lst:
        string += str(el) + " "

    return string


def is_prime(n):
    if n < 2:
        return "no"

    i = 2
    while i <= n / 2:
        if n % i == 0:
            return "no"
        else:
            i += 1

    return "yes"
