import prompt


def welcome():
    print("Welcome to the Brain Games!")
    print("May I have your name? ", end="")


def user_name():
    name = prompt.string("")
    print(f"Hello {user_name()}")
    return name
