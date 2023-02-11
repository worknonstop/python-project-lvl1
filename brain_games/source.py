import prompt


def welcome():
    print("Welcome to the Brain Games!\nMay I have your name? ")


def user_name():
    name = prompt.string("")
    return name
