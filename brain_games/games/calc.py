from brain_games import logic


def calc_game():
    logic.welcome()
    logic.user_name()
    print("What is the result of the experssion?")
    random_list = ["+", "*", "-"]
    random_operator = logic.random.choice(random_list)
    if random_operator == "+":
        operation = logic.addition()
    elif random_operator == "*":
        operation = logic.multiplication()
    else:
        operation = logic.subtraction()
    return operation
